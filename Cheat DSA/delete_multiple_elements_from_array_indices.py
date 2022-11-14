somelist = 1,2,3,4,5,6
indices = [0,2,3]
for i in sorted(indices, reverse=True):
    del somelist[i]