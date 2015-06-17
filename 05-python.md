# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Both are sequences of elements, but lists are mutable where tuples are not. Tuples work well as keys in a dictionary because it's not possible to build a dictionary where a list is the key in a dictionary, this returns a TypeError: unhashable type: 'list'. An example of using a tuple as dictionary keys would be associating (x,y) coordinates as keys with values that are obtained by plugging the tuple into some multivariate function.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Both are collections of elements, but sets don't include duplicates and lack internal order. A list is good for situations where you need order: if you had a group of people running a race you'd want a list to represent the order in which they finished because order is important to you. However, a set would be more useful for other pursuits. For instance, say you spend a day walking around Portland taking down names of people you see. Putting the names in a list would be fine, but you'd almost surely get a lot of duplicates - eating up your limited memory. Also, keeping them in order wouldn't really do you any good, since you're not worried about the order in which you met people. At the end of the day, you'd have a collection of names and you could easily ask yourself "Hmm, did I meet a James today?"  

>Since set elements are hashed, looking up a name in a collection like this is a constant time operation (e.g. ```James in set = True```). By comparison, lists are more of a hassle, because the worst case scenario (you didn't meet a James at all) would require you looking at each of the names in your list and asking "Is this James? No. Is this James? No." and so on. Searching through this list would be a linear time operation, which would be a huge pain if you met 30,000 people that day.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>`lambda` is an operator that defines a function. For inststance, you can use a lambda function to pass in an array of values quickly and cleanly instead of defining a function to do the work. Example:

>```f = lambda x, y : y*2 + x**2 + 5``` - this makes a multivariate function, f, that varies according to whatever's in x and y.

>```dogs = [('sparky', 'black lab', 2), ('beelzebub', 'corgie', 5), ('bracelet', 'german shepard', 6)]
> If you wanted ot sort the dog tuples by their breed, you could use
>```sorted(dogs, key=lambda dog: dog[1])``` 

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>In math class, we want to use set builder notation to denote things like "x | n in N & x = 2n". This set of includes all of th natural even numbers. Conveniently, Python's list comphension tricks are a lot like this! For example:

>`x = [2*x for x in range(10)]`
>`x = map(lambda w: 2*w, range(10))`

>The first is a straightforward list comphension, the second does the same taske by using `map`. The fun part about list comprehensions is that you can use them to do way more than just build sets (more to come soon).

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
