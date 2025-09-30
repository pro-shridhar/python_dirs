import pytest

from encode import encode_morse


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "EDABBIT CHALLENGE",
            ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .",
        ),
        ("HELP ME !", ".... . .-.. .--.   -- .   -.-.--"),
        ("CHALLENGE", "-.-. .... .- .-.. .-.. . -. --. ."),
        (
            "1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL...",
            ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-",
        ),
        (
            "did you got my mail ?",
            "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..",
        ),
        (
            "TWO THInGS TO KNOW : i FORGeT THeM :C",
            "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.",
        ),
    ],
)
def test_encode_morse(text, expected):
    assert encode_morse(text) == expected
