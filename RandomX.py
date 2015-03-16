#!/usr/bin/python -u
####!/usr/local/bin/python3
import sys
import re
import logging
import random
import math
import os

class RandomX:
  def __init__(self):
    self.total = 0
    self.X = 0
    self.Xsq = 0

  def consume(self, value):
    self.total += 1
    self.X += value
    self.Xsq += value*value

  def mean(self):
    return self.X / self.total

  def variance(self):
    return self.Xsq / self.total - (self.X / self.total)**2

if __name__ == '__main__':
  pass

