#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
from math import sqrt

class RandomX:
  def __init__(self):
    self.total = 0
    self.X = 0
    self.Xsq = 0
    self.values = []

  def consume(self, value):
    self.total += 1
    self.X += value
    self.Xsq += value*value
    self.values.append(value)

  def mean(self):
    return self.X / self.total

  def variance(self):
    return self.Xsq / self.total - (self.X / self.total)**2

  def addRandomX(self, rx):
    self.total += rs.total
    self.X += rs.X
    self.Xsq += rs.Xsq
    self.values = self.values + rs.values

  def normalize(self):
    mean = self.mean()
    sigma = sqrt(self.variance())
    for i in xrange(len(self.values)):
      self.values[i] = (self.values[i] - mean) / sigma

  def save(self, outFile, normalize=False):
    if (normalize):
      self.normalize()

    f = open(outFile, "w")
    for value in self.values:
      f.write("%f\n" % value)


if __name__ == '__main__':
  pass

