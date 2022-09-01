def max_sum_of_atmost_k_elems(arr,k):
    arr1 = []
    while len(arr1) < k:
        if arr[0] > arr[-1]:
            arr1.append(arr[0])
            arr.pop(0)
        elif arr[-1] > arr[0]:
            arr1.append(arr[-1])
            arr.pop(-1)
        else:
            arr1.append(arr[0])
            arr.pop(0)
    print(sum(arr1))

max_sum_of_atmost_k_elems([-2, -1, -6, -3, 1], 2)