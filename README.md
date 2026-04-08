🧠 MindBalance AI

MindBalance AI is a reinforcement-learning simulation environment that models the balance between productivity and mental health.

The environment simulates how an agent manages workload, stress, and energy while attempting to complete tasks without burning out.

---

🚀 Features

- Emotional state tracking (mood, stress, energy)
- Task-based productivity simulation
- Burnout detection system
- Decision-making agent
- Interactive demo using Gradio

---

🧠 Environment Design

Observation Space

[mood, energy, stress, task_progress]

Action Space

0 – Rest
1 – Work on task
2 – Deep work
3 – Relax
4 – Mindfulness

Goal

Complete all tasks while maintaining healthy stress and energy levels.

---

🧪 How It Works

The agent must learn to balance:

- Completing tasks
- Managing stress
- Maintaining mood and energy

Too much stress leads to burnout, ending the episode.

---

🖥 Live Demo

Try the interactive demo here:

https://huggingface.co/spaces/thecodedcharm/mindbalance_ai

---

🛠 Tech Stack

- Python
- NumPy
- Gradio

---

📂 Project Structure

mindbalance_ai/
├── mindbalance_ai.py
├── inference.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md

---

🚀 Run Locally

pip install numpy gradio
python inference.py
