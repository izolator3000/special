from dialogs.states.state import St
from dialogs.states.st_get_phone import GetPhone
from dialogs.service.cash import Cash


class Start(St):
    def process(self, user):
        pass

    def genetate_messengers(self, user):
        messages = []
        chat_id = user.user_data["tg_id"]
        text = Cash().dialog["start_start"]
        messages.append({"chat_id": chat_id, "text": text})

        text = Cash().dialog["client_name"]
        # fs_name = self.db_con.get_fs_name(tg_id=self.message.from_user.id)[0]
        # markup = Markup().create_keyboard((fs_name[0], " ".join(fs_name)), (1, 1))
        messages.append({"chat_id": chat_id, "text": text})
        return messages
