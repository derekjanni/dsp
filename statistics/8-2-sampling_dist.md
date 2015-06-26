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

Then, from the command line environment, it's as simple as running the estimate function and observing the output:

Simulate a 10-size sample 1000 times:
```python
estimate.Exp(10, 1000)
```
`Standard Error: 0.856410495377`
`Confidence Interval: (1.2291766987664456, 3.8586455636150165)`
![Sampling Distribution for X~Exp(2) with 1000 samples of size n=10 ](http://i.imgur.com/EWqzJUX.png)

Simulate a 50-size sample 1000 times
```python
estimate.Exp(50, 1000) 
```
`Standard Error: 0.305947978247`
`Confidence Interval: (1.5939562446187574, 2.5843674082263912)`
![Sampling Distribution for X~Exp(2) with 1000 samples of size n=50](http://i.imgur.com/ei4fRyj.png)

Simulate a 250-size sample 1000 times
```python
estimate.Exp(250, 1000)
```
`Standard Error: 0.12486248451`
`Confidence Interval: (1.8029704159502067, 2.2106111033128997)`
![Sampling Distribution for X~Exp(2) with 1000 samples of size n=250](http://i.imgur.com/ye2kIPk.png)


If we plot `n` vs. `Standard Error` we get:
![Effect of Increasing Sample Size on Standard Error](http://i.imgur.com/0Fmdd1j.png)

So, in summary, since we're using a unbiased estimator we see that the standard error decreases with increasing sample sizes. To save space with all of these graphs, here's a more complete view that shows the convergence more clearly:

![Effect of Increasing Sample Size on Standard Error](http://i.imgur.com/Pewy5lP.png)

Of course, such a plot is a little unnecessary, as we could (and should) just *prove* that as `n` increases, `standard error` decreases. Such a proof is easy:

Given that SE is defined as:
![Definition of Standard Error](https://upload.wikimedia.org/math/b/b/2/bb234d9a63401082dbd197c430fd35c9.png)
and
![Definition of "s"](https://upload.wikimedia.org/math/b/2/6/b26a881372bbca2d567df98c6ef84418.png)

It's easy to see that as `n` increases, both `s` and `standard error` must decrease toward zero, so long as the the population mean is finite!
