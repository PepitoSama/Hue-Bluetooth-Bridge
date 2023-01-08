from typing import List
from Tools import check_connection
from threading import Thread
from flask import request
import flask
import FR as LANG


# Const
from Config import API_START_URI

def configureRoutes(app: flask.Flask, devices: dict):
  @app.route(API_START_URI + 'toggle', methods=['GET'])
  def toggle():
      device_name = request.args.get('device_name')
      if (device_name):
        device = devices.get(device_name)
        if (device != None):
          check_connection(device.connection)
          device.connection.toggle_light()
          return {
            "message": "ok"
          }
        else:
          return {
            "error": LANG.DEVICE_NOT_KNOWN
          }
      else:
        return {
          "error": LANG.NEED_TO_SPECIFY_DEVICE_NAME
        }

  @app.route(API_START_URI + 'brightness/<int:value>', methods=['GET'])
  def set_brightness(value):
      device_name = request.args.get('device_name')
      if (device_name):
        device = devices.get(device_name)
        if (device != None):
          check_connection(device.connection)
          def run():
              device.connection.set_brightness(value)
          t = Thread(target=run, daemon=True)
          t.start()
          print(value)
          return "ok"
        else:
          return {
            "error": LANG.DEVICE_NOT_KNOWN
          }
      else:
        return {
          "error": LANG.NEED_TO_SPECIFY_DEVICE_NAME
        }

  @app.route(API_START_URI + 'brightness/vary/<string:value>', methods=['GET'])
  def vary_brightness(value):
      device_name = request.args.get('device_name')
      if (device_name):
        device = devices.get(device_name)
        if (device != None):
          check_connection(device.connection)
          def run():
              device.connection.varyBrightness(int(value))
          t = Thread(target=run, daemon=True)
          t.start()
          return "ok"
        else:
          return {
            "error": LANG.DEVICE_NOT_KNOWN
          }
      else:
        return {
          "error": LANG.NEED_TO_SPECIFY_DEVICE_NAME
        }

  @app.route(API_START_URI + 'brightness', methods=['GET'])
  def get_brightness():
      device_name = request.args.get('device_name')
      if (device_name):
        device = devices.get(device_name)
        if (device != None):
          return {
            "message": str(device.connection.getBrightness())
          }
        else:
          return {
            "error": LANG.DEVICE_NOT_KNOWN
          }
      else:
        return {
          "error": LANG.NEED_TO_SPECIFY_DEVICE_NAME
        }

  @app.route(API_START_URI + 'active', methods=['GET'])
  def get_active_state():
    device_name = request.args.get('device_name')
    if (device_name):
      device = devices.get(device_name)
      if (device != None):
        return str(device.connection.is_connected())
      else:
        return {
          "error": LANG.DEVICE_NOT_KNOWN
        }
    else:
      return {
        "error": LANG.NEED_TO_SPECIFY_DEVICE_NAME
      }