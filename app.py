from main import *
from rank import *
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
    else:  # rank
        return render_template('state_date.html')


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
            return render_template('show.html', type=data_type, rank=r, value=v[0][1], state=state, date=date)

    else:
        date = request.form['date']
        r, v = vaccine_rank(state, date)
        if r == None:
            return 'There is no data in this condition. Please return to the last page.'
        else:
            return render_template('show.html', type=data_type, rank=r, value=v[0][1], state=state, date=date)


@app.route('/race_r', methods=['GET', 'POST'])
def race_r():
    if request.method == 'POST':
        race_category = request.form['race_category']
        state = request.form['state_name']
        r, v = race_rank(state, race_category)
        if r == None:
            return 'There is no data in this condition. Please return to the last page.'
        else:
            return render_template('race_show.html', rank=r, value=v[0][1], state=state, category=race_category)
    else:
        return render_template('race_rank.html')


if __name__ == "__main__":
    app.run(debug=True)
