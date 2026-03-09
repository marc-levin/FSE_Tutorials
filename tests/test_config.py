# Just check if the student has loaded the environment variables correctly
from helpers.config import Config


def test_currency_symbol():
    assert Config.get_currency_symbol() == "P"


def test_secret_key():
    assert Config.get_secret_key() == "supersecretkey"

# Comment in a python file