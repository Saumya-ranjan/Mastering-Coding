# def func(x):
#   for i in range(0,len(x)):
#     for j in range(i+1,len(x)):
#       if x[i]==x[j]:
#         print(x[i])
        

from tkinter import X


def hashtable(x):                     # O(n) rather than O(n^2)
  mydict = {}
  for i in range(0,len(x)):          
    if x[i] in mydict:
      return X[i]
    else:
      mydict[x[i]]=i
  return 0
  

mylist = [2,1,1,2,3,4,5,3]
x = hashtable(mylist)
# func(mylist)
print(x)