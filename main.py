from env import Env
from algorithm import DP
import numpy as np

if __name__ == '__main__':
    env = Env(np.array([3, 1]))
    learner = DP(env, 0.9, 1e-4)
    learner.run()
    print(learner.values)
    print(learner.env.policy)