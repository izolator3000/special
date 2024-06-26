import sqlite3


class DBConnection:
    def __init__(self, db_file=r'C:\Users\Dima\PycharmProjects\special\DB\specialsql.db'):
        try:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"Не получилось соединиться с бд: {error}")

    def execute(self, sql_command, select_insert="select"):
        match select_insert:
            case "select":
                return self.cursor.execute(sql_command).fetchall()
            case "insert":
                self.cursor.execute(sql_command)
                return self.connection.commit()

    def close(self):
        self.connection.close()
