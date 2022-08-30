#!/usr/bin/env python
# coding: utf-8

# #  1. Write a program to print your name.

# In[1]:


print("Vishal Awasthi")


# # 2. Write a program for a Single line comment and multi-line comments

# In[3]:


# Write a program for a Single line comment and multi-line comments.

# Read the input from the user
# Perform some operations on the input data
# Output the result
print("Multi-line commenting")


# # 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

# In[4]:


a = 5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))


# # 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

# In[10]:


# Global Variables:

# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Example:

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# In[2]:


# Local variables:

# local variables can be accessed only inside the function in which they are declared.

#Exapmple:
def f():
  
    # local variable
    s = "I love India"
    print(s)
  
  
# Driver code
f()


# In[ ]:




