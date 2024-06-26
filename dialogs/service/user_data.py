from enum import Enum


class TgDataAddress(Enum):
    # название переменной = адрес в json в сообщении ТГ-а
    tg_user_name = "message.from_user.username"
    tg_msg_text = "message.text"
    first_name = "message.from_user.first_name"
    second_name = "message.from_user.last_name"
    tg_user_id = "message.from_user.id"
    tg_chat_id = "message.chat.id"
    tg_date_appeal = "int(message.date.utcnow().timestamp())"
    phone = "message.contact.phone_number"
