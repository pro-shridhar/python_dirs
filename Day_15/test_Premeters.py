import pytest
import re


def is_palindrome(maybe_palindrome):

    maybe_palindrome = re.sub(r"[^a-zA-Z]", "", maybe_palindrome)
    maybe_palindrome = maybe_palindrome.lower()
    maybe_palindrome = maybe_palindrome.replace(" ", "")
    rstr = maybe_palindrome[::-1]

    print(maybe_palindrome, rstr)
    return maybe_palindrome == rstr


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result

    # print(is_palindrome("Do geese see God"))
