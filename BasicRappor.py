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
    ### if original bit is set
    self.oneIfTrue = 0.5 * self.f * (self.p + self.q) + (1 - self.f)*self.q
    ### if original bit is off
    self.oneIfFalse = 0.5 * self.f * (self.p + self.q) + (1 - self.f)*self.p
    ### distribution object
    self.distro = BinDistro()

  def randomizeValue(self, value):
    retValue = value;
    ## first round of randomization - randomised response
    ## lie with probability f
    if (self.distro.getBit(self.f)):
      ## if we lie, generate random bit
      retValue = self.distro.getBit(0.5)

    ### second round of randomization
    ### for 1 generate 1 with probability q
    ### for 0 generate 1 with probability p
    if (retValue):
      retValue = self.distro.getBit(self.q)
    else:
      retValue = self.distro.getBit(self.p)

    ### return randomised bit
    return retValue

  def extractCount(self, totalOnes, sampleSize):
    return (totalOnes - sampleSize*self.oneIfFalse) / (self.oneIfTrue - self.oneIfFalse)
    
  def variance(self, sampleSize):
    return sampleSize*self.oneIfFalse*(1-self.oneIfFalse) / (self.oneIfTrue - self.oneIfFalse)**2

  def randomizeDictionary(self, theDict):
    retDict = {}
    for key, value in theDict.items():
      retDict[key] = self.randomizeValue(value)
    return retDict

  def extractFromDictionary(self, theDict, sampleSize):
    retDict = {}
    for key, value in theDict.items():
      retDict[key] = self.extractCount(value, sampleSize)
    return retDict

  def randomizeList(self, lst):
    return [self.randomizeValue(val) for val in lst]

  def extractFromList(self, lst, sampleSize):
    return [self.extractCount(val, sampleSize) for val in lst]

if __name__ == '__main__':
  bRappor = BasicRappor(0.5,1,0)
  print bRappor.randomizeList([1,1,0,0])

