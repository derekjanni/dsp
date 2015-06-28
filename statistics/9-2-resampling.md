[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

For this exercise, I simply modified my existing `hypothesis` file and added some new tests to `RunTests()`. The added tests examine whether the birth weight and pregnancy lenghts vary significantly from first children to other children. They also seek to determine whether the resample or permutation models return different results for the same data.

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
	data = Resample(group1), Resample(group2)
	return data
```
In `ReplicateTests()`, I added to the existing tests:
```python
ht = hypothesis.DiffMeansResample(Data)
p = PValue()
```
Which returned:
```
prglngth
means permute two-sided
p-value = 0.0
actual = 0.164708338667
ts max = 0.141380631515
means resample two-sided
p-value = 0.509
actual = 0.164708338667
ts max = 0.338554835567

birth weight
means permute two-sided
p-value = 0.0
actual = 0.170870412946
ts max = 0.0734615805093
means resample two-sided
p-value = 0.536
actual = 0.170870412946
ts max = 0.251699817305
```
