from typing import List
from HueLight import HueLight
from HueDevice import HueDevice
from random import random
from Config import DEVICES_DEFINITION
from threading import Thread
from HueDevice import HueDevice

#### Bluetooth methods

###
# Check connection, and try to reconnect if disconnected
###
def check_connection(device: HueLight) -> None:
  if (not device.is_connected()):
    print("Reconnecting")
    device.connect()

def get_initialized_devices():
  devices = dict()
  for device_def in DEVICES_DEFINITION:
    device = HueDevice(device_def["name"], device_def["mac_address"])
    def run():
      device.open_connection()
      devices[device_def["name"]] = device
      device.connection.connect()
      device.manager.run()
    t = Thread(target=run, daemon=True)
    t.start()
    # device.barrier.wait()
  return devices
