from requests import post
import json

url = "http://192.168.31.216:8123/api/services/media_player/play_media"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNjVmZWMzNzNmNDQ0MGE5OTA1NjhhN2IxYzk3YjkwYiIsImlhdCI6MTY5NTE3MjQwNywiZXhwIjoyMDEwNTMyNDA3fQ.gxf8CAPjR_tOkc-A0i0J_apYkKjeQtbeCj0wYKra8YY",
}
data = {" media_content_id" : "http://192.168.31.143:9000/intento1.mp4", "media_content_type" : "video", "enqueue" : "play", "entity_id" : "media_player.chromecast4051"}
#target = {"device_id" : "d102e21d40fe1b3806fbaf3e7e2071d9"}
response = post(url, headers=headers, json=data)
print(response.text)
