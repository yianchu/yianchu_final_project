import US_state
from matplotlib.path import Path
import pandas as pd


def race_rank(state, category):
    df = pd.read_csv('race_amount.csv')
    if state in US_state.us_state_abbrev.values():
        state = [k for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    df = df.rename(columns={'State': 'location'})
    key = ['location']
    if category != 'Total':
        category = category+'Total'
    key.append(category)
    new_df = df[key].sort_values(by=category, ignore_index=True)
    data = new_df.values[new_df['location'] == state]
    value = new_df.index[new_df['location'] == state]
    rank = value.tolist()
    return rank[0]+1, data


def positive_rank(state, date):
    df = pd.read_csv(
        'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2021.csv')
    if state in US_state.us_state_abbrev.values():
        state = [k for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    df = df.rename(columns={'state': 'location'})
    df = df.loc[df['date'] == date]
    df = df.groupby('location')['cases'].sum()
    df = pd.DataFrame({'location': df.index, 'cases': df.values})
    data = df.values[df['location'] == state]
    new_df = df.sort_values(by='cases', ignore_index=True)
    value = new_df.index[new_df['location'] == state]
    rank = value.tolist()
    return rank[0]+1, data


def vaccine_rank(state, date):
    df = pd.read_csv(
        "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv")
    key = ['date', 'location', 'people_vaccinated']
    df = df[key]
    if state in US_state.us_state_abbrev.values():
        state = [k for k, v in US_state.us_state_abbrev.items() if v == state]
        state = state[0]
    df = df.loc[df['date'] == date]
    data = df.values[df['location'] == state]
    if data:
        new_df = df.sort_values(by='people_vaccinated', ignore_index=True)
        value = new_df.index[new_df['location'] == state]
        rank = value.tolist()
        return rank[0]+1, data
    else:
        return None, None
