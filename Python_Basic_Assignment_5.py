"""
Q1. What does an empty dictionary's code look like?

Ans: An empty dictionary code is often represented by two empty curly brackets d = {} or d = dict{}

"""
#example
emptyDict= {}
print("length : ", len(emptyDict), type(emptyDict))
#length :  0 <class 'dict'>

"""
Q2. What is the value of a dictionary value with the key 'foo' and the value 42?
Ans : Value of dictionary is given below:
"""
{'foo':42}


"""
Q3. What is the most significant distinction between a dictionary and a list?

Ans : Dictionaries are represented by {} where as listed are represented by []. The Items stored in a dictionary are 
Unordered , while the items in a list are ordered.

Lists are just like the arrays, declared in other languages. Lists need not be homogeneous always which makes it a most 
powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, 
and hence, they can be altered even after their creation.

Dictionary in Python on the other hand is an unordered collection of data values, used to store data values like a map, 
which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key-value is 
provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, 
whereas each key is separated by a ‘comma’.
"""
#Dictionary
Dict = {1:'Mike', 2: 'john', 3: 'Mary'}
print("Dictionary with the use of interger keys: ", Dict)
#Dictionary with the use of interger keys:  {1: 'Mike', 2: 'john', 3: 'Mary'}

#list
list = ["Howard", "John", "Michael"]
print("list containing multiple value : ")
print(list[0:2])
#list containing multiple value :
#['Howard', 'John']

"""
Q4. What happens if you try to access sparn['foo'] if sparn is {'bar':100}?
Ans: Trying to access sparn['foo'] from sparn={'bar':100} gives an error as KeyError: 'foo'.

"""
sparn={'bar':100}
sparn['foo']
#KeyError: 'foo'

"""
Q5: If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in
spam.keys()?
Ans : 
The operator checks whether a value exist as a key in the dictionary or not so, there's no difference.
"""
"""
Q6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in 
spam.values()?

Ans :  'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether 
there is a value 'cat' for one of the keys in spam.
"""

"""
Q7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

Ans : spam.setdefault('color', 'black')
"""

"""
Q8. How do you "pretty print" dictionary values using which module and function?

Ans : We can pretty print dictionary values using three different functions:

1. By using pprint() function of pprint module.
2. By using dumps() method of json module.
3. By using dumps() method if yaml module.
"""
dict= [
    {'Name': 'Michael', 'Student_ID': 122303, 'email_ID': 'michael5142@yahoo.net'}
]
import pprint
print(dict)
pprint.pprint(dict)
import json
dump = json.dumps(dict, indent = 1)
print(dump)
import yaml
dump = yaml.dump(dict)
print(dump)
#[{'Name': 'Michael', 'Student_ID': 122303, 'email_ID': 'michael5142@yahoo.net'}]
#[{'Name': 'Michael', 'Student_ID': 122303, 'email_ID': 'michael5142@yahoo.net'}]
#[
# {
#  "Name": "Michael",
#  "Student_ID": 122303,
#  "email_ID": "michael5142@yahoo.net"
# }
#]
#- Name: Michael
#  Student_ID: 122303
#  email_ID: michael5142@yahoo.net
