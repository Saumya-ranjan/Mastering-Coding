# In string comparing '1' > '12'

# There has been a change in Python’s sorted() function, 
# it now takes three values namely, the iterable, key, and reverse. 
# Out of these last two are optional but this article emphasizes the key part 
# of the sorted() function. What key does is, it helps in the comparison of iterable 
# elements while sorting.  Python already had cmp() function that used to compare two 
# values and return 1, -1, or 0. But as of Python 3.0 and above, this function has been 
# deprecated and a new function cmp_to_key() has been introduced. The following article 
# discusses the application and explanation of this function.

# Definition
# cmp_to_key() uses a key to compare elements
# It is built into functools module, thus functools has to be imported first in order to use the function
# Used with tools that accept key functions such as min(), max(), sorted() etc.
# Takes only one argument which strictly should be a callable
# This function returns a special key that can be used to compare elements

from functools import cmp_to_key
def largestNumber(self, num):
        def cmp_func(x, y):
            if x+y > y+x:
                return 1
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums = sorted(nums , key = cmp_to_key(cmp_func) , reverse = True)
        print(nums)
        a = ''.join(nums)
        return str(int(a))