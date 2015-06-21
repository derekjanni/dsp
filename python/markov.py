#!/usr/bin/env python

__author__ = 'derekjanni'
import random
import sys

# global vars
fname = sys.argv[1]
wordcount = int(sys.argv[2])

# import file from cmd line args
f = open(fname,"r")
corpus = f.read().lower()
f.close()

# clean & convert data into an easy to use list
words = corpus.replace("\n", " ").replace("(", "").replace(")", "").split(" ")
words = [x for x in words if x]

# create map that relates every word in the document to the words that follow it
map = {x: [] for x in words}
for i in range(len(words) - 1):
    map[words[i]].append(words[i+1])

# generate chain based on above list
chain = [random.choice(map.keys())]
j = 0
while j < wordcount:
    try:
        last = chain[j]
        chain.append(random.choice(map[last]))
    except IndexError:
        #error handling for the chance that you pick the last word in the text, which won't have a "next" element
        pass
    j += 1
chain_as_string = " ".join(chain)
chain_as_string += '.' #period for style
print(chain_as_string)
