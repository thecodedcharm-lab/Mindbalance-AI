from mindbalance_ai import EmotionEnv, smart_agent

def run(level="medium"):
    env = EmotionEnv(level=level)
    env.reset()

    for _ in range(60):
        action = smart_agent(env)
        obs, reward, done, _, info = env.step(action)
        if done:
            break

    return {
        "mood": round(env.mood, 2),
        "stress": round(env.stress, 2),
        "energy": round(env.energy, 2),
        "tasks_remaining": env.tasks_remaining,
        "result": info.get("reason", "In Progress")
    }

if __name__ == "__main__":
    print(run("medium"))
