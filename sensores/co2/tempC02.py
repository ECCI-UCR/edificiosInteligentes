# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_scd30
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "3VqxnTbbIwFsZdNcZrC1Dhuze75JrCqNRDIcpjkU047XI1qy21e_Hy-faVVzwuCMFjgCO-2ZuUJ6mf7pR1M2IQ=="
#token = "87BN5OIsqZtTt6BFSP_2JKlJa_9tcZrsxN3Y5Dxv_557stycFHkjXEtJMIVVnVZT_dghdPUWQWseK4MqW0iRNQ=="
org = "UCR"
bucket = "sensores"

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

with InfluxDBClient(url="http://192.168.1.115:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    while True:
        if scd.data_available:
            data = "air,host=Lab4-19 co2="
            data += str(scd.CO2)
            data += ",temp="
            data += str(scd.temperature)
            write_api.write(bucket, org, data)
            #print("Data Available!")
            #print("CO2: %d PPM" % scd.CO2)
            #print("Temperature: %0.2f degrees C" % scd.temperature)
            #print("Humidity: %0.2f %% rH" % scd.relative_humidity)
            #print("")
            #print("Datos enviados")
            #print("")

        time.sleep(0.5)
client.close()
