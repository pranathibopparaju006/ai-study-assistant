import pytest

from assistant_utils import build_instruction, extract_generated_text


@pytest.mark.parametrize(
    "mode, expected",
    [
        ("Summarize Notes", "Summarize these notes"),
        ("Generate Quiz", "Create 10 multiple-choice questions"),
        ("Explain Concepts", "Explain the concepts in simple language"),
    ],
)
def test_build_instruction_for_supported_modes(mode, expected):
    assert build_instruction(mode).startswith(expected)


def test_build_instruction_rejects_unknown_mode():
    with pytest.raises(ValueError, match="Unsupported study mode"):
        build_instruction("Unknown mode")


def test_extract_generated_text_returns_joined_text():
    response = {
        "candidates": [
            {"content": {"parts": [{"text": "First part"}, {"text": "Second part"}]}}
        ]
    }
    assert extract_generated_text(response) == "First part\nSecond part"


@pytest.mark.parametrize("response", [{}, {"candidates": []}, {"candidates": [{"content": {"parts": []}}]}])
def test_extract_generated_text_rejects_missing_text(response):
    with pytest.raises(ValueError, match="did not contain generated text"):
        extract_generated_text(response)
