import unittest
from BinDistro import BinDistro

class TestPreprocess(unittest.TestCase):
    def setUp(self):
        pass

    def testBinDistro(self):
      binDistro = BinDistro()
      total = 0
      for i in range(0, 100):
        total += binDistro.getBit(0.5)
      self.assertTrue(abs(total - 50) < 10)
      print total
      pass

