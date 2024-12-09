'''
print("Hello, ", end=" ")
print("world")

'''
''''
Variable Naming Rules:
 a. Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
 b. The first character of a variable name cannot be a digit.
 c. Variable names are case-sensitive, so myVar and myvar are different variables.
 d. It's good practice to use descriptive variable names that reflect their purpose.
 e. Generally, we follow the convention of naming variables using snake_case, rather than lowerCamelCase
 
'''
 #int x = 5; But in python we need not do that.
'''
x = 10      # Integer
name = "Alice"  # String
pi = 3.14   # Float
is_student = True  # Boolen
print(name,x,pi,is_student)

 
 '''
name='biru'
age= 'ten'
print("my name is ",name, "and age is a ",age,)  

name_age = name+ " " +age
print(name_age)

print("My name is " + name + "and I am " + age + " years old.") 
print(f"My name is  {name}  and I am {age} years old.") 

age = 30 

with open("output.txt", "w") as f:
 print("Hello, World!", file=f)
 
 