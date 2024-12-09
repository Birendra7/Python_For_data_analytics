'''
 Typecasting
 type(
 Typecasting, also known as type conversion, is the process of changing the data type of a variable from one 
type to another. In Python, you can perform typecasting using built-in functions or constructor functions for the 
desired data type.
 Python type() is a built-in function that is used to return the type of data stored in the objects or variables in 
the program
 For example, if a variable contains a value of 45.5 then the type of that variable is float
 If variable ‘subj’ stores the value ‘Python’, then the type of ‘subj’ is a string.
 Here are some common type casting functions in Python:
 1. int(): Converts a value to an integer data type.
 2. float(): Converts a value to a floating-point data type.
 3. str(): Converts a value to a string data type.
 4. bool(): Converts a value to a boolean data type.
 5. list(): Converts a value to a list data type.
 6. tuple(): Converts a value to a tuple data type.
 7. set(): Converts a value to a set data type.
 8. dict(): Converts a value to a dictionary data type.
 
 
 
 Example of Typecasting:
 A. Integer to String
 num = 42
 num_str = str(num)
 print(num_str, type(num_str))
 B. String to Integer
 num_str = "123"
 num = int(num_str)
 print(num, type(num))
 C. Float to Integer
 float_num = 3.14
 integer_num = int(float_num)
 print(integer_num, type(integer_num))
 Note: it is important to ensure compatibility and proper handling of data in different contexts. 
Eg: You can’t typecast string “apple” to int
'''