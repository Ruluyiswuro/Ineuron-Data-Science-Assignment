"""1.What are the two values of the Boolean data type? How do you write them?

Ans : Two values of the boolean data types are True and False. We have to use uppercase
letter T and F with the rest in lowercase. The type( of both True and False is bool. The
bool is built in, meaning it's always available on Python and doesn't need to be imported.
However, the name itself isn't a keyword in the language.
"""
a = True
b= False
print(a,type(a))
print(b,type(b))

"""
2. What are the three different types of Boolean operators?

Ans : Boolean operators form the basis of mathematical sets and database logic. They 
connect our search words together to either narrow our set of results. The three different
types of Boolean operators in Python are :
are, and, and not.
"""
#Example
a = 100
b = 150
print(a>50 and b>100)
print(a>20 or b>100)
print(not(a>11))

"""
3. Make a list of each Boolean operator's truth tables(i.e. every possible combination
of Boolean values for the operator and what it evaluate).
Ans:
The truth table for the Boolean operator's truth table is given below:

* Truth Table for 'and' operator:
    True and True = True
    True and False = False
    False and True = False
    False and False = False
    
*Truth table for 'or' operator:
    True or True = True
    True or False = True 
    False or True = True
    False or False = False
    
*Truth table for 'not' operator :
    True not = False
    False not = True
"""

"""
4. What are the values of the following expressions?
(5>4) and (3==5)
not (5>4)
(5>4) or (3==5)
not ((5>4) or (3==5))
(True and True) and (True===False)
(not False) or (not True)
"""
print((5>4) and (3==5))
#Gives False
print(not (5>4))
#Gives False
print((5>4) or (3==5))
#Gives True
print(not ((5>4) or (3==5)))
#Gives False
print((True and True) and (True==False))
#Gives False
print((not False) or (not True))
#Gives True

"""
5. What are thee six comparison operators

Ans : The six comparison operators in Python are :
==, !=, <, >, <=, and =>
"""
"""
6. How do you tell the difference between the equal to and assignment operators? 
Describe a condition and when you would use one.

Ans : To tell the difference between equal to and value assignment operator,
Python uses two equals(==) for equal to and only one (=) for assigning a value in a variable.
"""
a = 10
b = 10#assigning a value
if b==a: # comparison of value using ==
    print(b)

"""7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')
Ans : In Python, code block to a collection of code that is  in the same block or indent.
This is most commonly found in classes, functions and loops.
"""

spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
#This gives ham , spam, and spam

"""
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in 
spam, and prints Greetings! if anything else is stored in spam.

"""
def Spam(spam):
    if spam == 1:
        print('Hello')
    elif spam==2:
        print('Howdy')
    else:
        print('Greetings!')

Spam(1)
Spam(2)
Spam(3)

"""
9.If your programme is stuck in an endless loop, what keys you’ll press?

Ans :  To stop a stuck program in an infinite loop, the key we'll use is Ctrl + c.
If it doesn't work, we can interrupt the kernel or restart the kernel.
"""

"""
10. How can you tell the difference between break and continue?

Ans : The break statement will move the execution outside of the loop if the break condition is satisfied,
whereas, continue statement will move the execution to the start of the loop.
"""
#Example to use break statement :
for val in "ineuron":
    if val == "r":
        break
    print(val)
print("Reached limit")
#Example to use continnue statement :
for val in "ineuron":
    if val == "r":
        continue
    print(val)
print("Reached limit")

"""
11. In a for loop, what is the difference between range(10), range(0,10) and range (0,10,1)?

Ans : Ans: The Differences are as follows:

The range(10) call range from 0 to 9 (but not include 10)
The range (0,10) explicitly tells the loop to start at 0
The range(0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration
"""
#printing a number for range(10)
for i in range(10):
    print(i, end=" ")
print()
#for range(0,10)
for i in range(0,10):
    print(i, end=" ")
print()
#for range(0,10,1)
for i in range(0,10,1):
    print(i, end=" ")
print()

"""
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program 
that prints the numbers 1 rto 10 using a while loop.
Ans :
"""
print("Using for loop : ")
for i in range(1,11):
    print(i, end=" ")
print()

i=1
print("Using while loop : ")
while i<=10:
    print(i, end =" ")
    i+=1

"""
13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

Ans: The function name bacon () inside a module named spam can be called using spam.bacon()
"""