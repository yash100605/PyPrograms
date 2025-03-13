#Python Inbuilt Errors
# 1. ZeroDivisionError: Raised when you try to divide a number by zero.
try:
    10/0
except ZeroDivisionError:
    print("Can't divide by zero")

"""# 2. ValueError: Raised when a function receives an argument of the 
                    correct type but an inappropriate value."""
try:
    x = int(input())
except ValueError:
    print("Invalid input give a numeric value")

"""# 3. IndexError: Raised when you try to access an 
                    index that is out of range for a list or other indexable object."""
try:
    x = [10,23,59]     
    print(x[4])
except IndexError:
    print("Invalid Index")
    
# 4. KeyError: Raised when you try to access a dictionary with a key that doesn't exist
try:
    pr_error = { "x":10 , "y":20 }
    print(pr_error["z"])
except KeyError:
    print("Invalid Key")

# 5. FileNotFoundError 
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# 6.TypeError:
try:
    result = "string" + 5  # This will raise TypeError
except TypeError:
    print("You can't add a string and an integer!")

# 7.ImportError:
# try:
#     import yashkecode  # This will raise ImportError
# except ImportError:
#     print("Module not found!")

# 8.NameError:
# try:
#     print(piew_piew)  # This will raise NameError
# except NameError:
#     print("Variable is not defined!")

# 9.MemoryError:
try:
    # Allocating too large a list might raise MemoryError (depending on the system)
    large_list = [0] * (10**10)
except MemoryError:
    print("Out of memory!")

# 10.AttributeError:
try:
    my_str = "hello"
    my_str.kuchbhi()  # This will raise AttributeError
except AttributeError:
    print("The object doesn't have this method!")

