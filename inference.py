import os
from mindbalance_ai import EmotionEnv, smart_agent

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "mindbalance-agent")
HF_TOKEN = os.getenv("HF_TOKEN", "")


def run_task(level="medium"):

    env = EmotionEnv(level=level)
    state = env.reset()

    total_reward = 0.0
    step_count = 0
    max_steps = 50

    print("[START]")
    print("task: productivity_balance")
    print("model:", MODEL_NAME)

    while step_count < max_steps:

        action = smart_agent(env)

        state, reward, done, info = env.step(action)

        step_count += 1
        total_reward += reward

        print("[STEP]")
        print("step:", step_count)
        print("action:", action)
        print("reward:", round(reward, 4))
        print("state:", state)

        if done:
            break

    # Convert reward → normalized score
    score = total_reward / 20.0
    score = max(0.0, min(1.0, score))

    print("[END]")
    print("steps:", step_count)
    print("score:", round(score, 4))

    return score


if __name__ == "__main__":
    run_task()
