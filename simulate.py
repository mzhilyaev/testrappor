#!/usr/bin/python

import sys
import re
import logging
from optparse import OptionParser
from math import sqrt
import json
import re
from BasicRappor import BasicRappor
from RandomX import RandomX
from User import User

def runTest(config):
  basicRappor = BasicRappor(
                  config["rrFreq"],
                  config["irOneFreq"],
                  config["irZeroFreq"])
  rounds = config["testRounds"]
  totalUsers = config["totalUsers"]
  submissions = config["totalSubmission"]
  positiveFraction = config["positiveFraction"]

  ## set up empirical mean and variance tracker
  estimatedValue = RandomX()

  ### frequency cap = submissions/totalUsers, because each user will need to submit
  ### cap times to get desired number of submissions
  freqCap = submissions * 1.0 /totalUsers;

  ### repeat the test round times
  for i in xrange(rounds):
    # populate users array: set 1 for positiveFraction of users and 0 for rest
    users = [User(j < totalUsers*positiveFraction, basicRappor) for j in xrange(totalUsers)]
    total = 0
    ### collect user submissions
    for j in xrange(totalUsers):
      total += freqCap * users[j].get()
    ### collect experimental extracted value
    #print basicRappor.extractCount(total, submissions), submissions*positiveFraction
    estimatedValue.consume(basicRappor.extractCount(total, submissions))

  ### print results
  print estimatedValue.mean(), sqrt(estimatedValue.variance()), sqrt(freqCap*basicRappor.variance(submissions)), basicRappor.oneIfTrue , basicRappor.oneIfFalse


def read_args():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config", help="simulation config file")
    parser.add_option("-p", "--param", dest="params", help="override config params")
    return parser.parse_args()

def setOverides(config, paramsString):
  if (paramsString == False):
    return
  params = re.split(",", paramsString);
  for param in params:
    (key, val) = re.split("=", param)
    config[key] = float(val)
  

if __name__ == '__main__':
    (options, args) = read_args()
    config = json.load(open(options.config,"r"));
    setOverides(config, options.params or False)
    runTest(config)

