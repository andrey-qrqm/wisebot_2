import random_event

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return ' Shut the fuck up!'
    if p_message == 'help':
        return ' Im not gonna help you motherfucker! '
    if p_message == 'антон':
        return 'все я спать нахуй'
    if p_message == 'макс':
        return 'любитель отчимов'
    if p_message == 'event':
        return 'WiseBot хочет чтобы ты ' + random_event.event()
    if p_message == 'андрей':
        return 'ебал в рот гит и все такое далее'
    if p_message == 'сева':
        return 'возьмёт 1v5 но всё равно проебет нашора'
    if p_message == 'аким':
        return 'душнит так что хуй залупа муравей в ахуе'

#print(handle_response('event'))
