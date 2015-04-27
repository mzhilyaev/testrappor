#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
from BasicRappor import BasicRappor

class User:
  def __init__(self, bit, rapporInstance):
    self.bit = bit
    self.rappor = rapporInstance
    self.randomizeOnce()

  def randomizeOnce(self):
    self.rrBit = self.rappor.permanentRandomization(self.bit)
    
  def report(self):
    return self.rappor.instantaneousRandomization(self.rrBit)

if __name__ == '__main__':
  pass

