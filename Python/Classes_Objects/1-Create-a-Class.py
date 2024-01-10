# Syntax
class className:
 code goes here

# Example 1- create a class
class person:
    pass
print(person)

# Example 2- Create an object
# We can create an object by calling the class
p = person()
print(p)

# Class Constructor
class person:
   def __init__(self, name):
      self.name =  name

p = person("Zwivhuya")
print(p.name)
print(p)