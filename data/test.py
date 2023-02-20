import unittest
from data_getter import *


class TestData(unittest.TestCase):
    def test_temp_hum_sns(self):
        self.assertIsInstance(temperature_and_humidity_sensors(), list)

    def test_hum_sns(self):
        self.assertIsInstance(hum_sensors(), list)

    def test_windows_control(self):
        self.assertIsInstance(window_pane_control(0), Statuses)

    def test_watering(self):
        for i in range(1, 7):
            self.assertIsInstance(management_of_watering_beds(0, i), Statuses)

    def test_hum_system(self):
        self.assertIsInstance(control_of_the_humidification_system(0), Statuses)


if __name__ == "__main__":
    unittest.main()