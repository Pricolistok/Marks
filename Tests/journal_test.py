
from Controller.journal.get_token_from_curl import get_data_from_curl

bash_curl = """
curl 'https://dnevnik.mos.ru/reports/api/progress/json?academic_year_id=9&student_profile_id=224645' \
  -H 'authority: dnevnik.mos.ru' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'auth-token: test_token' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'cookie: nothing_here' \
  -H 'profile-id: 1234' \
  -H 'profile-type: student' \
  -H 'referer: https://dnevnik.mos.ru/diary/diary/marks' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
  --compressed
"""

cmd_curl = """
curl "https://dnevnik.mos.ru/reports/api/progress/json?academic_year_id=9&student_profile_id=224645" ^
  -H "authority: dnevnik.mos.ru" ^
  -H "accept: application/json, text/plain, */*" ^
  -H "accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7" ^
  -H "auth-token: test_token" ^
  -H "content-type: application/json;charset=UTF-8" ^
  -H "cookie: nothing_here " ^
  -H "profile-id: 1234" ^
  -H "profile-type: student" ^
  -H "referer: https://dnevnik.mos.ru/diary/diary/marks" ^
  -H "sec-ch-ua: ^\^" Not A;Brand^\^";v=^\^"99^\^", ^\^"Chromium^\^";v=^\^"102^\^", ^\^"Google Chrome^\^";v=^\^"102^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  -H "sec-fetch-dest: empty" ^
  -H "sec-fetch-mode: cors" ^
  -H "sec-fetch-site: same-origin" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36" ^
  --compressed
"""


def test_bash_curl():
    assert get_data_from_curl(bash_curl) == ("test_token", 1234)


def test_cmd_curl():
    assert get_data_from_curl(cmd_curl) == ("test_token", 1234)


def test_empty_curl():
    assert get_data_from_curl("") == ("", 0)
