import numpy as np

class Space:
    def __init__(self, n=None, shape=None):
        self.n = n
        self.shape = shape


class EmotionEnv:
    """
    OpenEnv-style environment
    """

    def __init__(self, level="medium"):
        self.level = level

        self.action_space = Space(n=3)  # 0=ignore,1=calm,2=engage
        self.observation_space = Space(shape=(3,))

        self.state = None
        self.steps = 0
        self.max_steps = 10

    def reset(self):
        self.state = np.random.rand(3)
        self.steps = 0
        return self.state

    def step(self, action):
        self.steps += 1

        # Fake emotional dynamics
        reward = self._compute_reward(action)

        self.state = np.clip(
            self.state + np.random.randn(3) * 0.1,
            0, 1
        )

        done = self.steps >= self.max_steps

        return self.state, reward, done, {}

    def _compute_reward(self, action):
        if action == 1:
            return 1  # calming works
        elif action == 2:
            return 0.5
        return -0.5
