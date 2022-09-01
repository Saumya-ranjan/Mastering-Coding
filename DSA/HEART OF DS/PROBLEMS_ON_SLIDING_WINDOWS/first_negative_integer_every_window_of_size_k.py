def first_neg_win(arr,target):
    arr1 = []
    for i in range(len(arr)):
        count = 0
        for j in range(i,i+target):
            if i+target <= len(arr):
                if arr[j] < 0 :
                    arr1.append(arr[j])
                    break
                else:
                    count+=1
        if count == target:
            arr1.append(0)
    print(arr1)
  


        



first_neg_win([12,-1,-7,8,-15,30,16,28,45,34,24,24],3)