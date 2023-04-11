import re
import const
from linebot import LineBotApi
from linebot.models import (MessageAction, QuickReply, QuickReplyButton,
                            TextSendMessage)


def reply_message_for_line(reply_token, completed_text):
    try:
        # Create an instance of the LineBotApi with the Line channel access token
        line_bot_api = LineBotApi(const.LINE_CHANNEL_ACCESS_TOKEN)

        message = None
        keyword = '--- predictions ---'
        if keyword in completed_text:
            # キーワードで分割。キーワードは含まない。第2引数は分割数。
            completed_texts = completed_text.split(keyword, 1)
            # ユーザーに返却するテキストを取得。文字列の前後の空白と改行を削除
            assistant_answer = completed_texts[0].strip()
            # キーワード以降のテキストを取得
            prediction_text = completed_texts[1]
            # 改行で分割し、文字列の前後の空白と改行を削除
            predictions = map(lambda line: remove_ordinal_number(line.strip()), prediction_text.strip().split('\n'))
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
        else:
            message = TextSendMessage(text=completed_text)
            print('The keyword is not found in the text.')

        # Reply the message using the LineBotApi instance
        # line_bot_api.reply_message(reply_token, TextSendMessage(text=completed_text))
        line_bot_api.reply_message(reply_token, message)

    except Exception as e:
        # Raise the exception
        raise e


# 文字列の先頭にある序数を削除する関数
def remove_ordinal_number(text):
    # 正規表現で先頭の数字とピリオドを削除
    return re.sub(r'^\d+\.\s*', '', text)
