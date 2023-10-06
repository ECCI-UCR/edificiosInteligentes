from requests import get
import json

url = "http://192.168.31.216:8123/api/states/sensor.air_quality_monitor_indoor_air_quality"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNjVmZWMzNzNmNDQ0MGE5OTA1NjhhN2IxYzk3YjkwYiIsImlhdCI6MTY5NTE3MjQwNywiZXhwIjoyMDEwNTMyNDA3fQ.gxf8CAPjR_tOkc-A0i0J_apYkKjeQtbeCj0wYKra8YY",
    "content-type": "application/json",
}

response = get(url, headers=headers)
#print(response.text)
json = json.loads(response.text)
print(json["state"])
