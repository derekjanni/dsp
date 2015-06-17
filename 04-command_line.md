# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>From the crash course:

>`pwd`: print working directory 

>`hostname`: my computer's network name

>`mkdir`: make directory

>`cd`: change directory

>`ls`: list directory

>`rmdir`: remove directory

>`pushd`: push directory (onto a stack of sorts). pretty neat command for jumping around in your directories

>`popd`: pop directory (from the stack). counterpart to `pushd`

>`cp`: copy a file or directory. syntax: cp -r from_directory to_directory to move the directory and all of its contents.

>`mv`: move a file or directory. similar to cp in terms of syntax.

>`less`: page through a file

>`cat`: print the whole file

>`xargs`: execute arguments. good "divide and conquer" tactic when you're trying to feed too many args into another command. ex: "`rm` /path/*" might fail when working with lots of files in /path, but "`find` /path -type f -print | `xargs` `rm`" can save the day

>`find`: find files

>`grep`: find things inside files

>`man`: read a manual page

>`apropos`: find what man page is appropriate

>`env`: look at your environment

>`echo`: print some arguments. classic example "`echo` "hello world"

>`export`: export/set a new environment variable

`>exit`:exit the shell

>`sudo`: become super user root. "super user do". don't use this unless you're really sure about the arguments: if they containt malicious code you are basically giving that code a free pass on your system.

>`chmod`: change permission modifiers (rwx). ex: -rw-rw-r--  joe  acctg  coolstorybrah.txt (which you get from ls -l) lists rwx permissions for the user, group and others. chmod uog=rwx coolstorybrah.txt would give everyone permission to read/write/execute the file.

>`chown`: change ownership. Useful for hacking Kindle Fire, as I recall.
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>`ls`: lists the files in a directory. 

>`ls -a`: "-all" - lists all files including hidden ones starting with "." 

>`ls -l`: displays "long format" (whether it's a file/direct, permissions, owner, group, size, last-modified date and filename)

>`ls -lh`: exactly like `ls-l` but file size is listed in "human readable" formats like Kb/Mb abbreviated as K/M

---


---

What does `xargs` do? Give an example of how to use it.

>`xargs` is "execute arguments" - you can use it to pipe output of one unix command as input for another. Here's a really basic example: say you want to go through the python files in thinkstats2/code and find which of them use scipy directly. Instead of running two commands, you could just use find | xargs grep to filter the files:


```find *py | xargs grep "import scipy"```

this returns:

```mystery.py:import scipy.stats```

```normal.py:import scipy.stats```

```thinkstats2.py:import scipy```

>Pretty neat command, will definitely use.

---
