from flask import Flask, render_template, request
from data.tables import *
import data.db_session as db_session
from data.data_getter import *
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
db_session.global_init("data/base.sqlite")

session = db_session.create_session()

emergency_state = session.query(Statuses).filter(Statuses.id == 3).first()
emergency = emergency_state.status


def ask_sensors():
    air_sensors = temperature_and_humidity_sensors()
    soil_sensors = hum_sensors()
    for sens in air_sensors:
        session.add(sens)
    for sens in soil_sensors:
        session.add(sens)
    session.commit()


sched = BackgroundScheduler(daemon=True)
sched.add_job(ask_sensors, 'interval', seconds=10)
sched.start()


@app.route('/', methods=['GET', 'POST'])
def menu_page():
    global emergency
    global emergency_state
    if request.method == 'POST':
        emergency = not emergency
        emergency_state.status = emergency
    return render_template('index.html')


@app.route('/air/', methods=['GET', 'POST'])
def air_page():
    global emergency
    global emergency_state
    t_value = session.query(Setttings).filter(Setttings.id == 1).first()
    h_value = session.query(Setttings).filter(Setttings.id == 2).first()

    win_state = session.query(Statuses).filter(Statuses.id == 1).first()
    windows_state = win_state.status
    hum_state = session.query(Statuses).filter(Statuses.id == 2).first()
    humidity_state = hum_state.status


    air_sensors = session.query(Temp_hum_sens).order_by(Temp_hum_sens.id.desc()).limit(40)

    st_air_temp = (air_sensors[0].temp + air_sensors[1].temp + air_sensors[2].temp + air_sensors[3].temp) / 4
    st_air_hum = (air_sensors[0].hum + air_sensors[1].hum + air_sensors[2].hum + air_sensors[3].hum) / 4
    if request.method == 'POST':
        if request.form.get('win') is not None:
            windows_state = not windows_state
            window_pane_control(1 if windows_state else 0)
            win_state.status = windows_state
        if request.form.get('hum') is not None:
            humidity_state = not humidity_state
            control_of_the_humidification_system(1 if humidity_state else 0)
            hum_state.status = humidity_state
        if request.form.get('emergency') is not None:
            emergency = not emergency
            emergency_state.status = emergency
        session.commit()

    return render_template('a_sensors.html', windows_state=windows_state, humidity_state=humidity_state,
                           th_sns=air_sensors, temp1=list(map(lambda x: x.temp, air_sensors))[3::4],
                           temp2=list(map(lambda x: x.temp, air_sensors))[2::4],
                           temp3=list(map(lambda x: x.temp, air_sensors))[1::4],
                           temp4=list(map(lambda x: x.temp, air_sensors))[0::4],
                           hum1=list(map(lambda x: x.hum, air_sensors))[3::4],
                           hum2=list(map(lambda x: x.hum, air_sensors))[2::4],
                           hum3=list(map(lambda x: x.hum, air_sensors))[1::4],
                           hum4=list(map(lambda x: x.hum, air_sensors))[0::4],
                           st_air_temp=st_air_temp, st_air_hum=st_air_hum,
                           t_value=t_value, h_value=h_value, emergency=emergency)


@app.route('/soil/', methods=['GET', 'POST'])
def soil_page():
    global emergency
    global emergency_state
    hb_value = session.query(Setttings).filter(Setttings.id == 3).first()
    water_states = []
    bd_water_states = []
    for i in range(1, 7):
        water_bed = session.query(Statuses).filter(Statuses.id == 2 + i).first()
        water_states.append(water_bed.status)
        bd_water_states.append(water_bed)

    soil_sensors = session.query(Hum_ground_sens).order_by(Hum_ground_sens.id.desc()).limit(60)
    if request.method == 'POST':
        if request.form.get('emergency') is not None:
            emergency = not emergency
            emergency_state.status = emergency
        for i in range(6):
            if request.form.get(f'water{i + 1}') is not None:
                water_states[i] = not water_states[i]
                management_of_watering_beds((1 if water_states[i] else 0), i + 1)
                bd_water_states[i].status = water_states[i]
        session.commit()

    return render_template('s_sensors.html', water_states=water_states,
                           hum_sns=soil_sensors, hb_value=hb_value,
                           hum1=list(map(lambda x: x.hum, soil_sensors))[5::6],
                           hum2=list(map(lambda x: x.hum, soil_sensors))[4::6],
                           hum3=list(map(lambda x: x.hum, soil_sensors))[3::6],
                           hum4=list(map(lambda x: x.hum, soil_sensors))[2::6],
                           hum5=list(map(lambda x: x.hum, soil_sensors))[1::6],
                           hum6=list(map(lambda x: x.hum, soil_sensors))[0::6],
                           emergency=emergency)


