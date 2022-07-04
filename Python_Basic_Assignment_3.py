"""
ASSIGNMENT 3 PYTHON BASICS
Q1. Why are functions advantageous to have in your programs?

Ans : There are many advantages of Python as it provides high level readability and is interpreted.
Python is simple and easy to learn or read as it resembles the English language. Python is also free and open source.
It is portable and extensible and is supported by all the platforms of the industries.
Python also supports Object-Oriented Programming which permits polymorphism and inheritance.
Python also has libraries that helps in image recognition and computer vision.
Python is used widely in small or large online and offline projects. Python can handle a large
amount of data and supports parallel computing. The functions in Python reduces duplication
codes and advantage of function is code reusability.
"""

"""
Q2. When does the code in a function run:when it's specified or when it's called?

Ans : The code in a function executes when the function is called and not when it's specified.
When a functions is called, the program leaves the current section of code and begins to execute
the first line inside the function.
"""
#Example :
def function(full_name):
    print(full_name + " is learning Data Science from Ineuron.")

function("Ruluyi Swuro")

"""
Q3. What statement creates a function?

Ans: The statement 'def' creates a function.
"""
#Example :
def function(full_name):
    print(full_name + " is learning Data Science from Ineuron.")

function("Ruluyi Swuro")

"""
Q4. What is the difference between a function and a function call?

Ans : A function is a block of code that does a particular operation and returns a result. 
It usually accepts inputs as parameters and returns a result. A  function call is the code used to pass 
control to a function.
"""
#Function
def sqrt(a):
    return a*a
#Function call
print(sqrt(2))

"""
Q5. How many global copes are there in a Python program? How many are local scopes?

Ans : There is one global scope, and a local scope is created whenever a function is called.
A variable created inside a function belongs to the local scope of that function, abd can only
be used inside that function, whereas, a variable created in the main body of the Python code is a global
variable and belongs to the global scope.
"""
#Example of global scope
a = 100
def my_func():
    print(a)
my_func()
print(a)
#Example of local scope:
def my_func():
    a = 100
    def inner_func():
        print(a)
    inner_func()
my_func()

"""
Q6. What happens to variables in a local scope when the function call returns?

Ans : When a function returns, the local scope is destroyed and all the variables in it are forgotten.
A local variable becomes undefined after the function call completes.
"""

"""
Q7. What is the concept of a return value? Is it possible to have a return value in an expression?

Ans : The Python return statement is a key component of functions and methods.
We can use the return statement to make functions send Python objects back to the caller code.
These objects are known as the function's return value. A return value is the vale that a function call 
evaluates to.
        A return value can be used as a part of an expression.

"""

"""
Q8. If a function does not have a return statement, what is the return value of a call to that function?

Ans : If there is no return statement for a function, it's return value is None. The function 
always returns None if explicit return is not written.

Q9. How do you make a function variable refer to the global variable?

Ans : A global statement will force a variable in a function to refer to the global variable. If you want 
to refer global variable in a function, you can use the global keyword to declare which
variables are global.

Q10. What is the dat type of None?
Ans : The data type of None is NoneType.

Q11. What does the sentence import areallyourpetsnamederic do?
Ans : The sentence import areallyourpetsnamederic will import the module named areallyourpetsnamederic.

Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans : The function can be called spam.bacon().

Q13. What can you do to save a programme from crashing if it encounters an error?
Ans : We can place the line of code that might cause an error in a try clause and except block 
to handle the error.
"""
#Example
try:
    x=200
    print(x + 2)
except :
    print("An error occurred")

"""
Q14. What is the purpose of the try clause? What is the purpose of the except clause?

Ans : We can write a code that could cause an error inside try clause. The code that execute if an error 
occurred goes inside the except clause.
"""
#Example

x = 100
try:
    print(x)
except NameError:
    print("Value not defined")
except :
    print("Invalid operation")
