#  map( function , list of any datas)
#  so it passes that list to the function and get the output

# def addition(x):
#     return x + x

# Numbers = [1,2,3,4,5]
# tr = map(addition,Numbers)
# print(list(tr))



# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))    #takes each element from the list and passes in list inside map
print(test)
