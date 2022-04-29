from main import *
from rank import *
from percent import *

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index', methods=["post"])
def index():
    data_form = request.form['data_form']
    if data_form == 'map':
        return render_template('map.html')
    elif data_form == 'rank':  # rank
        return render_template('state_date.html')
    else:
        return render_template('percent.html')


@app.route('/handle_form', methods=['POST'])
def handle_form():
    data_type = request.form['data_type']
    if data_type == 'race':
        return redirect(url_for('race'))
    else:
        v_c_map(data_type)
        return render_template('home.html')


@app.route('/race', methods=['GET', 'POST'])
def race():
    if request.method == 'POST':
        race_category = request.form['race_category']
        race_map(race_category)
        return render_template('home.html')
    else:
        return render_template('race.html')


@app.route('/state_date', methods=['POST'])
def state_date():
    data_type = request.form['data_type']
    state = request.form['state_name']
    if data_type == 'race':
        return redirect(url_for("race_r"))
    elif data_type == 'positive_case':
        date = request.form['date']
        r, v = positive_rank(state, date)
        if r == None:
            return 'There is no data in this condition. Please return to the last page.'
        else:
            return render_template('show_rank.html', type=data_type, rank=r, value=v[0][1], state=state, date=date)

    else:
        date = request.form['date']
        r, v = vaccine_rank(state, date)
        if r == None:
            return 'There is no data in this condition. Please return to the last page.'
        else:
            return render_template('show_rank.html', type=data_type, rank=r, value=v[0][2], state=state, date=date)


@app.route('/race_r', methods=['GET', 'POST'])
def race_r():
    if request.method == 'POST':
        race_category = request.form['race_category']
        state = request.form['state_name']
        r, v = race_rank(state, race_category)
        if r == None:
            return 'There is no data in this condition. Please return to the last page.'
        else:
            return render_template('race_show_rank.html', rank=r, value=v[0][1], state=state, category=race_category)
    else:
        return render_template('race_rank.html')


@app.route('/percent', methods=['POST'])
def percent():
    data_type = request.form['data_type']
    state_name = request.form['state_name']
    percent_amount = request.form['percent_amount']
    if data_type == 'positive_case':
        date, per = positive_per(state_name, float(percent_amount))
    else:
        date, per = vaccine_per(state_name, float(percent_amount))
    return render_template('show_percent.html', data_type=data_type, state_name=state_name, percent_lim=percent_amount, date=date, per=per)


if __name__ == "__main__":
    app.run(debug=True)
