import unittest
import Tools

class TestToolsBluetoothMethods(unittest.TestCase):

  def test_add_a_job(self):
    Tools.save_job(
      id="testjob",
      func="testFunc",
      trigger="cron",
      hour=22,
      hours=12,
      minute=34,
      minutes=56,
      second=45,
      seconds=23,
      start_date="2021-11-14 17:55:34",
      blblblbl=45
    )

    job = Tools.find_job("testjob")

    self.assertTrue(job.get("func") == "testFunc")
    self.assertTrue(job.get("trigger") == "cron")
    self.assertTrue(job.get("hour") == 22)
    self.assertTrue(job.get("hours") == 12)
    self.assertTrue(job.get("minute") == 34)
    self.assertTrue(job.get("minutes") == 56)
    self.assertTrue(job.get("second") == 45)
    self.assertTrue(job.get("seconds") == 23)
    self.assertTrue(job.get("start_date") == "2021-11-14 17:55:34")
    self.assertTrue(job.get("blblblbl") == 45)

  def tearDown(self):
    Tools.delete_job("testjob")

  if __name__ == '__main__':
    unittest.main()