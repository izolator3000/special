from dialogs.service.cash import MyMessage, Cash
from dialogs.service.markup import create_keyboard


class St:
    def process(self, dialog, user):
        pass

    def genetate_messengers_for_StandardStart(self, user):
        return MyMessage(user["tg_chat_id"], Cash.STANDARD_START,
                         create_keyboard((Cash.STST_ORDER, Cash.STST_FIND_PRICE, Cash.STST_PAY), (3,)))._asdict(),
