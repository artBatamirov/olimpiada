from data import db_session
from data.tables import *


def main():
    db_session.global_init("base.sqlite")

    session = db_session.create_session()
    win_state = Statuses()
    win_state.id = 1
    win_state.name = 'windows'
    win_state.status = False
    session.add(win_state)
    hum_state = Statuses()
    hum_state.id = 2
    hum_state.name = 'humidication'
    hum_state.status = False
    session.add(hum_state)
    for i in range(1, 7):
        water_bed = Statuses()
        water_bed.id = 2 + i
        water_bed.name = f'water_bed{i}'
        water_bed.status = False
        session.add(water_bed)

    t_value = Setttings()
    t_value.id = 1
    t_value.name = 't_value'
    t_value.value = 23
    session.add(t_value)

    h_value = Setttings()
    h_value.id = 2
    h_value.name = 'h_value'
    h_value.value = 50
    session.add(h_value)

    hb_value = Setttings()
    hb_value.id = 3
    hb_value.name = 'hb_value'
    hb_value.value = 75
    session.add(hb_value)

    session.commit()


if __name__ == '__main__':
    main()
