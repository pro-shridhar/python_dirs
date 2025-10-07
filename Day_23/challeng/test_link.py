import pytest
from hyperlinks import tidy_link  # Replace with actual module name


@pytest.mark.parametrize(
    "url, text, title, expected",
    [
        (
            "https://edabit.com/challenges",
            "Challenges",
            "Go to the challenges!",
            '[Challenges](https://edabit.com/challenges "Go to the challenges!")',
        ),
        (
            "https://www.google.com",
            "Google",
            "Google Search",
            '[Google](https://www.google.com "Google Search")',
        ),
        (
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "Click Me!",
            None,
            "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
        ),
        (
            "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet",
            "Markdown Cheatsheet",
            None,
            "[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)",
        ),
        (
            "https://www.python.org/",
            "Python",
            "Visit the Python Website!",
            '[Python](https://www.python.org/ "Visit the Python Website!")',
        ),
        (
            "https://www.youtube.com/watch?v=O2yPnnDfqpw",
            "i just did a bad thing",
            None,
            "[i just did a bad thing](https://www.youtube.com/watch?v=O2yPnnDfqpw)",
        ),
        (
            "https://www.reddit.com/",
            "Reddit",
            "the front page of reddit",
            '[Reddit](https://www.reddit.com/ "the front page of reddit")',
        ),
    ],
)
def test_tidy_link(url, text, title, expected):
    result = tidy_link(url, text, title)  # Always pass 3 arguments
    assert result == expected
