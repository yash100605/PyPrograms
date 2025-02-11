# A tuple can be created using () brackets
a = (2,4,6,8,10)

# Operations on Tuple

# 1. Accessing Elemensts

print(a[2]) # By Indexing
print(a[2:4]) # By Slicing

# 2. Length of a Tuple
print(len(a))

# 3. Concatenation & Repetition

c1 = (1,2,3,4,5)
c2 = (6,7,8,9)
print(c1+c2) # Concatenation
print(c2*3)

# 4. Checking for an Element
print(4 in c1)
print(5 in c1)
print(22 in c1)
print(83 in c1)

# 5.CountValue & IndexValue
print(c1.count(2)) # will count occurence of 2 in tuple
print(c1.index(5)) # Output : 4
