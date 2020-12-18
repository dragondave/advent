import requests
import requests_cache
import numpy as np
import secrets
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

def input_grid(day, year=2020, symbols=None):
    if symbols is None:
        symbols = '.#'
    data = input_raw(day, year).strip().split('\n')
    trees = np.array([list(x) for x in data])
    for i, symbol in enumerate(symbols):
        trees[trees==symbol] = i
    trees = np.array(trees, dtype=int)
    return trees
