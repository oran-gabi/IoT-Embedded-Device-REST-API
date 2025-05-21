import random
import time

# Simulate reading a temperature sensor

def read_temperature():
    return round(20 + 5 * random.random(), 2)

# Simulate reading a humidity sensor


def read_humidity():
    return round(40 + 10 * random.random(), 2)