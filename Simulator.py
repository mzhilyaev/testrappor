#!/usr/bin/python
import sys
import re
import logging
from optparse import OptionParser
from math import sqrt
import json
import re
import random
from BasicRappor import BasicRappor
from RandomX import RandomX
from User import User

def simulate(config, output=True, save=False):
  basicRappor = BasicRappor(
                  config["rrFreq"],
                  config["irOneFreq"],
                  config["irZeroFreq"])
  rounds = config["testRounds"]
  positiveFraction = config["positiveFraction"]
  totalUsers = int(config["totalUsers"])
  freqCap = int(config["freqCap"])
  skipInstanteneousRandomizarion = False
  doSave = config["save"] or save

  if (config["irOneFreq"] == 1 and config["irZeroFreq"] == 0):
    skipInstanteneousRandomizarion = True

  ## compute total submissions - each user will report its random bit freqCap times
  submissions = freqCap*totalUsers
  ## number of users that have signal bit set
  positiveUsers = totalUsers*positiveFraction
  ## set up empirical mean and variance tracker
  estimatedValue = RandomX()

  ### repeat the test round times
  for i in xrange(rounds):
    # reset random number generator for every test round
    random.seed(i + random.randint(1,rounds))
    # populate users array: set 1 for positiveFraction of users and 0 for rest
    users = [User(j < positiveUsers, basicRappor) for j in xrange(totalUsers)]
    total = 0
    ### collect user submissions
    for j in xrange(totalUsers):
      if (skipInstanteneousRandomizarion):
        total += freqCap*users[j].report()
      else:
        for k in xrange(freqCap):
          total += users[j].report()
    ### collect experimental extracted value
    #print basicRappor.extractCount(total, submissions), submissions*positiveFraction
    estimatedValue.consume(basicRappor.extractCount(total, submissions))


  ### print results
  if (output):
    print "Total reports     %d" % (totalUsers*freqCap)
    print "Theoretical mean  %d" % (positiveUsers*freqCap)
    print "Empirical mean    %d" % estimatedValue.mean()
    print "Theoretical sigma %0.3f" % sqrt(basicRappor.variance(freqCap, positiveUsers*freqCap, submissions))
    print "Empirical sigma   %0.3f" % sqrt(estimatedValue.variance())

  if (doSave):
    ### make a file name
    ### make the file prefix
    filePrefix = "%d,%d,%d,%.1f,%.1f,%.1f" % (submissions \
                                              , positiveUsers*freqCap \
                                              , freqCap \
                                              , config["rrFreq"] \
                                              , config["irOneFreq"] \
                                              , config["irZeroFreq"] \
                                            )
    ### save sample to a file
    estimatedValue.save(filePrefix + ".sample.out")

    ### save stats to file
    statsFile = open(filePrefix + ".stats.out", "w")
    statsFile.write( filePrefix + ",%.4f,%.4f,%.4f,%.2f,%.2f" % ( \
                                      estimatedValue.mean() \
                                    , sqrt(estimatedValue.variance()) \
                                    , sqrt(basicRappor.variance(freqCap, positiveUsers*freqCap, submissions)) \
                                    , basicRappor.oneIfTrue \
                                    , basicRappor.oneIfFalse \
                                  ))
