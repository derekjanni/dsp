[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

Importing data for test
```python
import nsfg
import thinkstats2
import thinkplot
raw_df = nsfg.ReadFemPreg()
df = raw_df.dropna(subset=['totalwgt_lb', 'agepreg'])
```
