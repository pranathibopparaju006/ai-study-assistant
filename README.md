# 🧠 AI Study Assistant

A Streamlit web app that uses Google's Gemini AI to help students study smarter. Paste any text — lecture notes, articles, textbook excerpts — and instantly get a summary, quiz questions, or simplified concept explanations.

Built as part of the **SITER Academy Summer Internship 2026** Git assignment.

## Features

- **📝 Summarize** — condenses long text into clear bullet points
- **❓ Quiz Generator** — creates 5 multiple-choice questions from your text
- **💡 Concept Explainer** — breaks down key concepts in simple language with analogies

## Tech Stack

- **Python 3.14**
- **Streamlit** — web app framework
- **Gemini API** (Google Generative Language API) — accessed via REST (`requests` library) for compatibility with restricted environments
- **Git & GitHub** — version control

## Running Locally

```bash
git clone https://github.com/pranathibopparaju006/ai-study-assistant.git
cd ai-study-assistant
python -m pip install streamlit requests
python -m streamlit run app.py
```

You'll need a free Gemini API key from [aistudio.google.com](https://aistudio.google.com) — paste it into the sidebar once the app is running.

## Project Background

This project was built to fulfill a Git version control assignment, demonstrating:
- Repository initialization and structuring
- Staged, incremental commits
- Remote repository setup and pushing to GitHub
- Real-world debugging (environment restrictions, dependency conflicts, API integration)

## Author

Pranathi Bopparaju
Summer Intern, SITER Academy Norge — 2026
