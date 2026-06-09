#!/usr/bin/python
from MangDang.mini_pupper.ESP32Interface import ESP32Interface

esp32 = ESP32Interface()
calibration = esp32.get_calibration()

if calibration is None:
    print("Failed to read calibration data from ESP32")
else:
    print(calibration)
