[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Let's start by opening up `nsfg` and loading (and cleaning) the data. As it turns out, having NaN's in the dataset will make finding Spearman & Pearson's correlation coefficients hard. 

```python
import nsfg
import thinkstats2
import thinkplot
raw_df = nsfg.ReadFemPreg()
df = raw_df.dropna(subset=['totalwgt_lb', 'agepreg'])
```
To get a scatter plot:
```python
thinkplot.Scatter(weights, ages)
thinkplot.show(xlabel='Baby\'s Weight (lbs.)', ylabel='Mother\'s Age')
```
![Scatter Plot of Baby's Weight vs. Mother's Age]()

Then, calculate the Pearson & Spearman correlation coefficients, respectively:

```python
thinkstats2.Corr(weights, ages)
thinkstats2.SpearmanCorr(weights, ages)
```
These return `0.0688` and `0.0946` respectively. Neither indicate a linear relationship between the variables. Given that the plot is roughly a flat line (or a bit of an oval), it's also apparent that there is no non-linear relationship in these values.
