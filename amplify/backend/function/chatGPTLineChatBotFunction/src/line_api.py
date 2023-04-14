from typing import List

import const
from linebot import LineBotApi
from linebot.models import (MessageAction, QuickReply, QuickReplyButton,
                            TextSendMessage)


def reply_message_for_line(reply_token: str, assistant_answer: str, predictions: List[str]):
    try:
        # Create an instance of the LineBotApi with the Line channel access token
        line_bot_api = LineBotApi(const.LINE_CHANNEL_ACCESS_TOKEN)
        # predications 配列内の要素の文字列が21文字以上の場合配列から削除
        predictions = list(filter(lambda line: len(line) <= 20 and line != "", predictions))
        # predications が空だったら message に TextSendMessage を設定
        if len(predictions) == 0:
            message = TextSendMessage(text=assistant_answer)
        else:
            # クイックリプライアクションを作成
            quick_reply_actions = map(lambda line: QuickReplyButton(action=MessageAction(label=line, text=line)), predictions)
            # クイックリプライオブジェクトを作成
            quick_reply = QuickReply(items=quick_reply_actions)
            # テキストメッセージにクイックリプライを追加
            message = TextSendMessage(text=assistant_answer, quick_reply=quick_reply)

        # Reply the message using the LineBotApi instance
        line_bot_api.reply_message(reply_token, message)

    except Exception as e:
        raise e
