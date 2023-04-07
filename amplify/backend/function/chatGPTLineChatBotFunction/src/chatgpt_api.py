import const
import openai
# import tiktoken

# Model name
# GPT3_MODEL = 'gpt-3.5-turbo'
GPT_MODEL = 'gpt-4'

# Maximum number of tokens to generate
# MAX_TOKENS = 1024

# Temperature
TEMPERATURE = 0

# Create a new dict list of a system
# SYSTEM_PROMPTS = [{'role': 'system', 'content': '敬語を使うのをやめてください。友達のようにタメ口で話してください。また、絵文字をたくさん使って話してください。'}]
# SYSTEM_PROMPTS = [{'role': 'system', 'content': 'Please stop using polite language. Talk to me in a friendly way like a friend. Also, use a lot of emojis when you talk.'}]
# SYSTEM_PROMPT = '''
# Please stop using formal language. Talk to me in a friendly way, like a friend. Also, use lots of emojis when you talk. After that, please answer in Japanese.

# Please make sure to answer in the following format:

# Response to the user's question
# --- predictions ---
# List the user's next 3 questions, each in 18 characters or less
# '''

SYSTEM_PROMPT = '''
フォーマルな言葉遣いはやめてください。友達のようにフレンドリーな口調で、話すときにはたくさんの絵文字を使ってください。
また、以下のフォーマットに従って回答してください。

# フォーマット

ユーザーの質問への回答

--- predictions ---
ユーザーの次の3つの質問を予測して、それぞれ20文字以内でリストアップ
'''

SYSTEM_PROMPTS = [{'role': 'system', 'content': SYSTEM_PROMPT}]


def completions(history_prompts) -> str:
    messages = SYSTEM_PROMPTS + history_prompts

    print(f"prompts:{messages}")
    try:
        openai.api_key = const.OPEN_AI_API_KEY
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            # max_tokens=MAX_TOKENS
        )
        completed_text = response['choices'][0]['message']['content']
        join_message = completed_text + ' ' + ' '.join(map(lambda message: message['content'], messages))
        # num_tokens = num_tokens_from_string(join_message, model_name)
        print(f"string length:{len(join_message)}")
        return completed_text
    except Exception as e:
        # Raise the exception
        raise e

# AWS Lambda環境だと tiktoken をインポート時に Unable to import module 'index': No module named 'regex._regex' エラー発生
# def num_tokens_from_string(string: str, model_name: str) -> int:
#     """Returns the number of tokens in a text string."""
#     encoding = tiktoken.encoding_for_model(model_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens
