#!/usr/bin/env python
import dbus
import gatt
from typing import Dict, List
from Routes import configureRoutes
from Config import DEVICES_DEFINITION
from HueDevice import HueDevice

from HueLight import HueLight

# API imports
import flask

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
  device.barrier.wait()

  # Initialize bluetooth connection with saved devices
  devices = Tools.get_initialized_devices()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

configureRoutes(app, devices)

app.run(host='0.0.0.0')
