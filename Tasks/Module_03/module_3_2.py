# Задача "Рассылка писем"


def is_standard_mail(address: str) -> bool:
    """
    Проверяем, что почта содержит знак "@" и заканчивается на .com"/".ru"/".net".
    :param address: адрес электронной почты.
    :return: True - почта содержит "@" и заканчивается на .com"/".ru"/".net".
             False - если нет.
    """
    return "@" in address and (address.endswith(".ru") or address.endswith(".com") or address.endswith(".net"))


def send_email(message: str, recipient: str, *, sender="university.help@gmail.com") -> None:
    """
    Выводит в терминал сообщения о успешности отправки писем.
    :param message: сообщение, которое хотим отправить.
    :param recipient: почта получателя сообщения.
    :param sender: почта отправителя сообщения. По умолчанию "university.help@gmail.com"
    :return:
    Выводит в терминал:
    1. "Невозможно отправить письмо с адреса {sender} на адрес {recipient}", если {sender} или {recipient}
    не содержат знак "@" и заканчиваются на .com"/".ru"/".net".
    2. "Нельзя отправить письмо самому себе!", если {sender} = {recipient}.
    3. "Письмо успешно отправлено с адреса {sender} на адрес {recipient}.", если {sender} = "university.help@gmail.com"
    4. "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.",
    если остальные проверки не пройдены
    """
    if not is_standard_mail(recipient) or not is_standard_mail(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


if __name__ == "__main__":
    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
