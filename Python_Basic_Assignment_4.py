"""
ASSIGNMENT 4 SOLUTIONS :

Q1. What exactly is []?
Ans : The empty list represented by [] is a list that contains no items.
"""
#Example of empty list
a = []
print("Values of a: ", a)
#This would give me an empty list a=[]

"""
Q2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
(Assume [2,4,6,8,10] are in a spam).
Ans : spam[2] = 'hello' (as the list will start from index zero)
"""
#Example
spam = [2,4,6,8,10]
spam[2]='hello'
print(spam)

"""
LET'S PRETEND THE SPAM INCLUDES THE LIST ['a','b','c','d'] FOR THE NEXT THREE QUERIES.

Q3. What is the value of spam[int(int('3'*2)/11)]?

Ans : The value of spam[int(int('3'*)/11)] is 'd'. 
('3'*2 is the string '3', which is passed to int() before being divided by 11.
This eventually evaluates to 3, spam[3] is equal to d.)
"""
spam = ['a','b','c','d']
print("spam[int(int('3'*)/11)])->", spam[int(int('3'*2)//11)])

"""
Q4. What is the value of spam[-1]?
Ans : The value of spam[-1] is 'd'.
(negative index '-1' returns the last item from the list)
"""
spam = ['a','b','c','d']
print(spam[-1]) #d


"""
Q5. What is the value of spam[:2]?
Ans : The value of spam[:2] is ['a','b'].
(spam[:2] prints the value of spam from 0 to 2 excluding 2)
"""
spam = ['a','b','c','d']
print(spam[:2])

"""
LET'S PRETEND BACON HAS THE LIST [3.14, 'cat', 11,'cat', TRUE] FOR THE NEXT THREE QUESTIONS.

Q6. What is the value of bacon.index('cat')?
Ans : The value of bacon.index('cat') is 1.
(Index returns the first occurrence of a value in a list.)
"""
bacon = [3.14, 'cat', 11,'cat', True]
print(bacon.index('cat'))
#1

"""
Q7. How does bacon.append(99) change the look of the list value in bacon?

Ans : The append method adds the new element to the end of the list.
"""
bacon = [3.14, 'cat', 11,'cat', True]
bacon.append(99)
print(bacon)
#bacon = [3.14, 'cat', 11, 'cat', True, 99]

"""
Q8. How does bacon.remove('cat') change the look of the list in bacon?

Ans : bacon.remove('cat') will remove the first occurrence of the element in the list.
"""
bacon = [3.14, 'cat', 11,'cat', True]
bacon.remove('cat')
print(bacon)
#[3.14, 11, 'cat', True]

"""
Q9. What are the list concatenation and list replication operators?

Ans : The operators for list concatenation is +, it adds the elements to list from another list. While, operator for 
replication is *, it gives the same elements from the list for how many output you want.
"""
list1=['r', 'u', 'lu']
list2 = ['y', 'i', 'swu', 'ro']
print(list1 + list2) # concatenation
print(list1*2)#replication
#['r', 'u', 'lu', 'y', 'i', 'swu', 'ro'] added the list2 values to list1
#['r', 'u', 'lu', 'r', 'u', 'lu'] added the same value of list1 twice

"""
Q10. What is difference between the list methods append() and insert()?

Ans : The append() method will add values only to the end of the list, whereas, insert() can add the values anywhere 
inside the list.
"""
list = [1,2,3,4,5,6]
list.append('append')
print(list)
#[1, 2, 3, 4, 5, 6, 'append'] appended to the end of the list
list2=[1,2,3,4,23,454]
list2.insert(3,'insert')
print(list2)
#[1, 2, 3, 'insert', 4, 23, 454] inserted the given value

"""
Q11. What are the two methods for removing items from a list?

Ans :  The two methods for removing items from a list are the del and remove() method.
"""
#Example
list=[1,2,3,4,5,6,7]
del list[4]
print(list)
#[1, 2, 3, 4, 6, 7] the item in index 4 has been removed
list = [1,2,3,4,5,6,7]
list.remove(3)
print(list)
#[1, 2, 4, 5, 6, 7] the item in index 3 has been removed

"""
Q12. Describe how list values and string values are identical.

Ans : The values in a list and string are identical because:
1. Both list and string can be passed to len() function.
2. Both have indexes and slices, use in for loops.
3. Both can be concatenated or replicated.
4. Both can be used with 'in' and 'not in' operators.
"""


"""
Q13. What's the difference between tuples and list?

Ans : Lists are Mutable, Indexable and Sliceable, values can be added, removed or changed.
Tuples are also Indexable and Sliceable but are Immutable, values cannot be changed.
Tuples are represented using parentheses () while lists are represented using [].

"""
list=[1,2,3,54,3]
tuples=(1,2,3,4)
print(list)
print(tuples)

"""
Q14. How do you type a tuple value that only contains the integer 42? 
Ans : Tuple value contain only 42 will be typed as (42,). 
(The trailing comma represents the tuple value as it will be considered int without it.)

"""
#Example
tuple = (42)
tuple1 = (42,)
print(tuple,(type(tuple)))
print(tuple1, (type(tuple1)))

"""
Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?

Ans : The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa.
"""

"""
Q16.Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

Ans : Variables that "contain" list values are not necessarily lists themselves. They contain references to the list 
values.
"""

"""

Q17. How do you distinguish between copy.copy() and copy.deepcopy()?

Ans : The copy.copy() function will do a shallow copy of a list, while copy.deepcopy() function will do a deep copy of 
a list. 
Only copy.deepcopy() will duplicate any lists inside the list.

"""
import copy
l1 = [1,2,3,4,[2,34],3,4]
l2 = copy.copy(l1) #using copy for shallow copy
l3= copy.deepcopy(l1)# using deepcopy for deep copy

