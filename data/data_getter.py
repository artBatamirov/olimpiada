import requests
import datetime as dt
from tables import *

def temperature_and_humidity_sensors():
    sensors = []
    cur_time = dt.datetime.now()
    for i in range(1, 5):
        link = f'https://dt.miet.ru/ppo_it/api/temp_hum/{i}'
        response = requests.get(link)
        resp = response.json()
        sens = Temp_hum_sens()
        sens.device_id = resp['id']
        sens.hum = resp['humidity']
        sens.temp = resp['temperature']
        sens.time = cur_time
        sensors.append(sens)
    return sensors


def air_temperature():
    sensors = []
    cur_time = dt.datetime.now()
    for i in range(1, 7):
        link = f'https://dt.miet.ru/ppo_it/api/hum/{i}'
        response = requests.get(link)
        resp = response.json()
        sens = Hum_ground_sens()
        sens.device_id = resp['id']
        sens.hum = resp['humidity']
        sens.time = cur_time
        sensors.append(sens)
    return sensors


def window_pane_control(state):
    link = f'https://dt.miet.ru/ppo_it/api/fork_drive?state={state}'
    response = requests.patch(link)
    resp = response.json()
    sens = Statuses()
    sens.name = 'pane'
    sens.state = state
    return sens


def management_of_watering_beds(state, id):
    link = f'https://dt.miet.ru/ppo_it/api/watering?state={state}&id={id}'
    response = requests.patch(link)
    resp = response.json()
    sens = Setttings()
    sens.name = f'watering{id}'
    sens.state = state
    return sens

def control_of_the_humidification_system(state_value):
    link = f'https://dt.miet.ru/ppo_it/api/total_hum?state={state_value}'
    response = requests.patch(link)
    resp = response.json()
    sens = Setttings()
    sens.name = 'humidification'
    sens.state = state_value
    return sens
