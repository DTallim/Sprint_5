import randome
def generates_email(email_char_num):
    email=''.join(randome.choice(list('1234566789qwwerty'))for i in range(email_char_num))
    return f'{email}@yandex.ru'

def generates_password(psw_char_num):
    psw=''.join(random(list('123456789qwwertyQWERTY')) for x in range(psw_char_num))
    return psw