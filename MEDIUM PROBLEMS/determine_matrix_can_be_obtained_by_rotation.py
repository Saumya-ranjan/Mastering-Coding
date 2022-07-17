def find_rotation(mat,target):

    # Rotation Of  Ninety Degree: 
    def rotate(mat1):
        hash = {}
        mat2 = []
        mat1 = mat1[::-1]
        for i in mat1:
            for j in range(len(i)):
                if j not in hash:
                    hash[j] = [i[j]]
                else:
                    hash[j].append(i[j])
        for i in hash.values():
            mat2.append(i)
        return mat2
    
    # 1 rotate:
    if mat ==  target:
        return True 


    # 2nd Rotate
    mat3 = rotate(mat)
    if mat3 == target:
        return True

    # 3rd Rotate
    mat4  = rotate(mat3)
    if mat4 == target:
        return True


    #4th rotate
    mat5 = rotate(mat4)
    if mat5 == target:
        return True
    return False


print(find_rotation([[0,1],[1,0]], [[1,0],[0,1]]))