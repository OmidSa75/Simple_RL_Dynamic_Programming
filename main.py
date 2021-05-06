from env import Env
from algorithm import DP
import numpy as np

if __name__ == '__main__':
    env = Env(np.array([3, 1]))
    learner = DP(env, 1, 1e-4)
    learner.run()
    print(learner.values[1:-1, 1:-1])
    print(learner.env.policy[1:-1, 1:-1])
