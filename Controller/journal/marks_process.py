from Marks.Controller.journal.get_average import get_averages
from Marks.Controller.journal.get_marks import get_marks


def get_all_marks(marks: dict) -> dict:
    new_marks = {}

    for subject in marks:
        if subject['periods']:
            period = subject["periods"][-1]

            name = subject['subject_name']
            new_marks[name] = []

            for mark in period['marks']:
                for _ in range(mark['weight']):
                    new_marks[name].append(int(mark['values'][0]['five']))

            if not new_marks[name]:
                del new_marks[name]

    return new_marks

