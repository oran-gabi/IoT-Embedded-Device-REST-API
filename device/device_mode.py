from enum import Enum

# Define possible device modes

class DeviceMode(Enum):
    NORMAL = "normal"
    MAINTENANCE = "maintenance"
    RESTARTING = "restarting"