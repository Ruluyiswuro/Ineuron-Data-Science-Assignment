"""
PYTHON BASIC ASSIGNMENT 7

Q1. What is the name of the feature responsible for generating Regex objects?

Ans : re.compile() is the feature responsible for generation of Regex objects. In simple terms, we can compile a regular
expression into a regex object to look for occurrences of the same pattern inside various target strings without
rewriting it.
"""
import re
x = re.compile("Random_pattern")
type(x)
print(x)

"""
Q2. Why do raw strings often appear in Regex objects?

Ans : Regular expressions use the backslash character ('\') to indicate special forms (metacharacters) or to allow 
special characters (special sequences) to be used without invoking their meaning. This collides with Python's usage
of the same character for the same purpose in string literals. Hence, raw strings (e.g. r"\n") are used so that 
backslash do not have to be escaped.
"""

"""
Q3. What is the return value of the search() method?

Ans : The return value of the re.search() method is a match of object if the pattern is observed in the string, else it 
returns a None.
"""
import re
match = re.search('e', "full stack data science course")
print(match)
#<re.Match object; span=(19, 20), match='e'>
match2 = re.search('b', "full stack data science course")
print(match2)
#None

"""
Q4. From a match item, how do you get the actual strings that match the pattern?

Ans : For matched items group() method returns actual strings that match the pattern.
"""
import re
match = re.search('course', "full stack data science course")
print(match.group())
#course

"""
Q5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover?
Group2? Group1?

Ans : In the Regex r'(\d\d\d)-(\d\d\d-\d\d\d\d)' the zero group covers the entire matched pattern
whereas, group1 covers the first group (\d\d\d) and group 2 covers (\d\d\d-\d\d\d\d).

"""
import re
phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
pN = phoneNum.search('Phone number is 101-204-3567')
print(pN.groups()) #('101', '204-3567')
print(pN.group(1))#101
print(pN.group(2))#204-3567

"""
Q6. In the standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex
that you want it to fit real parentheses and periods?

Ans : The escape characters \ ,\( and \) in the raw string passed to re.compile will match the actual
parentheses characters.
"""
import re
phoneNum = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
pN = phoneNum.search('phone number is (103) 896-0991.')
print(pN.group())
#(103) 896-0991

"""
Q7. The findall() method returns a string list or a list of strings tuples. What causes it to return one of the two 
options?

Ans : If the regex has no groups, a list of strings matched is returned. If the regex pattern has groups,
a list of tuple of string is returned.
"""
import re
phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')
ph = phoneNum.findall('Phone number is 123-456-7891')
print(ph)
phoneNum = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
ph = phoneNum.findall('Phone number is (123) 456-7891')
print(ph)

"""
Q8. In standard expressions, what does the | character mean?

Ans : In standard expressions, the character | means OR operator.
"""

"""
Q9. In regular expressions, what does the character stand for?

Ans : A character is a set of valid characters which are recognized by Python and are use during a script
writing in python.
(no specific character is provided in the question).
"""

"""
Q10. In regular expressions, what is the difference between + and * characters?

Ans : In regular expressions, * represents zero or more occurrences of the preceding group.
Whereas, + represents one or more occurrences of the preceding group.
"""

"""
Q11. What is the difference between {4} and {4,5} in regular expressions?
Ans : In regular expressions, {4} represents that the preceding group should repeat 4 times.
Whereas, {4,5} represents that preceding group should repeat 4 times and maximum 5 times.



Q12. What do you mean by the \d,\w and \s shorthand character classes signify in regular expressions?

Ans : The shorthand characters \d, \w and \s are special sequences in regular expressions in python where:
1. \d matches digit character equivalent to [0-9]
2. \w matches a word charcater equivalent to [a-zA-Z0-9]
3/ \s matches whitespace character (space, tab, newline, etc)



Q13. What do you mean by the \D,\W and \S shorthand character classes signify in regular expressions?
Ans : The shorthand characters \D, \W and \S are special sequences in regular expressions in python where:
1. \D – Matches any non-digit character, this is equivalent to the set class [^0-9]
2. \W – Matches any non-alphanumeric character equivalent to [^a-zA-Z0-9_]
3. \S – Matches any non-whitespace character
"""

