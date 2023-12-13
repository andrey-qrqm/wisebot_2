import random_event


def handle_response(message, author) -> str:
    p_message = message.lower()

    if p_message == 'help':
        full = "Антон наконец меня заебал, \n/event роль - ивент на конкретную роль.\n/role - рандомная роль. \n/clear amount - удалить последние n сообщений, по дефолту удаляется 20\n"
        return full
    if p_message[:5] == 'event':
        if len(p_message)>5:
            arg_role = p_message[6:]
        else:
            arg_role = ""
        if arg_role:
            return 'WiseBot хочет чтобы '+ author + ' ' + random_event.event(arg_role)
        else:
            return 'Роль не указана, WiseBot хочет чтобы ' + author + ' ' + random_event.event(arg_role)
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


