

def get_average(numbers: list[int]) -> float:
    if len(numbers) >= 1:
        return round(sum(numbers) / len(numbers), 2)
    return 0.0


def get_averages(subjects: dict) -> dict:
    new_subjects = {}

    for subject in subjects:
        new_subjects[subject] = get_average(subjects[subject])

    return new_subjects


