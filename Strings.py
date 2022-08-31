# Different ways creating a string.

string = "Hello"
print(string)

string = 'Hello'
print(string)

string1 = '''World'''
print(string1)

string2 = """Welcome to 
			my youtube channel""" # triple
print(string2)
print()

# Concatenating two strings using + operator.

str1 = string + string1
print("Concatenating two different strings: ",str1)

# Finding the length of the string.

str3 = "Vishal"
print("Length of the String: ",len(str3))

# Extract a string using Substring.
#Searching in strings using index()
str3 = 'Awasthi'
str1 = 'thi'
str2 = 'i'

print("Position of thi:",str3.index(str1))
print("Position of i:",str3.index(str2))

# Matching a String Against a Regular Expression With matches()

from ast import Str 
import re 
substr = 'Lucknow'
str6 = 'Lucknow is the city of Nwab'
print(re.match(substr,str6))


# Comparing strings 

str8 = 'Vishal Awasthi'
str1 = 'Ashmit Awasthi'

str2 = str8

print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)

# startsWith(), endsWith() and compareTo()

string = 'Vishal Awasthi'
print(string.startswith("Vishal"))
print(string.endswith("sthi"))


# Trimming strings with strip()

str7 = "Hello World hi"
print(str7.strip("hi"))

# Replacing characters in strings with replace()

string = "hi World"
print(string.replace("hi","Hello"))

# Splitting strings with split()

string = 'hi-hello-bye'
print(string.split("-"))

# Converting integer objects to Strings.

num = 10
num1= str(num)
print(num1)
print(type(num1))

# Converting to uppercase and lowercase.

string = 'hello'
string1 = 'WORLD'

print(string.upper())
print(string1.lower())





