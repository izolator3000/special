from enum import Enum
from collections import namedtuple


class TgDataAddress(Enum):
    # название переменной = адрес в json от ТГ
    tg_id = "message.chat.id"
    tg_name = "message.from_user.first_name"
    tg_second_name = "message.from_user.last_name"
    tg_user_name = "message.from_user.username"
    # tg_calling_persone = "message.text"
    tg_date_appeal = "int(message.date.utcnow().timestamp())"

User = namedtuple("User", "tg_id tg_name tg_second_name tg_user_name tg_date_appeal")

# class User(Enum):
#     tg_id = auto()
#     tg_name = auto()
#     tg_second_name = auto()
#     tg_user_name = auto()

