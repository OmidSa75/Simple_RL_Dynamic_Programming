import numpy as np


class Env:
    def __init__(self, start_point):
        self.state = start_point
        self.grid = np.full((5, 6), fill_value=np.nan)
        self.grid[1:-1, 1:-1] = 0
        self.grid[1, 4] = 1
        self.grid[2, 4] = 1
        self.grid[2, 2] = np.nan

        self.states = np.ones((5, 6))
        self.states[np.isnan(self.grid)] = 0

        self.states_indices = self.return_states_indices()

        self.rewards = np.full((5, 6), fill_value=-0.04)
        self.rewards[1, 4] = 1
        self.rewards[2, 4] = -1

        self.policy = np.full((5, 6), fill_value=np.nan)
        self.policy[1:-1, 1:-1] = np.random.randint(0, 3, (3, 4))
        self.policy[2, 2] = np.nan

        print(self.policy[1:-1, 1:-1])

    def set_state(self, state):
        self.state = state

    def is_terminal(self, state):
        if self.grid[state[0], state[1]] == 1:
            return True
        else:
            return False

    def move(self, action):

        if action == 0:  # up
            rand = np.random.rand()
            if rand <= 0.1 and self.states[self.state[0], self.state[1] - 1] == 1:  # turn left
                self.state[1] -= 1
            elif 0.1 < rand <= 0.2 and self.states[self.state[0], self.state[1] + 1] == 1:
                self.state[1] += 1
            elif 0.2 <= rand and self.states[self.state[0] - 1, self.state[1]] == 1:
                self.state[0] -= 1
        elif action == 1:  # down
            if self.states[self.state[0] + 1, self.state[1]] == 1:
                self.state[0] += 1
        elif action == 2:  # right
            if self.states[self.state[0], self.state[1] + 1] == 1:
                self.state[1] += 1
        elif action == 3:  # left
            if self.states[self.state[0], self.state[1] - 1] == 1:
                self.state[1] -= 1

        return self.rewards[self.state[0], self.state[1]]

    def return_states_indices(self):
        rows, columns = np.indices(self.grid.shape)
        indices = np.c_[rows.flatten(), columns.flatten()]
        indices = indices[self.grid.flatten() == 0]
        return indices


if __name__ == '__main__':
    game = Env([3, 1])
