def triangle_minimum(triangle):
    a = len(triangle[-1])
    for i in triangle:
        while len(i)!=a:
            i.append(1000)
    for i in range(len(triangle)):
        for j in range(len(triangle[0])):
            if i == 0 :
                triangle[i][j] = triangle[i][j]
            elif j ==0 and i>0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            else:
                triangle[i][j] = min(triangle[i-1][j-1] +  triangle[i][j] , triangle[i-1][j] + triangle[i][j])
                
            
    return min(triangle[-1])


triangle_minimum([[2],[3,4],[6,5,7],[4,1,8,3]])