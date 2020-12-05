import requests
import requests_cache
import numpy as np
from secrets import COOKIE
requests_cache.install_cache()
COOKIE = {'session': secrets.COOKIE}
URL = "https://adventofcode.com/{year}/day/{day}/input"

def input_raw(day, year=2020):
    # print (day, year)
    if len(str(day)) > 10:
        return str(day)
    return requests.get(URL.format(year=year, day=day), cookies=COOKIE).text
    
def input(day, year=2020):
    return input_raw(day, year).strip().split('\n')

def input_int(day, year=2020):
    return [int(x) for x in input(day, year)]

def input_grid(day, year=2020):
    data = input_raw(day, year).strip().split('\n')
    trees = np.array([list(x) for x in data])
    trees[trees=='.'] = 0
    trees[trees=='#'] = 1
    trees = np.array(trees, dtype=int)
    return trees
