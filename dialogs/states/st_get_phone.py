from dialogs.states.state import St


class GetPhone(St):
    def process(self, dialog, user):
        print("Добрались до GetPhone", user)
