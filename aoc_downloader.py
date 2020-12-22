"""
Downloads input for Advent of Code.
"""

import argparse
from pathlib import Path
import logging
import requests


# Constant declarations
VERSION = '1.0'
YEAR_FROM = 2015
YEAR_TO = 2020
URL_STUB = 'https://adventofcode.com'

# Update this with a valid session cookie before running
SESSION_COOKIE = '---'

if __name__ == '__main__':

    # check if session cookie is set, otherwise abort
    if SESSION_COOKIE == '---':
        raise ValueError('SESSION COOKIE NOT SET!!!!')

    parser = argparse.ArgumentParser()
    parser.add_argument('year', help='year to download')
    parser.add_argument('day', help='day to download')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    parser.add_argument('-o', '--offline', help='prepare for offline use by downloading AoC HTML page for the day',
                        action='store_true')
    args = parser.parse_args()

    # check if --verbose was set
    if args.verbose:
        # set logging level to INFO
        logging.basicConfig(level=logging.INFO)
    else:
        # standard is ERRORS only
        logging.basicConfig(level=logging.ERROR)

    year = int(args.year)
    day = int(args.day)

    # do some sense checking on the year and day
    if year < YEAR_FROM or year > YEAR_TO:
        raise ValueError(f'Year {year} is not valid. Year must be {YEAR_FROM} <= year <= {YEAR_TO}.')
    if day < 1 or day > 25:
        raise ValueError(f'Day {day} is not valid. Day must be 01 <= day <= 25.')

    # print a little message saying what we are going to do
    print(f'Advent of Code downloader, v{VERSION}.')
    print(f'(c) 2020, Bjoern Winkler')
    print(f'-- Downloading AoC {year}, day {day} --')

    # check if a directory for the day exists
    p = Path('.') / f'{day:02}'
    if not p.exists():
        logging.info(f'Directory {p} does not exist, creating it.')
        p.mkdir()

    # check if a stub file named aoc{year}_{day}.py exists
    # if not, create an empty file
    stub_file = p / f'aoc{year}_{day:02}.py'
    if not stub_file.exists():
        logging.info(f'Stub file {stub_file} does not exist, creating it')
        stub_file.touch()

    # prepare session cookie etc
    cookies = {'session': SESSION_COOKIE}

    # now get the HTML page if --offline option is set
    if args.offline:
        url_offline = f'{URL_STUB}/{year}/day/{day}'
        response = requests.get(url_offline, cookies=cookies)
        website = response.content

        offline_file = p / f'{year}_{day:02}_1.html'
        with open(offline_file, 'wb') as f:
            f.write(website)

        logging.info(f'Saving part 1 of {year}/{day} for offline use as {offline_file}.')

    # Get the input file
    url_input = f'{URL_STUB}/{year}/day/{day}/input'
    response = requests.get(url_input, cookies=cookies)
    input_content = response.content

    input_file = p / 'input.txt'
    with open(input_file, 'wb') as f:
        f.write(input_content)

    logging.info(f'Saving input for {year}/{day} as {input_file}.')
