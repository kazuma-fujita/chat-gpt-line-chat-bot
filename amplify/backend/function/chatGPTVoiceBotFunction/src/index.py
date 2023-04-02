import message_repository


INTENT_NAME = 'ChatGPT'

SLOT_NAME = 'empty_slot'

SLOT_DUMMY = {
    SLOT_NAME: {
        'shape': 'Scalar',
        'value': {
            'originalValue': 'dummy',
            'resolvedValues': ['dummy'],
            'interpretedValue': 'dummy'
        }
    }
}


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
        'sessionState': {
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


def chatGPT_intent(event):
    intent_name = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    input_text = event['inputTranscript']
    session_id = event['sessionId']

    if slots[SLOT_NAME] is None:
        return elicit_slot(SLOT_NAME, intent_name, SLOT_DUMMY)

    elif input_text == '終了':
        return close('Fulfilled', 'ご利用ありがとうございました。またのご利用お待ちしております。', intent_name, slots)

    completed_text = message_repository.create_completed_text(session_id, input_text)
    print(f'Received input_text:{input_text}')
    print(f'Received completed_text:{completed_text}')

    return confirm_intent(completed_text, intent_name, slots)


def handler(event, context):
    intent_name = event['sessionState']['intent']['name']

    if intent_name == INTENT_NAME:
        return chatGPT_intent(event)
