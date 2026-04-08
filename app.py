import gradio as gr

# Custom CSS for aesthetic theme
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
import gradio as gr
from mindbalance_ai import EmotionEnv, smart_agent



def run_simulation(level):

    env = EmotionEnv(level=level)
    env.reset()

    steps = 0
    result = "Running..."

    for _ in range(50):
        action = smart_agent(env)
        obs, reward, done, info = env.step(action)
        steps += 1

        if done:
            result = info.get("reason", "Finished")
            break

    burnout_risk = env.stress * (1 - env.energy)

    return f"""
🌿 Result: {result}

💚 Mood: {env.mood:.2f}  
⚡ Energy: {env.energy:.2f}  
🔥 Stress: {env.stress:.2f}  

🧠 Burnout Risk: {burnout_risk:.2f}

📋 Tasks Left: {env.tasks_remaining}  
⏱ Steps: {steps}
"""


# 🌿 Custom calming theme
theme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="emerald",
    neutral_hue="slate"
)


with gr.Blocks(theme=theme) as demo:

    gr.Markdown(
        """
        # 🧠🌿 MindBalance AI
        
        **AI simulation for balancing productivity and mental health**
        """
    )

    gr.Markdown(
        """
        Select difficulty and see how the AI manages **stress, mood, energy and workload**.
        """
    )

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

    btn.click(run_simulation, inputs=level, outputs=output)


demo.launch()
