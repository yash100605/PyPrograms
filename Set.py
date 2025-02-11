# A set is created using {} brackets 
a = {10,20,10,30,40,50,60,70}
print(a)

# Operations on Set
 
# 1.Adding Elements
a.add(56)
print(a)

# 2.Removing Elements
a.remove(56) # will remove 56
print(a)

a.discard(40) # will remove 40
print(a)

a.pop() # will remove random element
print(a)

a.clear() # will remove all elements
print(a)

# 3. Union , Intersection , Difference
b = {1,2,3,5,8,4,9}
c = {4,7,6,9}

print( b | c ) # Union --> { 1,2,3,4,5,6,7,8,9}
print( b & c ) # Intersection 
print( b - c ) # Difference

 