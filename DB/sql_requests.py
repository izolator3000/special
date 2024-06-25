from enum import Enum

class SqlRequests(Enum):
    save_user_start = "INSERT INTO Persone (tg_id, name, second_name, tg_name, date_appeal) " \
                      "VALUES ('{}', '{}', '{}', '{}', '{}')"

    user_tg_id = "??"
    smth = "SELECT * From Persone"


