import unittest
from BinDistro import BinDistro
from RandomX import RandomX
from BasicRappor import BasicRappor

class TestPreprocess(unittest.TestCase):
    def setUp(self):
        pass

    def assertPercentDiff(self, value1, value2, limit):
      self.assertTrue(abs((value1 - value2)*100.0 / value2) < limit)

    ### test variance computation for bernoulli trails with parameter q
    ### from random variable c*f where c is chosen with probability f
    ### 0 otherwise - this models freqency cap 
    def testStepWiseBernoulli(self):
      pass
      return
      tests = [ 
        { "q" : 0.5, "f": 0.5 , "c": 10 },
        { "q" : 0.1, "f": 0.9 , "c": 10 },
        { "q" : 0.2, "f": 0.3 , "c": 10 },
        { "q" : 0.9, "f": 0.9 , "c": 10 },
        { "q" : 0.1, "f": 0.1 , "c": 10 },
        { "q" : 0.5, "f": 0.5 , "c": 1 },
        { "q" : 0.1, "f": 0.5 , "c": 1 },
        { "q" : 0.1, "f": 0.1 , "c": 100 },
      ]
      rounds = 50000
      distro = BinDistro()
      for test in tests:
        ### setup paramters
        q = test["q"]
        f = test["f"]
        c = test["c"]
        ### emperical random variable to collect results of randomization
        ### for each round
        ev = RandomX()
        ### run the rounds
        for i in xrange(rounds):
          res = 0;
          ### get the bit equal to 1 from probability f
          bit = distro.getBit(f)
          if (bit):
            ### if bit is set we should randomize it c times with frequency q
            for j in xrange(c):
              res += distro.getBit(q)
          ### add results of accumulation to ev
          ev.consume(res * 1.0);
        ### after all rounds done compare emperical mean and variance to theoretical ones
        mean = c*q*f
        ### teoretical variance is (VAR(Binomial(q,c)) + cq**2)*f - (cqf)**2
        ### which is cqf(1 - q - cq + cqf)
        variance = c*q*f*(1 - q + c*q - c*q*f)

        #print ev.mean(), ev.variance(), mean, variance 
        self.assertPercentDiff(ev.mean(), mean, 5)
        self.assertPercentDiff(ev.variance(), variance, 5)
      pass

       
    ### test one sided single bit rappor accumulation for signal bit
    ### with frequency cap c and rappor paramters f,q,p
    def testSignalBitRAPPORAccumulation(self):
      tests = [ 
        { "q" : 0.6, "p": 0.4, "f": 0.5 , "c": 10 }
      ]
      rounds = 10000
      distro = BinDistro()
      for test in tests:
        ### setup paramters
        q = test["q"]
        p = test["p"]
        f = test["f"]
        c = test["c"]
        basicRappor = BasicRappor(f,q,p);
        ### emperical random variable to collect results of randomization for each round
        ev = RandomX()
        ### run the rounds
        for i in xrange(rounds):
          permanentBit = basicRappor.permanentRandomization(1)
          res = 0;
          for j in xrange(c):
             res += basicRappor.instantaneousRandomization(permanentBit)
          ### add total to ev
          ev.consume(res * 1.0);
        ### after all rounds done compare emperical mean and variance to theoretical ones
        mean = c * (q*(1-f/2) + p*f/2)
        ### teoretical variance is involved:
        variance = c*q*(1-f/2)*(1 - q + c*q - c*q*(1-f/2)) + c*p*f/2*(1 - p + c*p - c*p*f/2) - 2*c*q*(1-f/2)*c*p*f/2

        ### simlified form of variance
        mean_X1 = c*q*(1-f/2)
        mean_X0 = c*p*f/2
        variance_from2 = mean_X1*(1 - q + c*q) + mean_X0*(1 - p + c*p) - (mean_X1 + mean_X0)**2

        prod_X1 = q*(1-f/2)
        prod_X0 = p*f/2
        variance_from3 = c * (prod_X1*(1 - q + c*q) + prod_X0*(1 - p + c*p) - c*(prod_X1 + prod_X0)**2)

        print ev.mean(), ev.variance(), mean, variance, variance_from2, variance_from3
        self.assertPercentDiff(variance, variance_from2, 0.0001)
        self.assertPercentDiff(variance, variance_from3, 0.0001)
        self.assertPercentDiff(ev.mean(), mean, 5)
        self.assertPercentDiff(ev.variance(), variance, 5)
      pass

       
