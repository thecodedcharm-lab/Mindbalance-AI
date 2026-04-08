from env.emotion_env import EmotionEnv

def get_tasks():
    return [
        {
            "name": "calm_user",
            "env": EmotionEnv(level="easy"),
            "goal": "increase calmness score"
        },
        {
            "name": "stabilize_mood",
            "env": EmotionEnv(level="medium"),
            "goal": "reduce volatility"
        }
    ]
