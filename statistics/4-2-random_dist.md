[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

First, lets generate 1000 random numbers from `random` and put them into an array.

```python
a = []
for i in range(0, 1000)
  a.append(random.random())
```

Now, the PMF of these numbers:
```python
pmf = thinkstats2.Pmf(a, label='random numbers')
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='random number', ylabel ='PMF')
```
![PMF of Random Numbers](http://i.imgur.com/4b4NRXd.png)

And the CDF:
```python
cdf = thinkstats2.Cdf(a, label='random numbers')
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='random number', ylabel ='CDF')
```
![CDF of Random Numbers](http://i.imgur.com/iMFyrfr.png)

This is what we'd expect of a uniform random distribution: a flat, homogeneous PMF (indicating that there is an equal chance of pulling any X from this distribution) and an upward-sloping CDF (indicating that each incremental step in X relates to a corresponding increase in the CDF).

