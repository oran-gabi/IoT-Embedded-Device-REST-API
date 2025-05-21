import requests

base = "http://localhost:5000"

print("Temperature:", requests.get(f"{base}/temperature").json())
print("Humidity:", requests.get(f"{base}/humidity").json())
print("Status:", requests.get(f"{base}/status").json())
print("Uptime:", requests.get(f"{base}/uptime").json())
print("Info:", requests.get(f"{base}/info").json())
print("Set Interval:", requests.post(f"{base}/set-interval", json={"interval": 5}).json())
print("Current Mode:", requests.get(f"{base}/mode").json())
print("Update Mode:", requests.post(f"{base}/mode", json={"mode": "maintenance"}).json())
print("Restarting:", requests.post(f"{base}/restart").json())
