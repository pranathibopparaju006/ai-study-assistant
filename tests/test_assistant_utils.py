import pytest

from assistant_utils import build_instruction, extract_generated_text, validate_study_text


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

class FakeResponse:
    def __init__(self, status_code):
        self.status_code = status_code


def test_request_with_retries_retries_transient_errors_then_succeeds():
    from assistant_utils import request_with_retries

    responses = iter([FakeResponse(503), FakeResponse(429), FakeResponse(200)])
    calls = []
    waits = []

    def fake_post(url, **kwargs):
        calls.append((url, kwargs))
        return next(responses)

    result = request_with_retries(
        fake_post,
        "https://example.invalid/generate",
        headers={"x-goog-api-key": "test-key"},
        payload={"contents": []},
        sleep_fn=waits.append,
        jitter_fn=lambda low, high: 0,
    )

    assert result.status_code == 200
    assert len(calls) == 3
    assert waits == [2, 4]
    assert calls[0][1]["timeout"] == 60


def test_request_with_retries_does_not_retry_non_transient_error():
    from assistant_utils import request_with_retries

    calls = []
    result = request_with_retries(
        lambda url, **kwargs: calls.append(url) or FakeResponse(400),
        "https://example.invalid/generate",
        headers={},
        payload={},
        sleep_fn=lambda _: pytest.fail("should not sleep"),
    )

    assert result.status_code == 400
    assert calls == ["https://example.invalid/generate"]


def test_request_with_retries_stops_after_max_attempts():
    from assistant_utils import request_with_retries

    calls = []
    waits = []
    result = request_with_retries(
        lambda url, **kwargs: calls.append(url) or FakeResponse(503),
        "https://example.invalid/generate",
        headers={},
        payload={},
        max_attempts=3,
        sleep_fn=waits.append,
        jitter_fn=lambda low, high: 0,
    )

    assert result.status_code == 503
    assert len(calls) == 3
    assert waits == [2, 4]


def test_request_with_retries_requires_positive_attempt_count():
    from assistant_utils import request_with_retries

    with pytest.raises(ValueError, match="at least 1"):
        request_with_retries(
            lambda *_args, **_kwargs: FakeResponse(200),
            "https://example.invalid/generate",
            headers={},
            payload={},
            max_attempts=0,
        )


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_validate_study_text_rejects_blank_input(text):
    with pytest.raises(ValueError, match="enter notes or a topic"):
        validate_study_text(text)


def test_validate_study_text_trims_surrounding_whitespace():
    assert validate_study_text("  chapter notes  ") == "chapter notes"


def test_validate_study_text_rejects_oversized_input():
    with pytest.raises(ValueError, match="10 characters or fewer"):
        validate_study_text("x" * 11, max_chars=10)


def test_validate_study_text_rejects_non_text_input():
    with pytest.raises(ValueError, match="must be text"):
        validate_study_text(None)
