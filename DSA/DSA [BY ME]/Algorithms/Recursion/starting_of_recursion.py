
def func():
    counter = 0
    
    if counter>3:
        return 'done'
    counter+=1
    return func()

func()


# This is Stack Overflow that means the memory is exceeded at calling the function 
# again and again. So the memory collapses so to stop that from 
# happening we can make a counter and initialise it with 0 and keep increasing it 
# till the requirement is met and then we can just stop the  function if the 
# requirement is met.
