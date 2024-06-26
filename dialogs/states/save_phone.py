from dialogs.states.standard_start import StandardStart
from dialogs.states.state import St
from DB.sql_requests import SqlRequests


class SavePhoneSt(St):
    def process(self, dialog, user):
        dialog.send_message(self.genetate_messengers_for_StandardStart(user))
        dialog.set_state(StandardStart())
        dialog.execute_db(SqlRequests.save_phone.value.format(user["phone"], user["id"]), "insert")
