from enum import Enum


class SqlRequests(Enum):
    user_in_db = "SELECT * FROM Person WHERE (tg_user_name='{}' OR tg_user_id='{}' OR tg_chat_id='{}')"
    user_id = "SELECT id FROM Person WHERE tg_user_name='{}' OR tg_user_id='{}' OR tg_chat_id='{}'"
    add_new_user = "INSERT INTO Person (tg_user_name, first_name, second_name, tg_user_id, tg_chat_id, tg_date_appeal) " \
                   "Values ('{}', '{}', '{}', '{}', '{}', '{}')"

