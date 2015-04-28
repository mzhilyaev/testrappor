RAPPOR Simulator

1. create config file config.json

{
  "rrFreq": 0.3,
  "irOneFreq": 0.6,
  "irZeroFreq": 0.4,
  "testRounds": 1000,
  "totalUsers": 1000,
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


2.  running simulator

>> ./simulate.py -c config.json
Total reports     2000
Theoretical mean  200
Empirical mean    194
Theoretical sigma 159.783
Empirical sigma   168.081

3. overriding config parameters

>> ./simulate.py -c config.json -p freqCap=1,totalUsers=2000
Total reports     2000
Theoretical mean  200
Empirical mean    205
Theoretical sigma 158.146
Empirical sigma   153.725

4. saving sample to a file
>> ./simulate.py -c config.json -s

will create a file containing the sample and saple stats: 
2000,200,2,0.3,0.6,0.4.sample.out - contains extracted value for each simulation run
2000,200,2,0.3,0.6,0.4.stats.out - contains sample stats



