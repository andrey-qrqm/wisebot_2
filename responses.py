import random_event

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return ' Shut the fuck up!'
    if p_message == 'help':
        return ' Im not gonna help you motherfucker! '
    if p_message == 'антон':
        return 'негр и пидорас'
    if p_message == 'макс':
        return 'любитель отчимов'
    if p_message == 'event':
        return 'WiseBot хочет чтобы ты ' + random_event.event()

#print(handle_response('event'))