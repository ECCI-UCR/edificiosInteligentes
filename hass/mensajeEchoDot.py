from requests import post
import json

url = "http://192.168.31.216:8123/api/services/notify/alexa_media_luis_s_echo_dot"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNjVmZWMzNzNmNDQ0MGE5OTA1NjhhN2IxYzk3YjkwYiIsImlhdCI6MTY5NTE3MjQwNywiZXhwIjoyMDEwNTMyNDA3fQ.gxf8CAPjR_tOkc-A0i0J_apYkKjeQtbeCj0wYKra8YY",
}
data = {"message": "Hola Luis, me pusieron a hablar desde Python"}
response = post(url, headers=headers, json=data)
print(response.text)
