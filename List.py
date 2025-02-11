#List 
a = [ 10 , 3.71 , 24 , 728, 12, 87," yash " ]
print(a)

#List Operations :

# 1.Indexing
print(a[2])

# 2.Slicing
print(a[2:5])

# 3.Modifying Elements
a[5]="Tambe"
print(a)

# 4.Append
a.append(56)
print(a)

# 5.Insert
a.insert(4,44)
print(a)

# 6.Extend : can add multiple elements
a.extend(["Mumbai"])
print(a)

# 7.Removing the Elements
a.pop() # Removes the last index
a.pop(5) # Removes by index
print(a)

a.remove("Tambe") #Removes by value
print(a)

a.clear() # Clears the entire list
print(a)

# 8.Searching and Counting
b = [10, 20, 10 , 30 , 10 , 40]
print(b.index(40))
print(b.count(10))

# 9. Sorting and Reversing
c = [2,4,6,1,8,5,9,7,3]
c.sort()
print(c)
c.reverse()
print(c)

