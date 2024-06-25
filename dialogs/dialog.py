from dialogs.states.st_start import Start


class Dialog:
    def __init__(self, main, db_con):
        self.main = main
        self.db_con = db_con
        self.state = Start()

    def message_arrived(self, user):
        self.state.process(self, user)

    def set_state(self, state):
        self.state = state

    def execute_db(self, sql_command):
        return self.db_con.execute(sql_command)

    def send_message(self, messages):
        self.main.send_message(messages)
