#!/usr/bin/python -u
####!/usr/local/bin/python3
import sys
import re
import logging
import random
import math
import os

class BinDistro:
  def __init__(self):
    self.len = 200
    self.current = 0
    self.bits = [(i%2) for i in range(0,self.len)]
    for i in range(0, 100):
      random.shuffle(self.bits)

  def step(self):
    ret = self.bits[self.current]
    self.current += 1
    if (self.current >= self.len):
      random.shuffle(self.bits)

  def getBit(self, prob):
    randValue = random.random()
    if (randValue < prob):
      return 1
    else:
      return 0

if __name__ == '__main__':
  distro = BinDistro()
  total = 0
  for i in range(0,100):
    total += distro.getBit(0.5)
  print total

