from DB.sql_requests import SqlRequests
from dialogs.states.state import St
from dialogs.states.st_get_phone import GetPhone
from dialogs.service.cash import Cash, MyMessage
from dialogs.service.markup import create_keyboard


class Start(St):
    def process(self, dialog, user):
        dialog.execute_db(SqlRequests.save_user_start.value.format(*user))
        dialog.set_state(GetPhone())
        dialog.send_message(self.genetate_messengers(user))

    def genetate_messengers(self, user):
        return (MyMessage(user.tg_id, Cash.START_START, None)._asdict(),
                MyMessage(user.tg_id, Cash.CLIENT_NAME,
                          create_keyboard((user.tg_name, f"{user.tg_name} {user.tg_second_name}"), (1, 1)))._asdict())

        # return ({"chat_id": user.tg_id, "text": Cash.START_START},
        #         {"chat_id": user.tg_id, "text": Cash.CLIENT_NAME,
        #          "reply_markup": Markup().create_keyboard(
        #             (user.tg_name, f"{user.tg_name} {user.tg_second_name}"), (1, 1))})
