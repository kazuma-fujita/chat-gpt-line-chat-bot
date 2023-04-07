import openai
import const

# Model name
GPT_MODEL = 'gpt-3.5-turbo'
# GPT_MODEL = 'gpt-4'

# Maximum number of tokens to generate
# MAX_TOKENS = 1024

# Create a new dict list of a system
SYSTEM_PROMPTS = [{'role': 'system', 'content': 'You are an excellent AI assistant. Please keep your answer within 250 characters.'}]


def completions(history_prompts):
    messages = SYSTEM_PROMPTS + history_prompts

    print(f"prompts:{messages}")
    try:
        openai.api_key = const.OPEN_AI_API_KEY
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            # max_tokens=MAX_TOKENS
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        # Raise the exception
        raise e
