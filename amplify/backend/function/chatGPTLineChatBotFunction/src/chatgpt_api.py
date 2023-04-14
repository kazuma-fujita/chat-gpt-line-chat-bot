import const
import openai
import re
from typing import List, Tuple, Dict

# Model name
GPT_MODEL = 'gpt-4'  # or gpt-3.5-turbo

# Temperature
TEMPERATURE = 0.7

PREDICTION_KEYWORD = '### Predictions ###'

SYSTEM_PROMPT = f'''フォーマルな言葉遣いはやめてください。友達のようにフレンドリーな口調で、話すときにはたくさんの絵文字を使ってください。
また、以下のフォーマットに従って回答してください。

# フォーマット

ユーザーの質問への回答

{PREDICTION_KEYWORD}
ユーザーの次の3つの質問を予測して、それぞれ20文字以内でリストアップ
'''

DEFAULT_PREDICTION_TEXT = f'''{PREDICTION_KEYWORD}
1. ChatGPTって何ですか？
2. ChatGPTでは何ができますか？
3. どんな質問に答えてくれますか？
'''

SYSTEM_PROMPTS = [{'role': 'system', 'content': SYSTEM_PROMPT}]


def _parse_completed_text(completed_text: str) -> Tuple[str, List[str]]:
    # キーワードで分割。キーワードは含まない。第2引数は分割数。
    completed_texts = completed_text.split(PREDICTION_KEYWORD, 1)
    if len(completed_texts) < 2:
        raise Exception('The keyword is not found in the text.')
    # ユーザーに返却するテキストを取得。文字列の前後の空白と改行を削除
    assistant_answer = completed_texts[0].strip()
    # キーワード以降のテキストを取得
    prediction_text = completed_texts[1]
    # 改行で分割し、文字列の前後の空白と改行を削除
    predictions = list(map(lambda line: _remove_ordinal_number(line.strip()), prediction_text.strip().split('\n')))
    return assistant_answer, predictions


# 文字列の先頭にある序数を削除する関数
def _remove_ordinal_number(text: str) -> str:
    # 正規表現で先頭の数字とピリオドを削除
    return re.sub(r'^\d+\.\s*', '', text)


def _print_total_length(completed_text, messages):
    join_message = completed_text + ' ' + ' '.join(map(lambda message: message['content'], messages))
    print(completed_text.replace('\n', ''))
    print(f"total length:{len(join_message)}")


def completions(history_prompts: List[Dict[str, str]]) -> Tuple[str, str, List[str]]:
    messages = SYSTEM_PROMPTS + history_prompts

    try:
        openai.api_key = const.OPEN_AI_API_KEY
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
        )
        completed_text = response['choices'][0]['message']['content']

        if PREDICTION_KEYWORD not in completed_text:
            completed_text = f'{completed_text}\n{DEFAULT_PREDICTION_TEXT}'

        _print_total_length(completed_text, messages)

        assistant_answer, predictions = _parse_completed_text(completed_text)

        return completed_text, assistant_answer, predictions
    except Exception as e:
        raise e
