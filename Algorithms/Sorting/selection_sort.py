# In selection sort it has two pointer where one points to smallest and other is for 
# searching then it scans whole list and bring smallest one to top and it happens again 
# and again

# 12 3 4 56 67 5 45 4

def selectionsort(arr):
  i = 0
  while i < len(arr):
    min = arr[i]
    index = i
    for j in range(i+1,len(arr)):
      if arr[j] < min:
        index = j
        min = arr[j]
    arr[i] , arr[index] = arr[index] , arr[i]
    i += 1
  
  return arr

arr = [8,6,5,0,4,3,2]
print(selectionsort(arr))