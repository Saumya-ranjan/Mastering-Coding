dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print (dict['Name'])
print (dict['Age'])

dict['Age'] = 8;                      # update existing entry
dict['School'] = "DPS School";        # Add new entry
print ( dict['Age'])
print (dict['School'])

dict.pop('Name')                    # remove entry with key 'Name'
# dict.clear();                       # remove all entries in dict
# del dict ;                          # delete entire dictionary
print(dict)

# Method of Dictionaries

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary