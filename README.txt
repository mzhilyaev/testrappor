RAPPOR Simulator

1. create config file config.json

{
  "rrFreq": 0.3,
  "irOneFreq": 0.6,
  "irZeroFreq": 0.4,
  "testRounds": 1000,
  "totalUsers": 10000,
  "freqCap": 2,
  "positiveFraction": 0.1
}

rrFreq - RAPPOR f
irOneFreq - RAPPOR q
irZeroFreq - RAPPOR p
testRounds - how many test iterations simulator will make
totalUsers - how many users (or clients) participate in simulation
positiveFraction - a fraction of totalUsers that have signal bit set
freqCap - a number of times a user will report permanent bit using instantaneous randomization



