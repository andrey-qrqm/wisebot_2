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
        return 'любитель 40 отчимов'
    if p_message == 'event':
        return 'WiseBot хочет чтобы '+ author + ' ' + random_event.event()
    if p_message == 'андрей':
        return 'ебал в рот гит и всех в мут нахуй'
    if p_message == 'сева':
        return 'хентай бойчик опять мисснул карой'
    if p_message == 'аким':
        return 'душнит так что хуй залупа муравей в ахуе'
    if p_message == 'автор':
        return get_nickname(author)
    if p_message == 'роль':
        return 'WiseBot хочет ' + get_nickname(author) + ' ' + random_event.random_role()


def get_nickname(author):
    try:
        if '(' in author:
            i = author.index('(') + 1
            nickname = author[i:(len(author) - 1)]
            return nickname
        else:
            return author
    except Exception as e:
        print(e)
        return author


