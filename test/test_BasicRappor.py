import unittest
from math import sqrt
from BasicRappor import BasicRappor
from RandomX import RandomX
from User import User

class TestBasicRappor(unittest.TestCase):
    def setUp(self):
        pass

    def testBasicRappor(self):
      return
      ### start with no instantaneous randomization
      basicRappor = BasicRappor(0.5, 0.6, 0.3)
      N = 1000
      estimatedValue = RandomX()

      ### do 1000 submitions of N/2 ones and N/2 zeros
      ### and collect stats
      for j in xrange(1000): 
        total = 0
        ### submit 1 N/2 times and 0 N/2 times and compute total
        for i in xrange(N):
          total += basicRappor.randomizeValue(i % 2)
        estimatedValue.consume(basicRappor.extractCount(total, N))

      print estimatedValue.mean(), sqrt(estimatedValue.variance()), sqrt(basicRappor.variance(N)) , basicRappor.oneIfTrue , basicRappor.oneIfFalse

    def testMomorizedRappor(self):
      basicRappor = BasicRappor(0.5, 0.6, 0.4)
      N = 1000
      K = 100
      estimatedValue = RandomX()


      ### frequency cap testing - let each user report a bit N/K times
      for i in xrange(10000):
        # create K users with proper distribution of 1 and 0
        users = [User((j%10) == 0, basicRappor) for j in xrange(K)]
        # run through these users and make the report the bit N/K times
        total = 0
        for j in xrange(K):
          total += N/K*users[j].get()
        estimatedValue.consume(basicRappor.extractCount(total, N))

      print estimatedValue.mean(), sqrt(estimatedValue.variance()), sqrt(basicRappor.variance(N)) , basicRappor.oneIfTrue , basicRappor.oneIfFalse


        
        