"""
Q14. What is the difference between .*? and .*?

Ans : .* is a Greedy mode, which returns the longest string that meets the condition. Whereas .*? is a non greedy mode 
which returns the shortest string that meets the condition.


Q15. What is the syntax for matching both numbers and lowercase letters with a character class?

Ans : The syntax for matching both numbers and lower case letters with a character class is 
[a-z0-9] or [0-9a-z]


Q16. What is the procedure for making a normal expression in regax case insensitive?

Ans : We can pass re.IGNORECASE as a flag to make a normal expression case insensitive


Q17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd
argument in re.compile()?

Ans : The . (dot) character matches everything in input except newline character. By passing re.DOTALL as a 2nd argument
to re.compile, you can make the dot character match all characters including newline character.


Q18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?

Ans : The Ouput will be 'X drummers, X pipers, five rings, X hen'
"""
import re
numReg = re.compile(r'\d+')
numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
print(numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen'))

"""
Q19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

Ans : Passing re.VERBOSE as 2nd argument will allow to add whitespace and comments to string passed to re.compile().

"""
"""
Q20. How would you write a regex that match a number with comma for every three digits? It must match the given 
following:

'42'
'1,234'
'6,368,745'
but not the following
'12,34,567'(which has only two digits between the commas)
'1234'(which lacks commas)

"""
import re
pattern = r'^\d{1,3}(,\d{3})*$'
pagex = re.compile(pattern)
for commas in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',commas, '---', pagex.search(commas))
#Output: 42 --- <re.Match object; span=(0, 2), match='42'>
#Output: 1,234 --- <re.Match object; span=(0, 5), match='1,234'>
#Output: 6,368,745 --- <re.Match object; span=(0, 9), match='6,368,745'>
#Output: 12,34,567 --- None
#Output: 1234 --- None

"""
Q21. How would you write a regex that matches the full name of someone whose last name is
Watanabe? You can assume that the first name that comes before it will always be one word that
begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following
'haruto watanabe' (where the fist name is not capitalized)
'Mr.Watanabe'(where the preceding word has a nonletter character)
'Watanabe'(which has no first name)
'Haruto watanabe'(where Watanabe is not capitalized)
Ans : patter = r'[A-Z]{1}[a-z]*\sWatanabe
"""
import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
namex = re.compile(pattern)
for name in ['Haruto Watanabe','Alice Watanabe', 'RoboCop Watanabe', 'haruto watanabe', 'Mr.Watanabe','Haruto watanabe' ]:
    print('output : ', name, '-----', namex.search(name))
#output :  Haruto Watanabe ----- <re.Match object; span=(0, 15), match='Haruto Watanabe'>
#output :  Alice Watanabe ----- <re.Match object; span=(0, 14), match='Alice Watanabe'>
#output :  RoboCop Watanabe ----- <re.Match object; span=(4, 16), match='Cop Watanabe'>
#output :  haruto watanabe ----- None
#output :  Mr.Watanabe ----- None
#output :  Haruto watanabe ----- None

"""
Q22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,
or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
and the sentence ends with a period? This regex should be case-insensitive. It must match the
following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats'

Ans : pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
"""
import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
casex = re.compile(pattern, re.IGNORECASE)
for sentence in ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.',
                 'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats']:
    print('Output is : ', sentence, '----', casex.search(sentence))
#Output is :  Alice eats apples. ---- <re.Match object; span=(0, 18), match='Alice eats apples.'>
#Output is :  Bob pets cats. ---- <re.Match object; span=(0, 14), match='Bob pets cats.'>
#Output is :  Carol throws baseballs. ---- <re.Match object; span=(0, 23), match='Carol throws baseballs.'>
#Output is :  Alice throws Apples. ---- <re.Match object; span=(0, 20), match='Alice throws Apples.'>
#Output is :  BOB EATS CATS. ---- <re.Match object; span=(0, 14), match='BOB EATS CATS.'>
#Output is :  RoboCop eats apples. ---- None
#Output is :  ALICE THROWS FOOTBALLS. ---- None
#Output is :  Carol eats 7 cats ---- None


