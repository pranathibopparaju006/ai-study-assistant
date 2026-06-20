import streamlit as st
import requests
import json

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Study Assistant", page_icon="🧠", layout="centered")

# ── Styling ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .hero {
        background: linear-gradient(135deg, #1a1f2e 0%, #16213e 50%, #0f3460 100%);
        border: 1px solid #2d3748; border-radius: 16px;
        padding: 2.5rem 2rem; text-align: center; margin-bottom: 2rem;
    }
    .hero h1 { font-size: 2.2rem; font-weight: 700; color: #e2e8f0; margin: 0; }
    .hero p  { color: #94a3b8; font-size: 1rem; margin-top: 0.5rem; }
    .feature-row { display: flex; gap: 0.75rem; margin-bottom: 2rem; flex-wrap: wrap; }
    .feature-pill {
        background: #1e293b; border: 1px solid #334155; border-radius: 20px;
        padding: 0.4rem 1rem; color: #7dd3fc; font-size: 0.82rem; font-weight: 600;
    }
    .result-card {
        background: #1e293b; border: 1px solid #334155; border-radius: 12px;
        padding: 1.5rem; margin-top: 1rem; color: #e2e8f0; line-height: 1.7;
    }
    .result-title {
        font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
        color: #7dd3fc; text-transform: uppercase; margin-bottom: 0.75rem;
    }
    .stTextArea textarea {
        background: #1e293b !important; color: #e2e8f0 !important;
        border: 1px solid #334155 !important; border-radius: 10px !important;
    }
    .stTextInput input {
        background: #1e293b !important; color: #e2e8f0 !important;
        border: 1px solid #334155 !important; border-radius: 10px !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #6366f1) !important;
        color: white !important; border: none !important; border-radius: 10px !important;
        font-weight: 600 !important; width: 100% !important; font-size: 1rem !important;
    }
    label { color: #94a3b8 !important; font-size: 0.9rem !important; }
    .tip-box {
        background: #0f2027; border-left: 3px solid #3b82f6;
        border-radius: 0 8px 8px 0; padding: 0.75rem 1rem;
        color: #94a3b8; font-size: 0.85rem; margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🧠 AI Study Assistant</h1>
    <p>Paste any text — get instant summaries, quiz questions, and concept explanations.</p>
</div>
<div class="feature-row">
    <span class="feature-pill">📝 Summarize</span>
    <span class="feature-pill">❓ Quiz Generator</span>
    <span class="feature-pill">💡 Concept Explainer</span>
    <span class="feature-pill">⚡ Powered by Gemini AI</span>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Setup")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Paste your API key here")
    st.markdown("---")
    st.markdown("**How to get a free API key:**")
    st.markdown("1. Go to [aistudio.google.com](https://aistudio.google.com)")
    st.markdown("2. Sign in with Google")
    st.markdown("3. Click **Get API Key**")
    st.markdown("4. Paste it above")
    st.markdown("---")
    st.markdown("**Built for:** SITER Summer Internship 2026")

# ── Main UI ───────────────────────────────────────────────────────────────────
st.markdown('<div class="tip-box">💡 <b>Tip:</b> Works best with paragraphs from textbooks, articles, or lecture notes.</div>', unsafe_allow_html=True)

text_input = st.text_area(
    "📄 Paste your study text here", height=220,
    placeholder="Example: Git is a distributed version control system..."
)

mode = st.selectbox("🎯 What do you want to do?", [
    "📝 Summarize the text",
    "❓ Generate quiz questions",
    "💡 Explain key concepts simply"
])

PROMPTS = {
    "📝 Summarize the text": "Summarize the following text clearly using bullet points. Keep it under 150 words and be student-friendly.\n\nText:\n{text}",
    "❓ Generate quiz questions": "Generate 5 multiple-choice quiz questions from the text below.\nFormat:\nQ1. [Question]\na) b) c) d)\nAnswer: [correct]\n\nText:\n{text}",
    "💡 Explain key concepts simply": "Identify 3-5 key concepts from the text. Explain each simply like you're teaching a 15-year-old. Use analogies where helpful.\n\nText:\n{text}"
}

LABELS = {
    "📝 Summarize the text": "SUMMARY",
    "❓ Generate quiz questions": "QUIZ QUESTIONS",
    "💡 Explain key concepts simply": "KEY CONCEPTS"
}

# ── Generate ──────────────────────────────────────────────────────────────────
if st.button("✨ Generate"):
    if mode == "📝 Summarize the text":
        st.success("Demo Summary")
        st.write(text_input[:300])

    elif mode == "❓ Generate quiz questions":
        st.success("Demo Quiz")
        st.write("""
Q1. What is the main topic?

a) AI
b) Sports
c) Movies
d) Music

Answer: a
""")

    else:
        st.success("Demo Concepts")
        st.write("""
Concept 1: Artificial Intelligence
Concept 2: Text Processing
Concept 3: Learning Assistance
""")
        
# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#475569; font-size:0.8rem;'>AI Study Assistant · SITER Summer Internship 2026 · Built with Python & Streamlit</p>",
    unsafe_allow_html=True
)