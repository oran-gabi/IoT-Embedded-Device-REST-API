# ✅ IoT Embedded Device REST API – Remote Monitoring & Control System

A complete, modular, and testable IoT Device REST API project using Flask, Python OOP, and simulated sensors — with optional web/iOS client integration.

---

## 📁 Project Structure

```
IoT-Embedded-Device-REST-API/
├── README.md                    # Project documentation
├── device/                      # Core device logic and API server
│   ├── rest_api.py              # Flask REST API
│   ├── sensor.py                # Simulated sensor readings
│   ├── device.py                # OOP class to manage device state
│   ├── device_mode.py           # Enum for device modes
│   └── requirements.txt         # Python dependencies
├── web_dashboard/               # Simple front-end dashboard
│   ├── index.html               # HTML UI for dashboard
│   └── app.js                   # JavaScript fetch API calls
├── test/                        # API test scripts
│   └── api_test.py              # Script to test endpoints
```

---

## 🔧 Key Features

| Feature         | Description                              |
| --------------- | ---------------------------------------- |
| `/temperature`  | Read current temperature from the device |
| `/humidity`     | Read current humidity from the device    |
| `/status`       | View device status                       |
| `/uptime`       | View device uptime                       |
| `/mode` (GET)   | Get current device mode                  |
| `/mode` (POST)  | Change device mode using enums           |
| `/set-interval` | Configure sensor read interval           |
| `/restart`      | Simulate device restart                  |
| Web Dashboard   | Display real-time sensor data in browser |
| API Testing     | Automated Python testing using requests  |

---

## 🧠 Technologies Used

- Python 3
- Flask
- RESTful API Design
- Object-Oriented Programming
- Enums for state management
- HTML, JavaScript (Fetch API)
- curl / Postman for API testing

---

## 🚀 Getting Started

### 1. Run the Server
```bash
cd device
pip install -r requirements.txt
python rest_api.py
```

### 2. Test APIs with Python
```bash
python test/api_test.py
```

### 3. Open the Web Dashboard
Just open the file in your browser:
```bash
web_dashboard/index.html
```

---

## 📦 Enum Device Modes

Supported values for the `/mode` endpoint:
- `normal`
- `maintenance`
- `restarting`

Example:
```bash
curl -X POST http://localhost:5000/mode \
     -H "Content-Type: application/json" \
     -d '{"mode": "maintenance"}'
```

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature/my-feature`)
- Commit your changes (`git commit -am 'Add some feature'`)
- Push to the branch (`git push origin feature/my-feature`)
- Submit a pull request

For major changes, please open an issue first to discuss what you'd like to change.

---

Created with ❤️ by Oran Gabai