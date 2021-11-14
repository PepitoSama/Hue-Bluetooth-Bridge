#!/usr/bin/env python
from os import times
from typing import Dict, List
from threading import Thread, Barrier
from Routes import configureRoutes
from Config import DEVICES_DEFINITION
from HueDevice import HueDevice
from Tools import jobJsonToJob, toggle_light_every
from flask_apscheduler import APScheduler
import flask

from HueLight import HueLight

# Import json file
import json
with open('./jobs.json') as f:
  jobs = json.load(f)

devices = dict()

if __name__ == '__main__':
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


  app = flask.Flask(__name__)

  #Config Timezone
  class Config:
    SCHEDULER_API_ENABLED = False
    SCHEDULER_TIMEZONE = "Europe/Paris"

  app.config.from_object(Config())

  # initialize scheduler
  scheduler = APScheduler()
  scheduler.init_app(app)
  scheduler.start()


  # Add saved jobs
  decodedJobs = []
  for job in jobs:
    jobJsonToJob(job, scheduler, devices)

  configureRoutes(app, devices, scheduler)

  app.run(
    debug=True,
    host='0.0.0.0',
    use_reloader=True
  )