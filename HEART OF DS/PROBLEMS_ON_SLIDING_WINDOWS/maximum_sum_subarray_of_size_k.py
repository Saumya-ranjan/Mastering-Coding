# Efficient Method --> Because of one for loop( o(n))

def sum_subarray(arr,window):
    arr1 = []
    for i in range(len(arr)):
        if i + window <=len(arr):
            arr1.append(sum(arr[i:i+window]))
    print(max(arr1))

sum_subarray([2,5,2,8,2,9,1],4)

