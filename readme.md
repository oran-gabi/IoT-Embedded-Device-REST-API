# ✅IoT Embedded Device REST API – Remote Monitoring & Control System

a complete IoT Device REST API Project with optional iOS/web clients 

## 📁 Project Structure

iot_device_project/
├── README.md
├── device/
│   ├── rest_api.py         # Flask REST API for the IoT device
│   ├── sensor.py           # (Simulated) sensor reading logic
│   ├── device.py
│   ├── device_mode.py
│   └── requirements.txt    # Python dependencies
├── mobile_client_ios/
│   └── SwiftUI_Client/     # Optional iOS app (Xcode project)
├── web_dashboard/
│   ├── index.html          # Web client with Axios to call API
│   └── app.js
├── test/
│   └── api_test.py        # Python script to test all API endpoints

- `device/rest_api.py`: Flask API using a `Device` class
- `device/device.py`: Main OOP class encapsulating all device behavior
- `device/device_mode.py`: Enum for device operation modes
- `device/sensor.py`: Simulated sensor readings
- `test/api_test.py`: Test suite for API endpoints
- `web_dashboard/`: Simple web UI





## 🔧 Key Features

| Feature         | Description                              |
| --------------- | ---------------------------------------- |
| `/temperature`  | Read current temperature from the device |
| `/status`       | View device status                       |
| `/restart`      | Remotely restart the device              |
| `/set-interval` | Configure reading interval               |
| Web client      | Control/monitor from browser             |
| iOS client      | Native Swift app (optional)              |
| Python testing  | Script to validate API endpoints         |

## 🧠 Technologies Used

* Embedded Linux (Raspberry Pi / similar)

* Python 3

* Flask

* Bash scripts / system calls

* Swift / SwiftUI (optional)

* HTML/CSS/JS with Axios

* curl / Postman for API testing


# IoT Device REST API

A simulated REST API for an embedded Linux IoT device using Flask.

## Features
- Read temperature & humidity from simulated sensors
- Monitor uptime and current device mode
- Restart device and change device mode using enums
- Set read interval dynamically
- Simple web dashboard with temperature and humidity display
- Ready for mobile/web integration or IoT expansion

## Run the Server
```bash
cd device
pip install -r requirements.txt
python rest_api.py
```

## Test APIs
```bash
python test/api_test.py
```

## Web Dashboard
Open `web_dashboard/index.html` in your browser.

---

You can now upload this folder structure to GitHub with commit messages like:

```bash
git init
git add .
git commit -m "Initial commit: IoT device REST API"
git remote add origin https://github.com/yourusername/iot-device-rest-api.git
git push -u origin main

## Enum Device Modes
Supported modes via POST `/mode`:
- `normal`
- `maintenance`
- `restarting`

```bash
curl -X POST http://localhost:5000/mode -H "Content-Type: application/json" -d '{"mode": "maintenance"}'

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request