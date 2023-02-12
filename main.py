from flask import Flask, render_template, request
from data.tables import *
from data.data_getter import *
import requests
app = Flask(__name__)

@app.route('/air/', methods=['GET', 'POST', 'PATCH'])
def index():
    win = '0'
    hum = '0'
    swap = {'0': '1', '1': '0', None: '0'}
    if request.method == 'POST':
        win = request.form.get('win')
        hum = request.form.get('hum')
        win = swap[win]
        hum = swap[hum]
    if request.method == 'PATCH':
        window_pane_control(win)
        control_of_the_humidification_system(hum)

    return render_template('a_sensors.html', windows_state=win, humidity_state=hum,
                           do=temperature_and_humidity_sensors(), da=[[10, 27], [15, 12], [14, 25], [18, 19]])



@app.route('/soil/', methods=['GET', 'POST', 'PATCH'])
def index1():
    swap = {'0': '1', '1': '0', None: '0'}
    s1 = '0'
    s2 = '0'
    s3 = '0'
    s4 = '0'
    s5 = '0'
    s6 = '0'

    if request.method == 'POST':
        s1 = swap[request.form.get('s1')]
        s2 = swap[request.form.get('s2')]
        s3 = swap[request.form.get('s3')]
        s4 = swap[request.form.get('s4')]
        s5 = swap[request.form.get('s5')]
        s6 = swap[request.form.get('s6')]
    if request.method == 'PATCH':
        management_of_watering_beds(s1, 1)
        management_of_watering_beds(s2, 2)
        management_of_watering_beds(s3, 3)
        management_of_watering_beds(s4, 4)
        management_of_watering_beds(s5, 5)
        management_of_watering_beds(s6, 6)
    return render_template('s_sensors.html', s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6,
                           do=air_temperature(), da=[[10, 27], [15, 12], [14, 25], [18, 19]])


@app.route('/settings/', methods=['GET', 'POST', 'PATCH'])
def index2():
    t_value = 15
    h_value = 11
    hb_value = 80
    if request.method == 'POST':
        t_value = request.form.get('t_value')
        h_value = request.form.get('h_value')
        hb_value = request.form.get('hb_value')

    return render_template('settings.html', t_value=t_value, h_value=h_value, hb_value=hb_value)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

