# STRIVER DSA SHEET:
def combination(arr,target,output,index):
    if target == 0:
        print(output)
        return 
    output.append(arr[index])
    combination(arr,target-arr[index],output,index)
    output.remove(arr[index])
    combination(arr,target,output,index+1)




combination([2,3,6,7],7,[],0)