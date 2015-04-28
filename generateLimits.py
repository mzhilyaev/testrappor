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

parameters = {
 "f": [0.5, 0.4 , 0.3, 0.2, 0.1],
 "qp": [[1,0], [0.8, 0.2], [0.6,0.4]],
 "c": [1,10],
 "positiveFractions": [0.01 , 0.05, 0.1 , 0.2, 0.5]
}

## run N limits for various RAPOR configuration
## l is the smallest fraction of N default (1%)
## r is the max error (default 10%)
## for details see:
## https://docs.google.com/a/mozilla.com/document/d/1vsLa1A4tqivyyquQsqEhkff6qK9Y4ymlwkyXQNZ7_yk/edit#heading=h.jv0e4kdw15dv

def computeSampleSizeLimits(l = 0.01, r = 0.1):
  for c in parameters["c"]:
    for f in parameters["f"]:
      for qp in parameters["qp"]:
        basicRappor = BasicRappor(f,qp[0],qp[1])
        ## p = 1 - q, hence expected numbar does not matter
        N = 4 * basicRappor.variance(c, 0, 1) / (r*l)**2
        print "%d,%.1f,%.1f,%.1f,%.0f" % (c,f,qp[0],qp[1],N)
  
### N is number of users not views
def computeErrorLimits(N): 
  for c in parameters["c"]:
    for pr in parameters["positiveFractions"]:
      for f in parameters["f"]:
        for qp in parameters["qp"]:
          basicRappor = BasicRappor(f,qp[0],qp[1])
          ## p = 1 - q, hence expected numbar does not matter
          e = 2 * sqrt(basicRappor.variance(c, 0, N*c)) / (pr*N*c)
          print "%d,%.0f,%.0f,%.1f,%.1f,%.1f,%.2f" % (c,pr*100,pr*N*c,f,qp[0],qp[1],e*100)

if __name__ == '__main__':
    computeErrorLimits(10000)

