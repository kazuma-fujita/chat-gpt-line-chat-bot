import json
from decimal import Decimal
import const
import openai

openai.api_key = const.OPEN_AI_API_KEY


SLOT_DUMMY = {
    "question_slot": {
        "shape": "Scalar",
        "value": {
            "originalValue": "ダミー",
            "resolvedValues": [
                "ダミー"
            ],
            "interpretedValue": "ダミー"
        }
    }
}


def decimal_to_int(obj):
    if isinstance(obj, Decimal):
        return int(obj)


def elicit_slot(slot_to_elicit, intent_name, slots):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitSlot',
                'slotToElicit': slot_to_elicit,
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': 'InProgress'
            }
        }
    }


def confirm_intent(message_content, intent_name, slots):
    return {
        'messages': [{'contentType': 'PlainText', 'content': message_content}],
        'sessionState': {
            'dialogAction': {
                'type': 'ConfirmIntent',
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': 'Fulfilled'
            }
        }
    }


def close(fulfillment_state, message_content, intent_name, slots):
    return {
        'messages': [{'contentType': 'PlainText', 'content': message_content}],
        "sessionState": {
            'dialogAction': {
                'type': 'Close',
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': fulfillment_state
            }
        }
    }


def get_openai_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input_text},
        ]
    )
    print("Received response:" + json.dumps(response,default=decimal_to_int, ensure_ascii=False))
    return response["choices"][0]["message"]["content"].replace('\n', '')


def ChatGPT_intent(event):
    print("Received event:" + json.dumps(event, default=decimal_to_int, ensure_ascii=False))
    intent_name = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    input_text = event['inputTranscript']

    if slots['question_slot'] is None:
        return elicit_slot('question_slot', intent_name, SLOT_DUMMY)

    confirmation_status = event['sessionState']['intent']['confirmationState']

    if confirmation_status == "Confirmed":
        return close("Fulfilled", 'それでは、電話を切ります', intent_name, slots)

    elif confirmation_status == "Denied":
        return close("Fulfilled", 'お力になれず、申し訳ありません。電話を切ります', intent_name, slots)

    # confirmation_status == "None"
    response_text = get_openai_response(input_text)
    print("Received response_text:" + response_text)

    return confirm_intent(
        f'それでは、回答します。{response_text}。以上が回答になります。回答に納得したかたは、はい、とお伝え下さい。納得いかない場合、いいえ、とお伝え下さい',
        intent_name, slots)


def lambda_handler(event, context):
    print("Received event:" + json.dumps(event, default=decimal_to_int, ensure_ascii=False))

    intent_name = event['sessionState']['intent']['name']

    if intent_name == 'chatgpt':
        return ChatGPT_intent(event)