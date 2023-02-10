from flask import Flask, render_template
from data.tables import *
from data.data_getter import *
import requests
app = Flask(__name__)

@app.route('/air/', methods=['GET', 'POST'])
def index():
    return render_template('a_sensors.html', widows_state=True, humidity_state=True,
                           do=temperature_and_humidity_sensors(), da=[[10, 27], [15, 12], [14, 25], [18, 19]])



@app.route('/soil/', methods=['GET', 'POST'])
def index1():
    return render_template('s_sensors.html', s_humidity_state=[False, True, False, False, False, True],
                           do=air_temperature(), da=[[10, 27], [15, 12], [14, 25], [18, 19]])


@app.route('/settings/', methods=['GET', 'POST'])
def index2():
    return render_template('settings.html', t_value='15', h_value='12%', hb_value='20%')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)