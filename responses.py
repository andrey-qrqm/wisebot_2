import random_event
import responses

def handle_response(message, author) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return ' Shut the fuck up!'
    if p_message == 'help':
        return ' Im not gonna help you motherfucker! '
    if p_message == 'антон':
        return 'негр и пидорас но хороший человек'
    if p_message == 'макс':
        return 'любитель отчимов'
    if p_message == 'event':
        return 'WiseBot хочет чтобы '+ author + ' ' + random_event.event()
    if p_message == 'андрей':
        return 'ебал в рот гит и все такое далее'
    if p_message == 'сева':
        return 'возьмёт 1v5 но всё равно проебет нашора'
    if p_message == 'аким':
        return 'душнит так что хуй залупа муравей в ахуе'
    if p_message == 'автор':
        return get_nickname(author)


def get_nickname(author):
    i = author.index('(') + 1
    nickname = author[i:(len(author) - 1)]
    return nickname

