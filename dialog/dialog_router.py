from dialog.service.UserData import User
from dialog.dialog import Dialog


class DialogList:
    def __init__(self, main):
        self.main = main
        self.dialog_list = {}

    def message_arrived(self, message):
        user = User()   # Приняли данные и обработали в удобный вид
        user.save_data_from_tg(message)

        if user.user_data["tg_id"] not in self.dialog_list:
            self.dialog_list[user.user_data["tg_id"]] = (Dialog(self.main), user)

        self.dialog_list[user.user_data["tg_id"]][0].answer(user)