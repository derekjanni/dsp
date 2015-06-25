[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Calculate Cohen's d by loading the data into Python and sending it to the proper thinkstats2 function. 

```python
import nsfg
import thinkstats2
df = nsfg.ReadFemPreg()
firsts = df[df.birthord==1]
others = df[df.birthord>1]
fwgts = firsts.totalwgt_lb
owgts = others.totalwgt_lb
thinkstats2.CohenEffectSize(fwgts, owgts)
```

This code block returns a value of ~ -0.08867.

If we compare this to the output for pregnancy length:

```python
flen = firsts.prglngth
olen = others.prglngth
thinkstats2.CohenEffectSize(flen, olen)
```

For which the output is ~ 0.02888.

Neither of these effect sizes are very large, but the `d` score for birthweights between first children and those that follow them is slightly negative (i.e. "others" are slightly heavier) while the `d` score for pregnancy lengths indicates that first pregancies are slightly longer than "others".
