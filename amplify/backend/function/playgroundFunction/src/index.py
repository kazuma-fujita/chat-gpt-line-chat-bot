import json
import tiktoken


def handler(event, context):

    print('received event:')

    print(event)
    # text = 'Hello World'
    text = 'ヘローワールド'
    model_name = 'gpt-4'

    num_tokens = num_tokens_from_string(text, model_name)
    messages = [{'role': 'system', 'content': 'Please stop using polite language. Talk to me in a friendly way like a friend. Also, use a lot of emojis when you talk.'}]
    completed_text = 'Hello World'
    join_message = completed_text + ' ' + ' '.join(map(lambda message: message['content'], messages))
    print('join_string: ' + join_message)
    stringLength = len(join_message)
    num_tokens = num_tokens_from_string(text, model_name)
    print(f"String length:{stringLength}")

    print(f"num_tokens: {num_tokens}")

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from your new Amplify Python lambda!')
    }


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

