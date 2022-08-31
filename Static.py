# Define a static variable and access that through a class.

class Python:
# Access through class
	staticVariable = 25 
print(Python.staticVariable) # give 25


# Define a static variable and change within the class
class Python:
# Access through class
	staticVariable = 25 
print(Python.staticVariable) # give 12

# change within an class

Python.staticVariable = 12 
print(Python.staticVariable)

# Define a static variable and access that through a instance

class Python:
# Access through class
	staticVariable = 25 

# Access through instance

	instance = Python() 
	print(instance.staticVariable) # give 12

# Define a static variable and change within the instance

class Python:
# Access through class
	staticVariable = 25 
	instance = Python() # Access through instance
	print(instance.staticVariable) # give 12

# Change within an instance
	instance.staticVariable = 30
	print(instance.staticVariable) # give 30
