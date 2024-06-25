from dialogs.states.st_start import Start


class Dialog:
    def __init__(self, main):
        self.main = main
        self.state = Start()

    def message_arrived(self, user): print(f"Dialog's user: {user}\nuser.tg_id: {user.tg_id}")

    def set_state(self, state):
        self.state = state

    def save_in_db(self, pairs): pass

    def send_message(self, messages):
        print(messages)
        self.main.send_message(messages)
