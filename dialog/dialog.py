from dialog.states.st_start import Start


class Dialog:
    def __init__(self, main):
        self.main = main
        self.state = Start()

    def answer(self, user):
        instr = self.state.process(user)

        if not instr.state:
            self.set_state(instr.state)

        if not instr.pairs:
            self.save_in_db(instr.pairs)

        if instr.messages != 0:
            self.send_message(instr.messages)

    def set_state(self, state):
        self.state = state

    def save_in_db(self, pairs): pass

    def send_message(self, messages):
        print(messages)
        self.main.send_message(messages)
