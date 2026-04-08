import gradio as gr
import random
from env.emotion_env import EmotionEnv


# 🌿 Custom CSS (NOW ACTUALLY USED)
custom_css = """
body {
    background: linear-gradient(135deg, #d4f8d4, #e8ffe8);
}

.gradio-container {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    border-radius: 20px;
}

h1 {
    text-align: center;
    color: #2e7d32;
    font-family: 'Poppins', sans-serif;
}

button {
    background-color: #66bb6a !important;
    color: white !important;
    border-radius: 12px !important;
}

textarea {
    border-radius: 10px !important;
}
"""


# 🤖 SIMPLE AGENT (since “smart_agent” vanished into thin air)
def smart_agent(env):
    return random.randint(0, env.action_space.n - 1)


def run_simulation(level):
    env = EmotionEnv(level=level)
    state = env.reset()

    steps = 0
    total_reward = 0

    for _ in range(50):
        action = smart_agent(env)
        state, reward, done, info = env.step(action)

        total_reward += reward
        steps += 1

        if done:
            break

    # Fake derived emotional metrics (since your env doesn't track them yet)
    mood = state[0]
    energy = state[1]
    stress = state[2]

    burnout_risk = stress * (1 - energy)

    return f"""
🌿 Result: Simulation Complete

💚 Mood: {mood:.2f}  
⚡ Energy: {energy:.2f}  
🔥 Stress: {stress:.2f}  

🧠 Burnout Risk: {burnout_risk:.2f}

⭐ Total Reward: {total_reward:.2f}  
⏱ Steps: {steps}
"""


# 🌿 Theme
theme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="emerald",
    neutral_hue="slate"
)


with gr.Blocks(theme=theme, css=custom_css) as demo:

    gr.Markdown("""
    # 🧠🌿 MindBalance AI
    
    **AI simulation for balancing productivity and mental health**
    """)

    gr.Markdown("""
    Select difficulty and see how the AI manages stress, mood, energy and workload.
    """)

    level = gr.Dropdown(
        ["easy", "medium", "hard"],
        value="medium",
        label="🌱 Difficulty Level"
    )

    btn = gr.Button("✨ Run Simulation")

    output = gr.Textbox(
        label="🌿 Simulation Result",
        lines=10
    )

    btn.click(fn=run_simulation, inputs=level, outputs=output)


if __name__ == "__main__":
    demo.launch()