@app.route('/statistics/', methods=['GET', 'POST'])
def statistics_page():
    global emergency
    global emergency_state

    air_sensors = session.query(Temp_hum_sens).order_by(Temp_hum_sens.id.desc()).limit(40)
    soil_sensors = session.query(Hum_ground_sens).order_by(Hum_ground_sens.id.desc()).limit(60)
    temp1 = list(map(lambda x: x.temp, air_sensors))[3::4]
    temp2 = list(map(lambda x: x.temp, air_sensors))[2::4]
    temp3 = list(map(lambda x: x.temp, air_sensors))[1::4]
    temp4 = list(map(lambda x: x.temp, air_sensors))[0::4]
    hum_air1 = list(map(lambda x: x.hum, air_sensors))[3::4]
    hum_air2 = list(map(lambda x: x.hum, air_sensors))[2::4]
    hum_air3 = list(map(lambda x: x.hum, air_sensors))[1::4]
    hum_air4 = list(map(lambda x: x.hum, air_sensors))[0::4]
    hum_soil1 = list(map(lambda x: x.hum, soil_sensors))[5::6]
    hum_soil2 = list(map(lambda x: x.hum, soil_sensors))[4::6]
    hum_soil3 = list(map(lambda x: x.hum, soil_sensors))[3::6]
    hum_soil4 = list(map(lambda x: x.hum, soil_sensors))[2::6]
    hum_soil5 = list(map(lambda x: x.hum, soil_sensors))[1::6]
    hum_soil6 = list(map(lambda x: x.hum, soil_sensors))[0::6]
    st_air_temp = []
    st_air_hum = []
    st_soil_hum = []
    for i in range(10):
        a = (temp1[i] + temp2[i] + temp3[i] + temp4[i]) / 4
        st_air_temp.append(a)
    for i in range(10):
        a = (hum_air1[i] + hum_air2[i] + hum_air3[i] + hum_air4[i]) / 4
        st_air_hum.append(a)
    for i in range(10):
        a = (hum_soil1[i] + hum_soil2[i] + hum_soil3[i] + hum_soil4[i] + hum_soil5[i] + hum_soil6[i]) / 6
        st_soil_hum.append(a)

    if request.method == 'POST':
        emergency = not emergency
        emergency_state.status = emergency

    return render_template('statistics.html', st_air_temp=st_air_temp, st_air_hum=st_air_hum, st_soil_hum=st_soil_hum,
                           emergency=emergency)


@app.route('/settings/', methods=['GET', 'POST'])
def settings_page():
    global emergency
    global emergency_state

    t_value = session.query(Setttings).filter(Setttings.id == 1).first()
    t_value_ask = t_value.value
    h_value = session.query(Setttings).filter(Setttings.id == 2).first()
    h_value_ask = h_value.value
    hb_value = session.query(Setttings).filter(Setttings.id == 3).first()
    hb_value_ask = hb_value.value

    if request.method == 'POST':
        if request.form.get('emergency') is not None:
            emergency = not emergency
            emergency_state.status = emergency
        t_value_ask = request.form.get('t_value')
        t_value.value = t_value_ask
        h_value_ask = request.form.get('h_value')
        h_value.value = h_value_ask
        hb_value_ask = request.form.get('hb_value')
        hb_value.value = hb_value_ask
        session.commit()

    return render_template('settings.html', t_value=t_value_ask, h_value=h_value_ask, hb_value=hb_value_ask,
                           emergency=emergency)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

