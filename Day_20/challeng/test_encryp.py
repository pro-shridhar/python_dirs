import pytest
from encryption import encrypt


@pytest.mark.parametrize(
    "word, expected",
    [
        ("karaca", "0c0r0kaca"),
        ("burak", "k0r3baca"),
        ("banana", "0n0n0baca"),
        ("alpaca", "0c0pl0aca"),
        ("hello", "2ll1haca"),
    ],
)
def test_encrypt(word, expected):
    assert encrypt(word) == expected
