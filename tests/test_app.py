from streamlit.testing.v1 import AppTest


def test_app_renders_all_three_study_modes():
    app = AppTest.from_file("app.py", default_timeout=10).run()

    assert not app.exception
    assert app.title[0].value == "📚 AI Study Assistant"
    assert list(app.selectbox[0].options) == [
        "Summarize Notes",
        "Generate Quiz",
        "Explain Concepts",
    ]


def test_generate_button_warns_when_notes_are_blank():
    app = AppTest.from_file("app.py", default_timeout=10).run()
    app.button[0].click().run()

    assert not app.exception
    assert any("enter notes or a topic first" in item.value.lower() for item in app.warning)
