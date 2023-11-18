import random_event


def handle_response(message, author) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return " Shut your mouth motherfucker"
    if p_message == 'help':
        full = "Антон наконец меня заебал, \nevent - рандомный ивент на игру. \nevent роль - ивент на конкретную роль.\nроль - рандомная роль. \n!clear[n] - удалить последние n сообщений, по дефолту удаляется 20\nимена - список кого может обосрать бoт"
        return full
    if p_message == 'антон':
        return 'негр и пидорас но хороший человек'
    if p_message == 'анур':
        return 'резиновая уточка этого сервера'
    if p_message == 'женя':
        return 'багеты, негры, лягушки, фетиши севы - это все к ней'
    if p_message == 'макс':
        return 'любитель 40 отчимов'
    if p_message[:5] == 'event':
        if len(p_message)>5:
            arg_role = p_message[6:]
        else:
            arg_role = ""
        if arg_role:
            return 'WiseBot хочет чтобы '+ author + ' ' + random_event.event(arg_role)
        else:
            return 'Роль не указана, WiseBot хочет чтобы ' + author + ' ' + random_event.event(arg_role)
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
    if p_message == 'имена':
        return "антон, анур, женя, андрей, сева, макс, аким"

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


