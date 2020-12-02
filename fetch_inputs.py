import datetime
import os
import sys
import requests

YEAR = 2020
TZ_OFFSET = -5

PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(PATH)
EST_TZ = datetime.timezone(datetime.timedelta(hours=TZ_OFFSET))
NOW_DATE = datetime.datetime.now(EST_TZ).date()

try:
    from cookie import AOC_COOKIE
except ImportError:
    print("Could not find token.")
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

date = datetime.datetime(YEAR, 12, 1).date()

for i in range(1, 26):
    if date > NOW_DATE:
        break
    date += datetime.timedelta(days=1)
    fname = f"inputs/{i}.txt"
    if os.path.isfile(fname):
        continue
    with open(fname, "w+") as f:
        url = f"https://adventofcode.com/{YEAR}/day/{i}/input"
        r = requests.get(url, cookies=dict(session=AOC_COOKIE))
        f.write(r.text)
        print(f"Got input for day {i}.")
