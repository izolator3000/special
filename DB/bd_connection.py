import sqlite3


class DBConnection:
    def __init__(self, db_file='specialsql.db'):
        try:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"Не получилось соединиться с бд: {error}")

    def save(self, user):

        "insert into persone (name, value) select 'web', '14' from dual where not exists(select 1 from sys where name = 'web')"
        result = self.select(f"select * from Persone where tg_id='{data['tg_id']}'")
        res = bool(len(result))
        if not res:
            text = f"INSERT INTO Persone (tg_id, name, second_name, tg_name, date_appeal) " \
                   f"VALUES ('{data['tg_id']}', '{data['first_name']}', '{data['last_name']}', '{data['user_name']}'," \
                   f" '{data['date']}');"
            self.insert(text)
        self.insert()




    def insert(self, sql_text: str):
        try:
            self.cursor.execute(sql_text)
        except Exception as error:
            print(error)

        try:
            self.connection.commit()
        except Exception as error:
            print(error)

    def update(self, sql_text: str): self.insert(sql_text)

    def select(self, sql_text: str):
        try:
            return self.cursor.execute(sql_text).fetchall()
        except Exception as error:
            print(error)
            return True


    def close(self):
        self.connection.close()
























#
#     def user_exists(self, tg_name):
#         """Проверяем, есть ли юзер в базе"""
#         result = self.cursor.execute("SELECT `tg_name` FROM `Persone` WHERE `tg_name` = ?", (tg_name,))
#         return bool(len(result.fetchall()))
#
#     def get_user_id(self, tg_name):
#         """Достаем tg_name юзера в базе по его tg_name"""
#         result = self.cursor.execute("SELECT `tg_name` FROM `Persone` WHERE `tg_name` = ?", (tg_name,))
#         return result.fetchone()[0]
#
#     def add_user(self, user_id):
#         """Добавляем юзера в базу"""
#         self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
#         return self.conn.commit()
#
#     def add_record(self, user_id, operation, value):
#         """Создаем запись о доходах/расходах"""
#         self.cursor.execute("INSERT INTO `records` (`users_id`, `operation`, `value`) VALUES (?, ?, ?)",
#             (self.get_user_id(user_id),
#             operation == "+",
#             value))
#         return self.conn.commit()
#
#     def get_records(self, user_id, within = "all"):
#         """Получаем историю о доходах/расходах"""
#
#         if within == "day":
#             result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
#                 (self.get_user_id(user_id),))
#         elif within == "week":
#             result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
#                 (self.get_user_id(user_id),))
#         elif within == "month":
#             result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
#                 (self.get_user_id(user_id),))
#         else:
#             result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? ORDER BY `date`",
#                 (self.get_user_id(user_id),))
#
#         return result.fetchall()
#
