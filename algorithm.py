import numpy as np


class DP:
    def __init__(self, env, gamma, thresh):
        self.env = env
        self.actions = [0, 1, 2, 3]

        self.gamma = gamma
        self.thresh = thresh

        self.values = np.random.random((5, 6))
        self.values[np.isnan(self.env.grid)] = np.nan
        self.values[1, 4] = 0
        self.values[2, 4] = 0

    def run(self):
        while True:
            max_change = 0
            for s in self.env.states_indices:
                old_vs = self.values[s[0], s[1]]

                #  v[s] only has policy if not a terminal state
                new_v = float('-inf')

                for a in self.actions:
                    self.env.set_state(s.copy())
                    r = self.env.move(a)
                    v = r + self.gamma * self.values[self.env.state[0], self.env.state[1]]
                    if v > new_v:
                        new_v = v

                self.values[s[0], s[1]] = new_v
                max_change = max(max_change, np.abs(old_vs - self.values[s[0], s[1]]))
                # print(max_change, )

            if max_change < self.thresh:
                break

        for s in self.env.states_indices:
            best_act = None
            best_value = float('-inf')
            for a in self.actions:
                self.env.set_state(s.copy())
                r = self.env.move(a)
                v = r + self.gamma * self.values[self.env.state[0], self.env.state[1]]
                if v > best_value:
                    best_value = v
                    best_act = a
            self.env.policy[s[0], s[1]] = best_act
