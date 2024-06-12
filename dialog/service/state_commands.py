class Instruction:
    def __init__(self):
        self.state = 0
        self.pairs = 0
        self.messages = 0

    def set_state(self, state):
        self.state = state

    def save_in_db(self, pairs: list):
        self.pairs = pairs

    def send_message(self, messages: list):
        self.messages = messages
