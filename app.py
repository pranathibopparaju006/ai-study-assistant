
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant")
st.caption("Your personal AI-powered learning companion")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = ""

with st.sidebar:
    st.header("⚙️ Study Settings")
    mode = st.selectbox(
        "Choose a tool",
        ["Summarize Notes", "Generate Quiz", "Explain Concepts"]
    )
    st.info("Paste your study material in the main panel.")

text = st.text_area(
    "📖 Enter your notes or study topic",
    height=260,
    placeholder="Paste your notes here or enter a topic..."
)

if st.button("✨ Generate with AI", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter notes or a topic first.")
    elif not API_KEY:
        st.error("Gemini API key missing. Check .streamlit/secrets.toml.")
    else:
        if mode == "Summarize Notes":
            instruction = "Summarize these notes with headings, key points, and a short conclusion."
        elif mode == "Generate Quiz":
            instruction = "Create 10 multiple-choice questions from this material. Include four options and the correct answer with a brief explanation."
        else:
            instruction = "Explain the concepts in simple language with examples and a short recap."

        with st.spinner("AI is preparing your study material..."):
            try:
                response = requests.post(
                    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
                    headers={
                        "x-goog-api-key": API_KEY,
                        "Content-Type": "application/json"
                    },
                    json={
                        "contents": [{
                            "parts": [{
                                "text": instruction + "\n\nStudy material:\n" + text
                            }]
                        }]
                    },
                    timeout=60
                )

                if response.ok:
                    data = response.json()
                    result = data["candidates"][0]["content"]["parts"][0]["text"]
                    st.subheader("🎯 Your Study Result")
                    st.markdown(result)
                    st.download_button(
                        "⬇️ Download result",
                        data=result,
                        file_name="study_result.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Gemini API error ({response.status_code}): {response.text[:500]}")

            except requests.RequestException as error:
                st.error(f"Connection error: {error}")
            except (KeyError, IndexError, ValueError):
                st.error("Unexpected AI response. Please try again.")

st.divider()
st.caption("AI Study Assistant | Verify important facts with trusted learning resources.")
