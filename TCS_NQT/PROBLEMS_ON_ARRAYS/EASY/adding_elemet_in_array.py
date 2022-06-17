arr = [1,2,3,4,5]
   
def insertbeginning(number,arr):
    arr.insert(number,0)
def insertending(number,arr):
    arr.append(number)
def insertatpos(number,arr,k):
    arr.insert(number,k)
    print(arr)
       

insertbeginning(6,arr)
insertending(3,arr)
insertatpos(3,arr,3)