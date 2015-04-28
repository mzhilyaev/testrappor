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
from Simulator import simulate

def read_args():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config", help="simulation config file")
    parser.add_option("-p", "--param", dest="params", help="override config params")
    parser.add_option("-s", "--save", dest="save", action="store_true", default=False, help="save simulated sample")
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
    config["save"] = options.save
    simulate(config)

