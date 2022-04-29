import US_state
from matplotlib.path import Path
import pandas as pd


def state_num(state):
    race = pd.read_csv('race_amount.csv')
    if state in US_state.us_state_abbrev.values():
        state = [k for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    race = race.rename(columns={'State': 'location'})
    key = ['location', 'Total']
    race = race[key]
    data = race.values[race['location'] == state]
    return data[0][1]


def find_per(data, percent):
    difference = 10000
    length = int(len(data)/2)
    date = data[0][0]
    difference = length
    while difference > 2:
        difference = int(difference/2)
        if data[length][1] > percent:
            length = length - difference
            date = data[length][0]
        else:
            length = length + difference
            date = data[length][0]
    return date, data[length][1]


def positive_per(state, percent):
    df = pd.read_csv(
        'United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')
    if state in US_state.us_state_abbrev.keys():
        state = [v for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    df = df.rename(columns={'state': 'location'})
    key = ['submission_date', 'location', 'tot_cases']
    df = df[key]

    df['submission_date'] = pd.to_datetime(df['submission_date'])
    df = df.sort_values(by='submission_date')

    state_totalnum = state_num(state)

    data = df.values[df['location'] == state]
    date_case = []
    for line in data:
        date_case.append([line[0], line[2]/state_totalnum])
    date, per = find_per(date_case, percent)
    return date, per


def vaccine_per(state, percent):
    df = pd.read_csv(
        "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv")
    key = ['date', 'location', 'total_vaccinations']
    df = df[key]
    if state in US_state.us_state_abbrev.values():
        state = [k for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    data = df.values[df['location'] == state]
    state_totalnum = state_num(state)
    date_case = []
    for line in data:
        if (line[2] - state_totalnum) > 0:
            date_case.append([line[0], 1])
        else:
            date_case.append([line[0], line[2]/state_totalnum])
    date, per = find_per(date_case, percent)
    return date, per

