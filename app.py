import random
import time

import requests
import streamlit as st

from assistant_utils import build_instruction, extract_generated_text


st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("📚 AI Study Assistant")
st.caption("Your personal AI-powered learning companion")

try:
    API_KEY = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    API_KEY = ""

MODEL_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash:generateContent"
)

with st.sidebar:
    st.header("⚙️ Study Settings")
    mode = st.selectbox(
        "Choose a tool",
        ["Summarize Notes", "Generate Quiz", "Explain Concepts"],
    )
    st.info("Paste your study material in the main panel.")

study_text = st.text_area(
    "📖 Enter your notes or study topic",
    height=260,
    placeholder="Paste your notes here or enter a topic...",
)

if st.button("✨ Generate with AI", type="primary", use_container_width=True):
    if not study_text.strip():
        st.warning("Please enter notes or a topic first.")
    elif not API_KEY:
        st.error(
            "Gemini API key missing. "
            "Configure GEMINI_API_KEY in Streamlit Secrets."
        )
    else:
        try:
            instruction = build_instruction(mode)
        except ValueError:
            st.error("Please choose a supported study mode.")
        else:
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": (
                                    f"{instruction}\n\n"
                                    f"Study material:\n{study_text}"
                                )
                            }
                        ]
                    }
                ]
            }
            headers = {"x-goog-api-key": API_KEY}

            with st.spinner("AI is preparing your study material..."):
                response = None
                try:
                    for attempt in range(4):
                        response = requests.post(
                            MODEL_URL,
                            headers=headers,
                            json=payload,
                            timeout=60,
                        )

                        retryable = response.status_code in (
                            429, 500, 502, 503, 504
                        )
                        if not retryable or attempt == 3:
                            break

                        wait_time = (2 ** (attempt + 1)) + random.uniform(0, 1)
                        time.sleep(wait_time)

                    if response is None:
                        st.error("No response received from Gemini. Please try again.")
                    elif response.ok:
                        result = extract_generated_text(response.json())
                        st.subheader("🎯 Your Study Result")
                        st.markdown(result)
                        st.download_button(
                            "⬇️ Download result",
                            data=result,
                            file_name="study_result.txt",
                            mime="text/plain",
                        )
                    elif response.status_code in (429, 500, 502, 503, 504):
                        st.error(
                            "Gemini is temporarily busy or unavailable. "
                            "Please wait a little and try again."
                        )
                    else:
                        st.error(
                            f"Gemini API error ({response.status_code}). "
                            "Check your API key and request, then try again."
                        )

                except requests.RequestException:
                    st.error(
                        "Could not connect to Gemini. "
                        "Please check your connection and try again."
                    )
                except (ValueError, TypeError):
                    st.error(
                        "Gemini returned an unexpected response. "
                        "Please try again."
                    )

st.divider()
st.caption(
    "AI Study Assistant | Verify important facts with "
    "trusted learning resources."
)
