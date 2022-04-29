import US_state
import data_map
# from flask import Flask, render_template, request, redirect, url_for
import pandas as pd


def v_c_map(data_type):  # map
    if data_type == 'positive_case':
        df = pd.read_csv(
            'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2021.csv')
        df = df.rename(columns={'state': 'location'})
        df = df.loc[df['date'] == '2021-12-31']
        df = df.groupby('location')['cases'].sum()
        df = pd.DataFrame({'location': df.index, 'cases': df.values})
        df['location'] = df['location'].map(US_state.us_state_abbrev)
        data_map.draw_map(df, 'cases')

    elif data_type == 'vaccination':  # vaccine
        df = pd.read_csv(
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv")
        key = ['date', 'location', 'total_vaccinations',
               'people_vaccinated', 'people_fully_vaccinated']
        df = df[key]
        data_map.data_get(df, 'people_vaccinated')


def race_map(category):
    df = pd.read_csv('race_amount.csv')
    df = df.rename(columns={'State': 'location'})
    key = ['location']
    if category != 'Total':
        category = category+'Total'
    key.append(category)
    df['location'] = df['location'].map(US_state.us_state_abbrev)
    data_map.draw_map(df[key], category)
