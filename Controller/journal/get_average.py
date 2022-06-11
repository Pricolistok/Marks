

def get_average(numbers: list[int]) -> float:
    return round(sum(numbers) / len(numbers), 2)


def get_averages(subjects: dict) -> dict:
    new_subjects = {}

    for subject in subjects:
        new_subjects[subject] = get_average(subjects[subject])

    return new_subjects


