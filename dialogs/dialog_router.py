from dialogs.dialog import Dialog
from DB.bd_connection import DBConnection


class DialogList:
    def __init__(self, main):
        self.main = main
        self.db_con = DBConnection()
        self.dialogs = {}

    def message_arrived(self, user):
        try:
            self.dialogs[user.tg_id].message_arrived(user)
        except KeyError:
            dialog = Dialog(self.main, self.db_con)
            self.dialogs[user[0]] = dialog
            dialog.message_arrived(user)
