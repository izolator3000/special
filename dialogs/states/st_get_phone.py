from DB.sql_requests import SqlRequests
from dialogs.service.cash import MyMessage, Cash
from dialogs.service.markup import request_phone
from dialogs.states.save_phone import SavePhoneSt
from dialogs.states.standard_start import StandardStart
from dialogs.states.state import St


class GetPhone(St):
    def process(self, dialog, user):
        self.save_tg_appeal_name(dialog, user)
        phone = self.we_have_phone(dialog, user)
        if phone != [(None,)]:
            dialog.send_message(self.genetate_messengers_for_StandardStart(user))
            dialog.set_state(StandardStart())
        else:
            dialog.send_message(self.genetate_messenger_for_phone(user))
            dialog.set_state(SavePhoneSt())

    def genetate_messenger_for_phone(self, user):
        return MyMessage(user["tg_chat_id"], Cash.PHONE, request_phone())._asdict(),

    def save_tg_appeal_name(self, dialog, user):
        dialog.execute_db(SqlRequests.save_appeal_name.value.format(user["tg_msg_text"], user["id"]), "insert")

    def we_have_phone(self, dialog, user):
        return dialog.execute_db(SqlRequests.we_have_phone.value.format(user["id"]))
