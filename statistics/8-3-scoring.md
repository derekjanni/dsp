# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

First, I created a file that could be used with the command line to quickly simulate games and generate graphs called `soccer.py` shown below:

```python
import thinkstats2
import random
import math
import numpy as np
import scipy.stats as scp
import thinkplot

def nextTime(rate):
    "Implementation of 'waiting time' until next event in Poisson Processes"
    "Proof near top of second page: http://www.columbia.edu/~ks20/4404-Sigman/4404-Notes-ITM.pdf"
    "Note: Maybe a weird way to approach this one, but I couldn't help it"
    return -math.log(1.0 - random.random()) / rate

def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.           
                                                                                  
    estimate: sequence of numbers                                                 
    actual: actual value                                                          
                                                                                  
    returns: float RMSE                                                           
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    """Computes the mean error of a sequence of estimates.                        
                                                                                  
    estimate: sequence of numbers                                                 
    actual: actual value                                                          
                                                                                  
    returns: float mean error                                                     
    """
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

def Simulate(lam):
    """                                                                           
    This function simulates a soccer game based on an inputted lam, which denotes
    the average length of time between goals. We use basic queue-theory to model.
    This function models a Poisson process.                                       
    https://en.wikipedia.org/?title=Poisson_process                               
    """
    gametime = 0 #total time in a game                                            
    goals = 0 #total goals scored                                                 
    rate = float(lam)/90 #goals per game -> goals per minute                      
    while gametime < 90:
        gametime += nextTime(rate)
        goals += 1
    return(goals)

def SimMany(lam, n, rep):

    def CILine(height):
        thinkplot.plot(range(rep), [height for i in range(rep)])

    obs = []
    for i in range(rep):
        obs.append(Simulate(lam))

    actual = lam
    rmse = RMSE(obs, actual)
    me = MeanError(obs, actual)
    cdf = thinkstats2.Cdf(obs)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    thinkplot.Plot(obs)
    CILine(ci[0])
    CILine(ci[1])
    print("Standard Error: " + str(rmse))
    print("Mean Error: " + str(me))
    print('Confidence Interval: '+ str(ci))
    thinkplot.show(xlabel='Iteration', ylabel='Sample Value of Goals per Game')
```

By calling `soccer.Simulate(lam)` from the command line, you can simulate a single game. 

By calling `soccer.SimMany(lam, n, rep)` from the command line you can simulate (and plot) many games and deduce facts about the sampling distribution from there. Consider what happens for increasing values of `n`:

Assume lam=3 and sample 10 games 1000 times
```
Standard Error: 1.95294649184
Mean Error: 0.912
Confidence Interval: (1, 7)
```
![Simulation For (3, 10, 1000)](http://i.imgur.com/O1iaEnZ.png)

Assume lam=3 and sample 50 games 1000 times
```
Standard Error: 2.0059910269
Mean Error: 0.96
Confidence Interval: (1, 7)
```
![Simulation For (3, 50, 1000)](http://i.imgur.com/l0H4UI2.png)

Assume lam=3 and sample 500 games 1000 times
```
Standard Error: 1.96697737659
Mean Error: 0.961
Confidence Interval: (1, 7)
```
![Simulation for (3, 500, 1000)](http://i.imgur.com/emok8nd.png)

The `mean error` and `standard error` do not appear to decrease at all, even with large sample sizes!

What if we try varying `lam` instead? Below are calculations for increasing values of `lam` with n=50 & rep=1000
```
10:
Standard Error: 3.26879182574
Mean Error: 0.971
Confidence Interval: (6, 16
20:
Standard Error: 4.51275968782
Mean Error: 0.867
Confidence Interval: (14, 28)
50:
Standard Error: 7.18561062123
Mean Error: 0.789
Confidence Interval: (39, 63)
100:
Standard Error: 10.0511193407
Mean Error: 0.829
Confidence Interval: (84, 118)
```

Oddly enough, it appears that the Standard Error actually *increases* for increasing `lam`. In fact, for all values of `lam` that I plugged in, the Standard Error is approximately equal to the root of `lam`! I suspect there is a proof of this out there somewhere...


---
