from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

# You can generate an API token from the "API Tokens Tab" in the UI
token = "3VqxnTbbIwFsZdNcZrC1Dhuze75JrCqNRDIcpjkU047XI1qy21e_Hy-faVVzwuCMFjgCO-2ZuUJ6mf7pR1M2IQ=="
#token = "87BN5OIsqZtTt6BFSP_2JKlJa_9tcZrsxN3Y5Dxv_557stycFHkjXEtJMIVVnVZT_dghdPUWQWseK4MqW0iRNQ=="
org = "UCR"
bucket = "sensores"

with InfluxDBClient(url="http://192.168.1.115:8086", token=token, org=org) as client:
   write_api = client.write_api(write_options=SYNCHRONOUS)
#   data="sensorAire,place=Lab4-19 co2=425,humidity=45,temperature=25.5 4"
#   data="airSensor,sensorId=A0100,station=Harbor humidity=35.0658,temperature=21.667 1636729543000000000"
#   data = "mem2,host=host1 used_percent=21.43234543"
   for contador in range (1, 10):
      data = "air,host=Lab4-19 co2=426,temp=25"
      write_api.write(bucket, org, data)
      time.sleep(3)
#   query = 'from(bucket: "Sensores") |> range(start: -1h)'
#   tables = client.query_api().query(query, org=org)
#   for table in tables:
#      for record in table.records:
#         print(record)
client.close()
