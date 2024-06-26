from DB.sql_requests import SqlRequests
from dialogs.states.save_phone import SavePhoneSt
from dialogs.states.standard_start import StandardStart
from dialogs.states.state import St
from dialogs.states.st_get_phone import GetPhone
from dialogs.service.cash import Cash, MyMessage
from dialogs.service.markup import create_keyboard, request_phone


class Start(St):
    def process(self, dialog, user):
        name, phone = self.we_have_appeal_name_and_phone(dialog, user)
        print(f"{name=}, {phone=}")
        if name != '':
            if phone != '':
                dialog.send_message(self.genetate_messengers_for_StandardStart(user))
                dialog.set_state(StandardStart())
            else:
                dialog.send_message(self.genetate_messengers_for_phone(user))
                dialog.set_state(SavePhoneSt())
        else:
            dialog.send_message(self.genetate_messengers_for_name(user))
            dialog.set_state(GetPhone())

    def we_have_appeal_name_and_phone(self, dialog, user):
        return dialog.execute_db(SqlRequests.appeal_name_and_phone.value.format(user["id"]))[0]

    def genetate_messengers_for_name(self, user):
        return (MyMessage(user["tg_chat_id"], Cash.START_START, None)._asdict(),
                MyMessage(user["tg_chat_id"], Cash.CLIENT_NAME,
                          create_keyboard((user["first_name"],
                                           f"{user['first_name']} {user['second_name']}"), (1, 1)))._asdict())

    def genetate_messengers_for_phone(self, user):
        return MyMessage(user["tg_chat_id"], Cash.PHONE, request_phone())._asdict(),
