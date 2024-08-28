def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not ((recipient[recipient.rfind("."):] in [".com", ".ru", ".net"] and recipient.rfind("@") != -1)
       and (sender[sender.rfind("."):] in [".com", ".ru", ".net"] and sender.rfind("@") != -1)):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif sender == recipient:
        return "Нельзя отправить письмо самому себе!"
    elif sender != "university.help@gmail.com":
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
                 sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
