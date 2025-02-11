# A string can only be written in quotes for example :
a = 'Python'
print(a)
b = "Yash is the best Coder"
print(b)
c = '''Early bird gets
the worm\n''' # tripple quotes can be used for multiple lines .
print(c)

# Operaations on a String 

#Concatenation 
c1 = "Paplu"
c2 = "Taplu"
print(c1+" "+c2)
 
#Repetition
print(c1*3)

#Indexing
print(c1[1])

#Slicing
print(c1[0:4])

#length
print(len(c2))

#Upper And Lower Case
l1 = "small"
print(l1.upper())
l2 = "CAPITAL"
print(l2.lower())

#Replace and Pop
r1 = "I will have a bike oneday "
print(r1.replace("bike", "car"))
p1 = [11,22,33,44]
print(p1.pop(2))