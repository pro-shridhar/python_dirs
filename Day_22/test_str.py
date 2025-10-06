import pytest
from new import censor_string


@pytest.mark.parametrize(
    "text, bad_words, censor, expected",
    [
        (
            "The cow jumped over the moon.",
            ["cow", "over"],
            "*",
            "The *** jumped **** the moon.",
        ),
        (
            "Why do my cats keep eating grass?",
            ["Why", "keep", "eating"],
            "!",
            "!!! do my cats !!!! !!!!!! grass?",
        ),
        (
            "How do I stop myself from using python!?",
            ["do", "stop", "using"],
            "-",
            "How -- I ---- myself from ----- python!?",
        ),
        (
            "If statements are pretty fun to use.",
            ["statements", "pretty", "to"],
            "~~",
            "If ~~~~~~~~~~~~~~~~~~~~ are ~~~~~~~~~~~~ fun ~~~~ use.",
        ),
        (
            "I'm dyslexic, but that deos'tn matter!",
            ["that", "matter!"],
            "?",
            "I'm dyslexic, but ???? deos'tn ???????",
        ),
        (
            "I should be doing work but I am doing this instead.",
            ["should", "but", "this"],
            "*",
            "I ****** be doing work *** I am doing **** instead.",
        ),
    ],
)
def test_censor_string(text, bad_words, censor, expected):
    assert censor_string(text, bad_words, censor) == expected
