class Env:
    def __init__(self, width, height, start_point):
        self.width = width
        self.height = height
        self.state = start_point

    def set(self, rewards, actions):
        self.rewards = rewards
        self.actions = actions

    def set_state(self, state):
        self.state = state

    def current_state(self):
        return self.state

    def is_terminal(self, state):
        return state not in self.actions

    def end(self):
        return self.state not in self.actions

    def move(self, action):
        if action in self.actions[self.state[0], self.state[1]]:
            if action == 0:  # up
                self.state[0] -= 1
            elif action == 1:  # down
                self.state[0] += 1
            elif action == 2:  # right
                self.state[1] += 1
            elif action == 3:  # left
                self.state[1] -= 1

        return self.rewards.get((self.state[0], self.state[1]), 0)

    def all_states(self):
        return set(list(self.actions.keys()) + list(self.rewards.keys()))


def make_env():
    env = Env(3, 4, (2, 0))
    rewards = {(0, 3): 1, (1,3): -1}
    actions = {
        (0, 0): ()
    }
