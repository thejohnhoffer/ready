### Get set up

- Install [bash][bash] if on Windows
- Install [git][git] if on Mac or Linux
- Install [conda][conda] on Windows, Mac, or Linux

[bash]: https://github.com/thejohnhoffer/ready/wiki/bash-git-python#bash
[git]: https://github.com/thejohnhoffer/ready/wiki/bash-git-python#git
[conda]: https://github.com/thejohnhoffer/ready/wiki/bash-git-python#conda

### Get the code

In a `bash` prompt, type this:

```
git clone https://github.com/thejohnhoffer/ready.git
cd ready
```

Now you're in a folder that contains this project.


### Notes

`$` means you're in a `bash` prompt, like this:

```
laptop:ready John$
```

In `bash`, you type `ipython` to enter `ipython`. Something like `In [1]:` means you're in an `ipython` prompt. You can type `exit()` to leave `ipython`. Then you'll be returned to your `bash` prompt. You can also just close the window or `bash` application.

You'll notice `ipython` has colors to help you remember the meaning of symbols:
![ipython](ipython.png)

In this image:
- Green:
    - numbers like `8`
    - your input prompt `In [1]:`
    - standard python [functions](https://docs.python.org/3/library/functions.html) like `str`
    - standard python [keywords](https://github.com/thejohnhoffer/ready/wiki/keywords) like `def`, and `return`
- Red: your output `Out [1]:`
- Orange: strings like `')'`
- Blue: function defintions like the first mention of `make_smile`
- Gray:
    - variables like `eyes`, `mouth`, and the second mention of `make_smile`
    - symbols like `:`, `(`, `)`, `,` and `+`

### Run the code from bash

One option is to run python directly in a `bash` prompt like this:

```
python test.py
```


### Run the code from ipython

Or, you can run python interactively. In a `bash` prompt, type this:

```
ipython
```

Then, from the `ipython` prompt, type this:

```
In [1]: import read

In [2]: read.files('single_spaced.txt', 'double_spaced.txt')
``` 

If you open [test.py](test.py), you'll notice these two lines.

### What is happening?

When you type `import read`, python finds [the file](https://github.com/thejohnhoffer/ready/blob/master/read.py) called `read.py`. After python finds that file, Then you can type `read.files` to find [the function](https://github.com/thejohnhoffer/ready/blob/master/read.py#L11) called `files` in `read.py`. You can call this function on two filenames `a` and `b` by typing `read.files(a ,b)`.
