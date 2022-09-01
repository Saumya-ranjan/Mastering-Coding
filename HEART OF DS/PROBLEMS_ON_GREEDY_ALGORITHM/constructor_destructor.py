class Solution:
    def __init__(self,x,y):   #Constructor
        self.x = x
        self.y = y
    def __add__(self,other):
        return (self.x + other.x , other.y + self.y)

    

p = Solution(50,60)
p1 = Solution(60,120)
p2  = p+p1
print(p2)



    
