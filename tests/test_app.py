from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"
STUDY_MODES = [
    "Summarize Notes",
    "Generate Quiz",
    "Explain Concepts",
]


def _run_app():
    return AppTest.from_file(str(APP_PATH), default_timeout=10).run()


def test_app_renders_all_three_study_modes():
    app = _run_app()

    assert not app.exception
    assert app.title[0].value == "📚 AI Study Assistant"
    assert list(app.selectbox[0].options) == STUDY_MODES


def test_generate_button_warns_when_notes_are_blank():
    app = _run_app()
    app.button[0].click().run()

    assert not app.exception
    assert any(
        "enter notes or a topic first" in item.value.lower()
        for item in app.warning
    )


def test_nonempty_notes_explain_missing_api_key():
    app = _run_app()
    app.text_area[0].set_value(
        "Photosynthesis converts light energy into chemical energy."
    )
    app.button[0].click().run()

    assert not app.exception
    assert any(
        "gemini api key missing" in item.value.lower()
        for item in app.error
    )
