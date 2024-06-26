from DB.sql_requests import SqlRequests
from dialogs.dialog import Dialog
from DB.bd_connection import DBConnection


class DialogList:
    def __init__(self, main):
        self.main = main
        self.db_con = DBConnection()
        self.dialogs = {}

    def message_arrived(self, user):
        if not self.user_in_db(user):
            print(f"User не в бд: {user}")
            self.add_new_user_in_db(user)

        id = self.user_id(user)
        try:
            self.dialogs[id].message_arrived(user)
        except:
            dialog = Dialog(self.main, self.db_con)
            self.dialogs[id] = dialog
            dialog.message_arrived(user)
        """
        try:
            if self.user_in_db(user):
                self.dialogs[self.user_id(user)].message_arrived(user)
            else:
                self.add_new_user_in_db(user)
                dialog = Dialog(self.main, self.db_con)
                self.dialogs[self.user_id(user)] = dialog
                dialog.message_arrived(user)
        except Exception as e:
            print(f"Что-то пошло не так с добавлением нового пользователя: {e}")"""

    def user_in_db(self, user):
        return bool(len(self.db_con.execute(SqlRequests.user_in_db.value.format(user["tg_user_name"],
                                                                       user["tg_user_id"],
                                                                       user["tg_chat_id"]))))

    def add_new_user_in_db(self, user):
        self.db_con.execute(SqlRequests.add_new_user.value.format(user["tg_user_name"],
                                                                  user["first_name"],
                                                                  user["second_name"],
                                                                  user["tg_user_id"],
                                                                  user["tg_chat_id"],
                                                                  user["tg_date_appeal"]), "insert")

    def user_id(self, user):
        id = self.db_con.execute(SqlRequests.user_id.value.format(user["tg_user_name"],
                                                                    user["tg_user_id"],
                                                                    user["tg_chat_id"]))
        if not id:
            raise Exception(f"user_id не нашёл id для {user['tg_user_name']}")
        return id[0][0]


