import time
from sensor import read_temperature, read_humidity
from device_mode import DeviceMode

# OOP class representing the device


class Device:
    def __init__(self, model="Simulated IoT Device", version="1.0"):
        self.start_time = time.time()
        self.interval = 10
        self.model = model
        self.version = version
        self.mode = DeviceMode.NORMAL

    def get_temperature(self):
        return read_temperature()

    def get_humidity(self):
        return read_humidity()

    def get_status(self):
        return {"status": self.mode.value}

    def get_uptime(self):
        uptime_secs = int(time.time() - self.start_time)
        return time.strftime('%H:%M:%S', time.gmtime(uptime_secs))

    def restart(self):
        self.mode = DeviceMode.RESTARTING
        return {"message": "Device restarting..."}

    def set_interval(self, new_interval):
        self.interval = new_interval
        return {"message": "Interval updated to " + str(new_interval)}

    def get_info(self):
        return {"model": self.model, "version": self.version}
    
    def get_mode(self):
        return {"mode": self.mode.value}

    def set_mode(self, mode_str):
        try:
            self.mode = DeviceMode(mode_str)
            return {"message": f"Mode updated to {mode_str}"}
        except ValueError:
            return {"error": "Invalid mode"}, 400
