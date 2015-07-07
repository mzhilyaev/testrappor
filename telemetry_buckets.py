#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import json

  
def exponential_buckets(dmin, dmax, n_buckets):
     check_numeric_limits(dmin, dmax, n_buckets)
     log_max = math.log(dmax);
     bucket_index = 2;
     ret_array = [0] * n_buckets
     current = dmin
     ret_array[1] = current
     for bucket_index in range(2, n_buckets):
         log_current = math.log(current)
         log_ratio = (log_max - log_current) / (n_buckets - bucket_index)
         log_next = log_current + log_ratio
         next_value = int(math.floor(math.exp(log_next) + 0.5))
         if next_value > current:
             current = next_value
         else:
             current = current + 1
         ret_array[bucket_index] = current
     return ret_array

def check_numeric_limits(dmin, dmax, n_buckets):
    if type(dmin) != int:
        raise DefinitionException, "minimum is not a number"
    if type(dmax) != int:
        raise DefinitionException, "maximum is not a number"
    if type(n_buckets) != int:
        raise DefinitionException, "number of buckets is not a number"

if __name__ == '__main__':
  buckets = exponential_buckets(1,1200,100)
  print buckets
    

