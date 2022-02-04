def func(x):
    
    # if x == x[-1::-1]:            (Only for String) 
    #     print("Palindrome")    
    # else:
    #     print("Not Palindrome")

 
    if (str(x) == str(x)[::-1]):    #  Changed it as String  (Used it in leetcode)
        print("Palindrome")
    else:
        print("Not Palindrome")
        

func(123)