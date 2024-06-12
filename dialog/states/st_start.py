from dialog.service.state_commands import Instruction
from dialog.states.state import St
from dialog.states.st_get_phone import GetPhone
from dialog.service.cash import Cash
from dialog.service.markup import Markup


class Start(St):
    def process(self, user):
        instr = Instruction()

        instr.set_state(GetPhone())
        instr.save_in_db(user)

        messages = []
        chat_id = user.user_data["tg_id"]
        text = Cash().dialog["start_start"]
        messages.append({"chat_id": chat_id, "text": text})

        text = Cash().dialog["client_name"]
        # fs_name = self.db_con.get_fs_name(tg_id=self.message.from_user.id)[0]
        # markup = Markup().create_keyboard((fs_name[0], " ".join(fs_name)), (1, 1))
        messages.append({"chat_id": chat_id, "text": text})

        instr.send_message(messages)

        return instr