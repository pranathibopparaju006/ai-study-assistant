"""Pure helper functions for the AI Study Assistant."""

from typing import Any, Mapping


MAX_STUDY_TEXT_CHARS = 20000


def validate_study_text(text: str, max_chars: int = MAX_STUDY_TEXT_CHARS) -> str:
    """Trim and validate study material before sending it to the API."""
    if not isinstance(text, str):
        raise ValueError("Study material must be text")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Please enter notes or a topic first.")
    if isinstance(max_chars, bool) or not isinstance(max_chars, int) or max_chars < 1:
        raise ValueError("max_chars must be a positive integer")
    if len(cleaned) > max_chars:
        raise ValueError(f"Study material must be {max_chars} characters or fewer.")
    return cleaned


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

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def request_with_retries(
    post,
    url: str,
    *,
    headers: Mapping[str, str],
    payload: Mapping[str, Any],
    timeout: int = 60,
    max_attempts: int = 4,
    sleep_fn=None,
    jitter_fn=None,
):
    """Call a POST function, retrying only transient Gemini HTTP statuses.

    sleep_fn and jitter_fn are injectable so retry behavior can be tested
    without waiting or making network requests.
    """
    import random
    import time

    sleep = sleep_fn or time.sleep
    jitter = jitter_fn or random.uniform
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    response = None
    for attempt in range(max_attempts):
        response = post(url, headers=dict(headers), json=dict(payload), timeout=timeout)
        if response.status_code not in RETRYABLE_STATUS_CODES or attempt == max_attempts - 1:
            return response
        sleep((2 ** (attempt + 1)) + jitter(0, 1))
    return response
