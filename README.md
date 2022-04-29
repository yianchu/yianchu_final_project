# yianchu_final_project
SI 507 Final Project, Winter 2022, UMich.


## Package
Install the requirement packages by pip
- Flask
- pandas
- plotly

## General info
This project allows users to see the status of the race amount, vaccination, and covid-19 cases on the U.S. map on a date, 2021-12-31. In addition, users can also enter the date and the state to find the rank and the amount of vaccination and covid-19 cases among all states. 




### Data Sources
1. Get the data about the vaccination in all state on different date.
(https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv)
2. Get the data about the covid-19 cases in all state on different date.
(https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2021.csv)
3. Get the data about the race amount in all state today.
(https://worldpopulationreview.com/states/states-by-race)

### Data Structure
1. Map and Rank: use dataframe to sort the data and get the information.
2. Percent: use Binary Search to find the information.


### Interaction / Presentation
- Built the home page.
  - user will return the home to the home page after the search finish.
- Use the dictionary of U.S. states' full name and abbreviated name.
  - no matter whether the user enters the state's full name or abbreviated name, they can get the answer.
- Plot the U.S map about the user's choose (race, positive case, vaccination).
- Rank the amount about the user's choose (race, positive case, vaccination).

### Demo link
https://youtu.be/4YctnFHTmkU


