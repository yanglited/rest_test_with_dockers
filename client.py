import requests

url = "http://web-service:5000/api/greet"

response = requests.get(url)
data = response.json()

print("response: " + data["message"])
