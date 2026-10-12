
# 📚 AI Study Assistant

An AI-powered learning companion that helps students understand study material through concise summaries, interactive quizzes, and simple explanations using Google's Gemini AI.

## ✨ Features

- 📝 **Smart Summarization** — Turn lengthy notes into structured summaries.
- 🧠 **Quiz Generation** — Generate multiple-choice questions from study material.
- 💡 **Concept Explanation** — Understand complex topics in simple language with examples.
- 📥 **Download Results** — Save generated study material as a text file.
- ⚡ **Interactive Interface** — A simple, responsive Streamlit application.

## 🛠️ Technology Stack

- **Language:** Python
- **Frontend:** Streamlit
- **AI Model:** Google Gemini API
- **HTTP Requests:** Requests
- **Version Control:** Git and GitHub

## 🏗️ Project Structure

```text
ai-study-assistant/
├── .streamlit/
│   └── secrets.toml       # Local API key configuration
├── app.py                 # Main application
├── .gitignore             # Protects local secrets
└── README.md              # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pranathibopparaju006/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Install dependencies

```bash
python -m pip install streamlit requests
```

### 3. Configure your Gemini API key

Create a file named `.streamlit/secrets.toml` and add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own key. Never commit this file or expose your API key publicly.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 📖 How to Use

1. Launch the application.
2. Select a study tool from the sidebar.
3. Enter your notes or study topic.
4. Click **Generate with AI**.
5. Review the generated content and download it if needed.

## 🎯 Use Cases

- Exam preparation and revision
- Summarizing lecture notes
- Practicing topic-based quizzes
- Learning difficult concepts
- Creating quick study guides

## 🔐 Security

- Store the Gemini API key in Streamlit secrets.
- Keep `.streamlit/secrets.toml` out of version control.
- Never share API keys in screenshots, public repositories, or documentation.
- Rotate the key if it is accidentally exposed.

## 🔮 Future Improvements

- PDF and document uploads
- Persistent study history
- Difficulty-based quizzes
- Flashcards and spaced repetition
- Progress tracking and personalized learning
- Deployment with Streamlit Community Cloud

## 👩‍💻 Author

**Pranathi Bopparaju**

GitHub: [@pranathibopparaju006](https://github.com/pranathibopparaju006)

---

Built to make learning more interactive and accessible with AI.
