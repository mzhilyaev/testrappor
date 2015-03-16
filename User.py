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
    self.randomize()

  def randomize(self):
    self.randomBit = self.rappor.randomizeValue(self.bit)
    
  def get(self):
    return self.randomBit

if __name__ == '__main__':
  pass

