[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

For this exercise, I modified my existing `hypothesis` file and added some new wording to `RunTests()`. The added tests examine whether the birth weight and pregnancy lenghts vary significantly from first children to other children. They also seek to determine whether the resample or permutation models return different approximations for the null hypothesis.

Next, here's the class `DiffMeansResample` that I wrote and added to `hypothesis`

```python
class DiffMeansResample(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        data = thinkstats2.Resample(self.pool, n), thinkstats2.Resample(self.pool, m)
        return data
```
In `RunTests()`, I added the following to the existing test:

```python
# resample                                                                    
ht = DiffMeansResample(data)
p_value = ht.PValue(iters=1000)
print('means resample two-sided')
PrintTest(p_value, ht)
```
So that whenever `RunTests` was called, both forms of the null hypothesis would be tested. This returned:
```
prglngth
means permute two-sided
p-value = 0.178
actual = 0.0780372667775
ts max = 0.200182479001
means resample two-sided
p-value = 0.165
actual = 0.0780372667775
ts max = 0.184309916631

birth weight
means permute two-sided
p-value = 0.0
actual = 0.124761184535
ts max = 0.121272219846
means resample two-sided
p-value = 0.0
actual = 0.124761184535
ts max = 0.0943677846402
```

As you can see, the method doesn't *really* make a difference. That's not entirely surprising, as either simulation of the null hypothesis leads us to a situation where the elements are randomized into two distinct bins, which (in theory) should be equivalent in terms of mean, std, etc. The small fluctuations are likely a result of the random elements at play here, not any real difference in the methodology.
