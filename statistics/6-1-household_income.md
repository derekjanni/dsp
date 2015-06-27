[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

Let's start by importing the data and the functionality used to sample from it:

```python
import hinc
import hinc2
df = hinc2.ReadData()
sample = InterpolateSample(df)
```
For some reason our author decided that it was a good idea to take the log of everything in the dataset! Let's fix that and get some numbers we can actually interpret:
```python
income = [10**i for in sample]
```
Alright, now that that's out of the way, we can easily make a CDF and start deducing some facts about this distribution!
```python
cdf = thinkstats2.Cdf(income)
```
Lets compare the median & mean:
```python
>>> thinkstats2.Mean(income)
74278.707531187203
>>> thinkstats2.Median(income)
51226.454478940461
```
As expected, the mean far exceeds the median. What about skewness?
```python
>>> thinkstats2.Skewness(income)
4.9499202444295829
>>> thinkstats2.PearsonMedianSkewness(income)
0.7361258019141782
```
Well, there you have it, the "famously skewed" income data shows a rather large, positive 3rd standardized moment - indicating that the data are right-skewed. For further proof, consider:
```python
>>> cdf[thinkstats2.Mean(income)]
0.66000587956687196
```
Which tells us that about 66% of people rank below the mean income - a further indication of positive skew. If we are to raise the upper bound, we can observe how even higher incomes in the sample can affect skew:
```python
sample = hinc2.InterpolateSample(df, log_upper=7) #adds people earning up to $10 million per year to the sample
income = [10**i for i in sample]
cdf = thinkstats2.Cdf(income)
```
Now if we look at the different numbers, we see something interesting:
```python
>>> thinkstats2.Mean(income)
124267.39722164697
>>> thinkstats2.Median(income)
51226.454478940461
>>> thinkstats2.Skewness(income)
11.603690267537793
>>> thinkstats2.PearsonMedianSkewness(income)
0.39156450927742087
```
As expected, the difference in mean and median expanded even further, and the skewness coefficient more than doubled! However, oddly enough, Pearson's Skewness Coefficient actually *shrunk*. Why is that? When we investigate by renaming the two samples according to their (normal) skew:

```python
>>> thinkstats2.Std(less_skewed_income)
93946.92996347824
>>> thinkstats2.Std(more_skewed_income)
559608.5013743464
```
We see a huge difference in standard deviation: which is a the reason why the Pearson Skewness Coefficient does a poor job here. It also explains why this summary statistic is only infrequently *mentioned* in Stats books, it's lack of robustness earns it a space in the sparsely populated bin of "Stats terms that even Statisticians don't care about". Recall the formula for Pearson's Skewness Coefficient: 3 (mean - median) / (standard deviation). The difference in mean and median, while larger for the second interpolated data set, is no comparison for the nearly sixfold increase in standard deviation. 
