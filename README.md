# Python Exercises

This repository contains the exercises from https://github.com/exercism/python
providing small and well-defined problems complete with tests and solutions.
The excercises are mostly unchanged, this repo exists only to make using them
as straightforward as possible. You don't need to install anything other than
Python.

## Choosing an exercise

To select an exercise you can use this [list](difficulties.md) where they are
ordered very roughly by difficulty. Just browse through the exercises and read
the descriptions until you find a problem which interests you.

## Get started

* Clone the repository
    ```
    git clone git@github.com:Alexander-N/python-exercises.git
    ```
    Alternatively you can download the code from
    https://github.com/Alexander-N/python-exercises/archive/master.zip

* Let's say you select `hello-world`. Change into the directory of your exercise
   ```
   cd python-exercises/exercises/hello-world
   ```
* Edit `hello_world.py` to solve the exercise. Look at README.md and test.py
   to find out what to do.
* Run the tests with
   ```
   python3 test.py
   ```
* Compare your solution to the one in `solution.py`
* You can make a pull request to share your solution.

## Tips
For a better testing experience, use
[pytest](https://docs.pytest.org/). If you don't want to use a virtualenv, you
can install it globally
```
sudo pip3 install pytest
```
Run the tests with 
```
python3 -m pytest test.py
```
Add the `-x` option to stop running tests on first failure.
