from flask import Flask, render_template, request
from data.tables import *

app = Flask(__name__)

@app.route('/air/', methods=['GET', 'POST'])
def index():
    return render_template('a_sensors.html', widows_state=True, humidity_state=True,
                           do=[[1, 1, 1, 25, 14, 17], [], [], [], []], da=[[10, 27], [15, 12], [14, 25], [18, 19]])



@app.route('/soil/', methods=['GET', 'POST'])
def index1():
    return render_template('s_sensors.html', s_humidity_state=[False, True, False, False, False, True],
                           do=[[1, 1, 1, 25, 14, 17], [], [], [], []], da=[[10, 27], [15, 12], [14, 25], [18, 19]])


@app.route('/settings/', methods=['GET', 'POST'])
def index2():
    return render_template('settings.html', t_value='15', h_value='12%', hb_value='20%')

