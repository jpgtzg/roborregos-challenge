from lib.states.state import State
import logging

class System:
    def __init__(self, name) -> None:
        self.name = name
        self.states = []
        self.current_state = None
        pass

    def add_state(self, *state: State):
        self.states.append(*state)

    def start(self):
        pass

    def update(self):     
        pass

    def set_state(self, new_state: State):
        if new_state is None:
            return
        
        if new_state in self.states:
            self.current_state = new_state
            logging.info(f'System {self.name} state set to {new_state}')
        else:
            logging.error(f"Error: State {new_state} is not in the states list.")

