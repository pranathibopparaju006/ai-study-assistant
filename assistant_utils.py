"""Pure helper functions for the AI Study Assistant."""

from typing import Any, Mapping


INSTRUCTIONS = {
    "Summarize Notes": (
        "Summarize these notes with headings, key points, and a short conclusion."
    ),
    "Generate Quiz": (
        "Create 10 multiple-choice questions from this material. Include four "
        "options and the correct answer with a brief explanation."
    ),
    "Explain Concepts": (
        "Explain the concepts in simple language with examples and a short recap."
    ),
}


def build_instruction(mode: str) -> str:
    """Return the prompt instruction for a supported study mode."""
    try:
        return INSTRUCTIONS[mode]
    except KeyError as exc:
        raise ValueError(f"Unsupported study mode: {mode}") from exc


def extract_generated_text(data: Mapping[str, Any]) -> str:
    """Safely extract generated text from a Gemini generateContent response."""
    try:
        parts = data["candidates"][0]["content"]["parts"]
        result = "\n".join(
            part["text"] for part in parts if isinstance(part.get("text"), str)
        ).strip()
    except (KeyError, IndexError, TypeError, AttributeError) as exc:
        raise ValueError("Gemini response did not contain generated text") from exc

    if not result:
        raise ValueError("Gemini response did not contain generated text")
    return result
