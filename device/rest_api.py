from flask import Flask, jsonify, request
from device import Device

app = Flask(__name__)
device = Device()

@app.route("/temperature")
def temperature():
    return jsonify({"temperature": device.get_temperature()})

@app.route("/humidity")
def humidity():
    return jsonify({"humidity": device.get_humidity()})

@app.route("/status")
def status():
    return jsonify(device.get_status())

@app.route("/uptime")
def uptime():
    return jsonify({"uptime": device.get_uptime()})

@app.route("/restart", methods=['POST'])
def restart():
    return jsonify(device.restart())

@app.route("/set-interval", methods=['POST'])
def set_interval():
    data = request.get_json()
    if 'interval' in data:
        return jsonify(device.set_interval(int(data['interval'])))
    return jsonify({"error": "Missing interval field"}), 400

@app.route("/info")
def info():
    return jsonify(device.get_info())

@app.route("/mode")
def get_mode():
    return jsonify(device.get_mode())

@app.route("/mode", methods=['POST'])
def set_mode():
    data = request.get_json()
    if 'mode' in data:
        return device.set_mode(data['mode'])
    return jsonify({"error": "Missing mode field"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
