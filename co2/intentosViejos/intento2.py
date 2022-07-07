# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_scd30
from datetime import datetime
import sys
from socket import *

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)
file_object = open('sample.txt', 'a')
MYPORT = 5000
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if scd.data_available:
        #print("Data Available!")
        #print("CO2: %d PPM" % scd.CO2)
        #print("Temperature: %0.2f degrees C" % scd.temperature)
        #print("Humidity: %0.2f %% rH" % scd.relative_humidity)
        #print("")
        #print("Waiting for new data...")
        #print("")

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file_object.write(current_time)
        file_object.write(" ---- CO2: %d PPM" % scd.CO2)
        file_object.write("\n")
        strings = str(scd.CO2, 'utf8')
        #s.sendto(strings, ('<broadcast>', MYPORT))
        time.sleep(10)

file_object.close()

