[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

We want a vector that represents the actual number of children under the age of 18 in households - we will use this to generate a PMF.

```python
import chap01soln
import thinkplot
resp = chap01soln.ReadFemResp()
num = resp['numkdhh']
pmf = thinkstats2.Pmf(num, label = 'actual')
```

Now, lets see what the PMF looks like

```python
thinkplot.Pmfs([pmf])
thinkplot.show()
```

![PMF of the Actual Distribution of children under the age of 18 in the household](http://i.imgur.com/oSg7MJX.png)



