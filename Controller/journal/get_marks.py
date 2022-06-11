import requests

from constants import MARKS_LINK, ACADEMIC_YEAR


def get_marks(token: str, student_id) -> dict:
    params = {
        "student_profile_id": student_id,
        "academic_year_id": ACADEMIC_YEAR
    }
    headers = {
        "auth-token": token
    }
    response = requests.get(MARKS_LINK, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {}
