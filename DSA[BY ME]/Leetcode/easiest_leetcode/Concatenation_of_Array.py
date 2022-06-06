def func(x):                 # Concatenation with big o(n)
    for i in range(len(x)):
        x.append(x[i])
    print(x)

func([1,21])



# def func(x):                # concatenation with o(n)
#     print(x+x)
# func([1,2,3,4])


#  def getConcatenation(self, nums: List[int]) -> List[int]:            #  o(1)
#         m = len(nums)
#         a = [None] * 2 * m
#         a[:m] = a[m:] = nums
#         return a