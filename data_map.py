import pandas as pd
import US_state
import plotly.graph_objects as go

state_df = pd.read_csv("race_amount.csv")  # data


def data_get(state_df, feature):
    state_df['location'] = state_df['location'].map(US_state.us_state_abbrev)
    state_df.dropna(subset=['location'], inplace=True)
    state_df.reset_index(drop=True, inplace=True)
    state_df.reset_index(inplace=True)

    for loc in US_state.us_state_abbrev.values():
        loc_ser = state_df.loc[state_df['location'] == loc].iloc[0]
        index = loc_ser['index']
        state_df.loc[index] = loc_ser.fillna(0)

    state_df.fillna(method="ffill", inplace=True)
    state_df.fillna(0, inplace=True)
    draw_map(state_df, feature)


def draw_map(state_df, feature):
    fig = go.Figure(data=go.Choropleth(
        locations=state_df['location'],
        z=state_df[feature].astype(int),
        locationmode='USA-states',
        colorscale="Blues",
        colorbar_title=f"{feature}",
        text=f"{feature}:" +
        state_df[feature].astype(int).apply('{:,}'.format)
    ))

    fig.update_layout(
        geo_scope='usa',
        title={'text': f"{feature} in the United States", 'x': 0.5,
               'xanchor': 'center', 'font': {'size': 16}}
    )

    fig.show()


# state_df.dropna(subset=['location'], inplace=True)
# state_df.reset_index(drop=True, inplace=True)
# state_df.reset_index(inplace=True)

# for loc in US_state.us_state_abbrev.values():
#     loc_ser = state_df.loc[state_df['location'] == loc].iloc[0]
#     index = loc_ser['index']
#     state_df.loc[index] = loc_ser.fillna(0)

# state_df.fillna(method="ffill", inplace=True)
# state_df.fillna(0, inplace=True)

# key = ['date', 'location', 'total_vaccinations',
#        'people_vaccinated', 'people_fully_vaccinated']
# state_df = state_df[key]


# today = 2020

# race_amount = {}
# with open('race_amount.csv', newline='') as f:
#     race_data = csv.reader(f)
#     race_data = list(race_data)
#     race_keys = race_data[0]
#     for row in race_data[1:]:
#         race_amount[row[0]] = row[1:]

# print(state_df['location'])
# print(race_amount)
