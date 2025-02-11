# A dictionary is created using {key : value}
Dict = { "Fruit" : "Mango" , 
         "Car" : "Rolls Royce" , 
         "Bike" : "Honda" , 
         "Colour" : "Black" , 
         "Roll.No" : 72
         }
print(Dict)

# Operations on Dictionary

# 1.Accessing Values
print(Dict["Fruit"]) # Output : Mango
print(Dict["Roll.No"])

# 2.Adding and Updating Values
Dict["Car"] = "Koenisegg"
Dict["Bike"] = "Kawasaki"
print(Dict)

# 3.Dictionary Methods

print(Dict.keys()) # prints the keys from dictionary 
print(Dict.values()) # prints the values from dictionary
print(Dict.items()) # prints the key value for all content in the dictionary

# 4.Updating a Dictionary
NewDict = {
    "Name" : "Yash",
    "Hobby": "Chess",
    "DOB"  : "10-06-2005"
    }
Dict.update(NewDict)
print(Dict)

# 5.Removing Elements
Dict.pop("Car")
print(Dict) # Removes the key Car

Dict.clear()
print(Dict) # Removes all Elements


