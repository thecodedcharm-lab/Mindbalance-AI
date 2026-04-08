import random

class RandomAgent:
    def __init__(self, action_size):
        self.action_size = action_size

    def act(self, state):
        return random.randint(0, self.action_size - 1)
