from .test_marks_result import test_marks_result, test_processing_result
from Controller.journal.marks_process import get_all_marks


def test_process_marks():
    assert get_all_marks(test_marks_result) == test_processing_result


def test_empty_marks():
    assert get_all_marks({}) == {}
