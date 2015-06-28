[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

First, import and clean data for the test:
```python
import nsfg
import thinkstats2
import thinkplot
raw_df = nsfg.ReadFemPreg()
df = raw_df.dropna(subset=['totalwgt_lb', 'agepreg'])
ages = df.agepreg
weights = df.totalwgt_lb
data = ages, weights
```

Next, here's the class `DiffMeansResample` that I wrote and added to `thinkstats2`

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

    def Resample(xs):
        return np.random.choice(xs, len(xs), replace=True)

    def RunModel(self):
	      data = Resample(group1), Resample(group2)
	      return data
```
