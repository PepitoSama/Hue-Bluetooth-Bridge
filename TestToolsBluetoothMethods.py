import unittest
import Tools

class TestToolsBluetoothMethods(unittest.TestCase):

  def setUp(self):
    self.devices = Tools.get_initialized_devices(True)
    self.active_device = Tools.get_device(self.devices, "MainLight")

  def test_connect_to_devices(self):
    self.assertTrue(Tools.is_connected(self.active_device))

  def tearDown(self):
    for device in self.devices.values():
      device.connection.disconnect()

  if __name__ == '__main__':
    unittest.main()