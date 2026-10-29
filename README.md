# 📚 AI Study Assistant

An AI-powered learning companion that helps students understand study material through concise summaries, multiple-choice quizzes, and simple explanations using Google's Gemini AI.

🚀 **Live Demo:** [Try AI Study Assistant](https://ai-study-assistant-lbqoqvgdmvdcv2h4eg3bnbr.streamlit.app)

## ✨ Features

- 📝 **Smart Summarization** — Turn lengthy notes into structured summaries with headings and key points.
- 🧠 **Quiz Generation** — Generate 10 multiple-choice questions with options, answers, and explanations.
- 💡 **Concept Explanation** — Understand complex topics in simple language with examples and a recap.
- 📥 **Download Results** — Download generated study material as a text file.
- 🔄 **Error Handling** — Retry temporary Gemini API failures automatically.
- 🛡️ **Input Validation** — Reject blank notes and cap each request at 20,000 characters.
- ⚡ **Interactive Interface** — Use a simple Streamlit interface to select a study tool and enter study material.

## 🛠️ Technology Stack

- **Language:** Python
- **Frontend and UI:** Streamlit
- **AI Model:** Google Gemini API (`gemini-2.5-flash`)
- **HTTP Requests:** Requests
- **Version Control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## 🏗️ Project Structure

```text
ai-study-assistant/
├── .streamlit/
│   └── secrets.toml       # Local API key configuration (not committed)
├── app.py                 # Main Streamlit application
├── assistant_utils.py     # Validation, prompts, response parsing, retry helper
├── tests/                 # Mock-based unit tests
├── requirements.txt       # Runtime dependencies
├── requirements-dev.txt   # Test dependencies
├── .gitignore             # Excludes local secrets
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
python -m pip install -r requirements.txt
```

### 3. Configure your Gemini API key

Create a `.streamlit/secrets.toml` file in the project directory:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own Gemini API key. Never commit this file or expose your key publicly.

For Streamlit Community Cloud, configure `GEMINI_API_KEY` in your app's Secrets settings.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📖 How to Use

1. Open the application.
2. Select **Summarize Notes**, **Generate Quiz**, or **Explain Concepts** from the sidebar.
3. Enter your notes or study topic.
4. Click **Generate with AI**.
5. Review the generated content and download it if needed.

## Automated Checks

Install the development dependencies and run the unit tests:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m compileall -q app.py assistant_utils.py
```

GitHub Actions runs these checks on pushes and pull requests. The tests validate helper functions, response parsing, and retry behavior using mocked responses; they do not call the live Gemini API.

## 🎯 Use Cases

- Exam preparation and revision
- Summarizing lecture notes
- Practicing topic-based quizzes
- Understanding difficult concepts
- Creating quick study guides

## 🔐 Security

- Store the Gemini API key in Streamlit secrets.
- Keep `.streamlit/secrets.toml` out of version control.
- Never share API keys in screenshots, public repositories, or documentation.
- Rotate the key immediately if it is accidentally exposed.

## 🔮 Future Improvements

- PDF and document uploads
- Persistent study history
- Difficulty-based quizzes
- Flashcards and spaced repetition
- Progress tracking and personalized learning
- PDF and document uploads\n- Persistent study history\n- Difficulty-based quizzes\n- Flashcards and spaced repetition\n- Progress tracking and personalized learning\n- More UI and integration tests

## 👩‍💻 Author

**Pranathi Bopparaju**

GitHub: [@pranathibopparaju006](https://github.com/pranathibopparaju006)

---

*Built to make learning more interactive and accessible with AI.*


