[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

For this exercise, I created a file called `estimate.py` to hold the helper functions for sampling. Below is the complete code:

```python
import thinkstats2
import thinkplot
import math
import random
import numpy as np

def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.         
                                                                                
    estimate: sequence of numbers                                               
    actual: actual value                                                        
                                                                                
    returns: float RMSE                                                         
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
def Exp(n, m):
    """Prints the MSE and .                                                       
                                                                                  
    n: sample size                                                                
    m: number of iterations                                                       
    """
    lam = 2
    means = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)

    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    thinkplot.Plot(means)
    print('Standard Error: ' + str(RMSE(means)))
    print('Confidence Interval: '+ str(ci))
    thinkplot.show(xlabel='Iteration', ylabel='Sample Value of L')
```

Then, from the command line, it's as simple as running
```python
estimate.Exp(10, 1000) #simulate a 10-size sampling 1000 times
estimate.Exp(50, 1000) #simulate a 50-size sampling 1000 times
estimate.Exp(250, 1000) #simulate a 250-sieze sampling 1000 times
```

more to come soon
