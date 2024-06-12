from enum import Enum


class UserData(Enum):
    tg_id = "message.chat.id"
    tg_name = "message.from_user.first_name"
    tg_second_name = "message.from_user.last_name"
    tg_user_name = "message.from_user.username"
    # tg_calling_persone = "message.text"
    # tg_date_appeal = "int(message.date.utcnow().timestamp())"


class User:
    def __init__(self):
        self.user_data = dict()

    def save_data_from_tg(self, message):
        for data in UserData:
            if data not in self.user_data.keys():
                self.user_data[data.name] = eval(data.value)
