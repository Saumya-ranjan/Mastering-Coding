def func(x):
    curr_sum = max_sum  = x[0]
    for i in x[1:]:
        curr_sum = max(curr_sum+i,i) 
        max_sum = max(max_sum,curr_sum) 
    print(max_sum)
    

func([-2,1,-3,4,-1,2,1,-5,4])