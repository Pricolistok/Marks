import json
import os
from Controller.journal.get_marks import get_marks
from .test_marks_result import test_marks_result


def test_marks_get_command():
    token, user_id = os.getenv("test_token"), os.getenv("test_user_id")
    assert get_marks(token, user_id) == test_marks_result


def test_empty_get_command():
    token, user_id = "", 0
    assert get_marks(token, user_id) == []


def test_half_empty_get_command():
    token, user_id = os.getenv("test_token"), 0
    assert get_marks(token, user_id) == []


def test_half_empty_get_command2():
    token, user_id = "", os.getenv("test_user_id")
    assert get_marks(token, user_id) == []
