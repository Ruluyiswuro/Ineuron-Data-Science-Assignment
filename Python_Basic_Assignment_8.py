"""
PYTHON BASIC ASSIGNMENT NO 8

Q1. Is the Python Standard Library included with PyInputPlus?

Ans : PyInputPlus is not a part of Python Standard Library, it needs to be installed explicitly using the command
pip install PyInputPlus.

 Q2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

 Ans: PyInputPlus is commonly imported with import pyinputplus as pypi so that you can enter a shorter name (pypi)
 instead of calling the whole module's name when calling the function.

"""

"""
Q3. How do you distinguish between inputInt() and InputFloat()?
Ans :  inputInt() function accepts an integer value, it also takes additional parameters such as min, max, greaterThan
and lessThan parameters for bounds and always return an int.

Whereas, inputFloat() function accepts a floating-point numeric value, it also takes additional min, max, greaterThan
and lessThan parameters and always return a float.
"""

"""
Q4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

Ans: PyInputPlus module provided a function called inputInt() which only returns integer values. In order to restrict
the input between 0 and 99, we use parameters like min and max to ensure that the user enter the values between the 
defined range only. 
"""

"""
Q5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

Ans : We can use allowRegexes and blockRegexes keyword arguments to take list of regular expression strings to determine
what the pyinputplus functions will reject or accept valid input.
"""

"""
Q6. If a blank input is entered three times, what does inputStr(limit=3') do?

Ans : The statement inputStr(limit=3) will throw two exceptions ValidationException and RetryLimitException. The first 
exception is thrown because blank values are not allowed by inputStr() function by default. If we want to consider the 
blank values, we have to set blank = True. The second exception will occur because we have reached the max specified 
using the limit parameter. If we want to avoid the exception, we can use default parameter to return the default value 
when the max limit exceeded.

"""
"""
Q7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
Ans : Since the default parameter is set to hello, after a blank input is entered three times, the function will return 
the default value hello as a response instead of raising RetryLimitException.
"""