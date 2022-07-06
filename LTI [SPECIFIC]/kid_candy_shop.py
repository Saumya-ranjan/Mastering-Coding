# A kid goes to a shop that sells candies and other stuff. 
# All the candies are of the form of some palindrome between a 
# range (m, n) which is provided as input. The kid has a k amount 
# of money. Now the kid can buy some candies from the shop provided 
# that the difference between the max candy that he buys and the min 
# candy that he buys is less than or equal to k. What is the max number
# of candies that he can buy with k amount of money? 

# Eg 1: 

# Input= 50,78,12 
# Output= 2. 
# Explanation: palindromes are 55,66,77. 
# He can either choose (55,66) or (66,77) but not all as 22>12. 

# Eg 2:

# Input= 98, 112,13 
# Output= 3. 


# Brute Force 

# TLE

def candy_shop(a,b,W):
    arr = []
    count = 0
    for i in range(a,b):  # o(n)
        if str(i) == str(i)[::-1]:
            arr.append(i)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i]<=W:
                count+=1
    print(count)
                
    
candy_shop(0,112000,13 )