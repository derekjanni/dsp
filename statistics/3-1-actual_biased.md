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
thinkplot.Show(xlabel='Number of Children < Age 18 in the Household', ylabel='PMF')
```

![PMF of the Actual Distribution of children under the age of 18 in the household](http://i.imgur.com/iJQfz22.png)

Well, that image is a bit large, but it gets the point across. 

Now we compute the biased distribution (the same way that's outlined in the book):

```python
def BiasPmf(pmf, label):
     new_pmf = pmf.Copy(label=label)
     for x, p in pmf.Items():
         new_pmf.Mult(x, x)
     new_pmf.Normalize()
     return new_pmf
bias = BiasPmf(pmf, label='observed')
```
And plot both histograms at once:

```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, bias])
thinkplot.Show(xlabel='Number of Children < Age 18 in the Household', ylabel='PMF')
```
![PMF of Actual vs. Biased Distribution of children under the age of 18 in the household](http://i.imgur.com/V6nhyNA.png)

There's the classic "you don't know what you don't know" paradox played out in actual numbers. The moral of the story: when you're collecting data you have to make sure your sample is actually representative of the population in question. In the case of the biased distribution, asking the children immediately creates a problem - if there are no children in the household, then these households vanish from the dataset entirely!
