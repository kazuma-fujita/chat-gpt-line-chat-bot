import const
import openai
# import tiktoken

# Model name
# GPT3_MODEL = 'gpt-3.5-turbo'
GPT_MODEL = 'gpt-4'

# Maximum number of tokens to generate
MAX_TOKENS = 1024

# Create a new dict list of a system
# SYSTEM_PROMPTS = [{'role': 'system', 'content': '敬語を使うのをやめてください。友達のようにタメ口で話してください。また、絵文字をたくさん使って話してください。'}]
SYSTEM_PROMPTS = [{'role': 'system', 'content': 'Please stop using polite language. Talk to me in a friendly way like a friend. Also, use a lot of emojis when you talk.'}]


def completions(history_prompts) -> str:
    messages = SYSTEM_PROMPTS + history_prompts

    print(f"prompts:{messages}")
    try:
        openai.api_key = const.OPEN_AI_API_KEY
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS
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
