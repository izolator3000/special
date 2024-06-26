from dialogs.states.state import St


class StandardStart(St):
    def process(self, dialog, user):
        print("Добрались до стандартного начала:-)")