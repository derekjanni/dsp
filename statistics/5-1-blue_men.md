[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Let's start by setting up a scipy normal distribution. Notice that `178cm = 70.787in` and `7.7cm = 3.0315in`:

```python
import scipy.stats
dist = scipy.stats.norm(70.0787, 3.0315)
```

We now have a good model for the heights of men, in inches, in the United States. We want to know what percentage of men fall between the heights of 70 inches and 73 inches, or 5'10" and 6'1". To do this, we use the CDF to find the probability of picking a man with height less than or equal to the given number. As we would expect:

```python
dist.cdf(70.787) 
```
Returns a value of `0.5`, confirming the fact that exactly half of any normal distribution has a value less than the mean. Thus, the percentage of men in between the two bounds is:

```python
dist.cdf(73) - dist.cdf(70)
```

Running that line of code tells us that about `33.27%` of US men fall between these heights; thus, we have the percentage of American men eligible to join Blue Man Group.
