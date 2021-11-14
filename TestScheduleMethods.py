import unittest
import Tools
import flask
from Config import Config

class TestToolsBluetoothMethods(unittest.TestCase):

  def setUp(self):
    self.app = flask.Flask(__name__)
    self.app.config.from_object(Config())
    self.devices = Tools.get_initialized_devices(True)
    self.scheduler = Tools.initialize_scheduler(self.app)
    self.original_jobs = Tools.get_jobs()

  def test_add_saved_job(self):
    job = {
      "id": "testFunc",
      "func": "toggle_light_every",
      "device_name": "MainLight",
      "second": 1
    }
    Tools.jobJsonToJob(job, self.scheduler, self.devices)
    self.assertTrue(self.scheduler.get_job("testFunc") is not None)

  def test_not_saved_job(self):
    self.assertTrue(self.scheduler.get_job(" ") is None)

  def test_overwrite_job(self):
    new_jobs = [
      {
        "id": "testFunc1",
        "func": "randomFunc",
        "second": 5
      },
      {
        "id": "testFunc2",
        "func": "randomFunc",
        "second": 6
      },
      {
        "id": "testFunc3",
        "func": "randomFunc",
        "second": 7
      }
    ]

    Tools.overwrite_jobs(new_jobs)

    jobs = Tools.get_jobs()
    self.assertTrue(jobs[0]["id"] == "testFunc1")
    self.assertTrue(jobs[0]["func"] == "randomFunc")
    self.assertTrue(jobs[0]["second"] == 5)

    self.assertTrue(jobs[1]["id"] == "testFunc2")
    self.assertTrue(jobs[1]["func"] == "randomFunc")
    self.assertTrue(jobs[1]["second"] == 6)

    self.assertTrue(jobs[2]["id"] == "testFunc3")
    self.assertTrue(jobs[2]["func"] == "randomFunc")
    self.assertTrue(jobs[2]["second"] == 7)


  def tearDown(self):
    Tools.delete_job("testjob")
    Tools.overwrite_jobs(self.original_jobs)

  if __name__ == '__main__':
    unittest.main()