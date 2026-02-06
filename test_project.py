import os
import pytest
from project import verify_met, calculate_calories, save_log

NAMES_TEST = ["caminhada", "corrida", "musculação"]
def test_verify_met():
    assert verify_met(1, NAMES_TEST) == 2.0
    assert verify_met(3, NAMES_TEST) == 6.0
    assert verify_met(0, NAMES_TEST) is None
    assert verify_met(8, NAMES_TEST) is None


def test_calculate_calories():
    assert calculate_calories(2.0, 60, 30) == 60.0
    assert calculate_calories(10.0, 80, 30) == 400.0
    assert calculate_calories(5.0, 70, 0) == 0.0


def test_save_log():
    log_test = save_log("corrida", 300.0)
    assert os.path.exists("log.txt")
    assert "corrida" in log_test
    assert "300.0" in log_test