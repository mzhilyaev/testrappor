#!/usr/bin/python -u
####!/usr/local/bin/python3
import sys
import re
import logging
import random
import math
import os
from BinDistro import BinDistro

class BasicRappor:
  def __init__(self, randomResponseLiesFreq, instResponse1Freq, instResponse0Freq):
    self.reset(randomResponseLiesFreq, instResponse1Freq, instResponse0Freq)

  def reset(self, randomResponseLiesFreq, instResponse1Freq, instResponse0Freq):
    self.f = randomResponseLiesFreq
    self.q = instResponse1Freq
    self.p = instResponse0Freq
    ### compute probablities for extraction
    ### if original bit is set - this corresponds tp q* probability
    self.oneIfTrue = 0.5 * self.f * (self.p + self.q) + (1 - self.f)*self.q
    ### if original bit is off - this corresponds to p* probability
    self.oneIfFalse = 0.5 * self.f * (self.p + self.q) + (1 - self.f)*self.p
    ### distribution object
    self.distro = BinDistro()

  def permanentRandomization(self, value):
    ## first round of randomization - randomised response
    ## lie with probability f
    if (self.distro.getBit(self.f)):
      ## if we lie, generate random bit
      value = self.distro.getBit(0.5)

    ### return permanent bit
    return value

  def instantaneousRandomization(self, value):
    ### check if we need to do instantaneous randomization
    if (self.q == 1 and self.p == 0):
      return value
    ### second round of randomization
    ### for 1 generate 1 with probability q
    ### for 0 generate 1 with probability p
    if (value):
      value = self.distro.getBit(self.q)
    else:
      value = self.distro.getBit(self.p)

    ### return instantaneous bit
    return value

  def extractCount(self, observedSum, totalSize):
    return (observedSum - totalSize*self.oneIfFalse) / (self.oneIfTrue - self.oneIfFalse)
    
  def variance(self, c, expectedNumber, totalSize):
    ### variable naming follows conventions in the document below
    ### signal bit products
    q = self.q
    p = self.p
    f = self.f
    prod_X1 = q*(1-f/2)
    prod_X0 = p*f/2
    variancePrimeX = prod_X1*(1 - q + c*q) + prod_X0*(1 - p + c*p) - c*(prod_X1 + prod_X0)**2

    prod_Y1 = q*f/2
    prod_Y0 = p*(1-f/2)
    variancePrimeY = prod_Y1*(1 - q + c*q) + prod_Y0*(1 - p + c*p) - c*(prod_Y1 + prod_Y0)**2

    variance = (variancePrimeX * expectedNumber + variancePrimeY * (totalSize - expectedNumber)) / (self.oneIfTrue - self.oneIfFalse)**2
    return variance

if __name__ == '__main__':
  bRappor = BasicRappor(0.5,1,0)
  print bRappor.randomizeList([1,1,0,0])

