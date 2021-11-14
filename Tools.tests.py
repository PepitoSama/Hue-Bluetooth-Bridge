import unittest
from Tools import get_initialized_devices, get_device, is_connected

class TestToolsMethods(unittest.TestCase):

  def setUp(self):
    self.devices = get_initialized_devices(True)
    self.active_device = get_device(self.devices, "MainLight")

  def test_connect_to_devices(self):
    self.assertTrue(is_connected(self.active_device))

  if __name__ == '__main__':
    unittest.main()