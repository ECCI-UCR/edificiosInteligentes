from requests import post
import json

url = "http://192.168.31.216:8123/api/services/light/turn_off"

#url = "http://localhost:8123/api/services/light/turn_on"
#headers = {"Authorization": "Bearer TOKEN"}
#data = {"entity_id": "light.primera_luz"}

#response = post(url, headers=headers, json=data)
#print(response.text)


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNjVmZWMzNzNmNDQ0MGE5OTA1NjhhN2IxYzk3YjkwYiIsImlhdCI6MTY5NTE3MjQwNywiZXhwIjoyMDEwNTMyNDA3fQ.gxf8CAPjR_tOkc-A0i0J_apYkKjeQtbeCj0wYKra8YY",
}
data = {"entity_id": "light.primera_luz"}
response = post(url, headers=headers, json=data)
print(response.text)
