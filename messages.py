def create_start_message_new_user(username: str) -> str:
    greeting_msg = f"""
Привет, {username}!

Telegram-бот тортов на заказ. Принимает заказы на торты, собранные самим покупателем.

Если вам интересны наши услуги, пожалуйста, пройдите регистрацию.
Для этого согласитесь на обработку персональных данных.
"""
    return greeting_msg


def create_start_message_exist_user(username: str) -> str:
    """Текст стартового сообщения для существующего пользователя"""
    greeting_msg = f"""
Привет, {username}!

Bake Cake - telegram-бот тортов на заказ.
Выберите, куда хотите перейти.
"""
    return greeting_msg


def invalid_phone_number_message() -> str:
    """Текст в случае указания неправильного номера пользователем"""
    return """
Проверьте правильность введенённого телефона:
- номер должен начинаться на 7...
- должны быть только цифры
- длина 12 символов
Пример: 79998887766
"""
