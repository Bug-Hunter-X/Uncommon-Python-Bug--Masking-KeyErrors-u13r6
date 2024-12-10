# Uncommon Python Bug: Masking KeyErrors

This repository demonstrates a subtle bug related to exception handling in Python.  The `bug.py` file shows how catching a `KeyError` and returning a default value (0) can mask the true nature of the problem. The `bugSolution.py` illustrates a more robust approach.

## The Problem
The original code handles `KeyError` exceptions by printing an error message and returning 0. This is problematic as it silently fails without providing useful information about the missing key.  The return value of 0 could be mistaken for a valid result.

## The Solution
The improved code in `bugSolution.py` shows several ways to deal with this error more effectively.  One is to raise a more informative exception, giving more context to the problem. Another is to use the `get` method of dictionaries to handle the potential missing key gracefully.