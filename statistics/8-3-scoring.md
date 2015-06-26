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
    "Implementation of 'waiting time' until next event."
    "Proof by Knuth in The Art of Computer Programming v2"
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
    #print('goals scored this game: ' + str(goals))                               
    return(goals)

def SimMany(lam, n, rep):
    obs = []
    for i in range(rep):
        obs.append(Simulate(lam))

    actual = lam
    rmse = RMSE(obs, actual)
    me = MeanError(obs, actual)
    cdf = thinkstats2.Cdf(obs)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    thinkplot.Plot(obs)
    print("Standard Error: " + str(rmse))
    print("Mean Error: " + str(me))
    thinkplot.show(xlabel='Iteration', ylabel='Sample Value of Goals per Game')
```
---
