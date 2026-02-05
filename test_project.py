import os
import pytest
from project import verify_met, calculate_calories, save_log

NAMES_TEST = ["caminhada", "corrida", "musculação"]
def test_verify_met():
    assert verify_met(1, NAMES_TEST) == 2.0
    assert verify_met(3, NAMES_TEST) == 6.0
    assert verify_met(0, NAMES_TEST) is None
    assert verify_met(8, NAMES_TEST) is None


def test_function_2():
    ...


def test_function_n():
    ...