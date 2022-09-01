def move_all_ball(boxes):
    arr = []
    for i in range(len(boxes)):
        count = 0
        for j in range(len(boxes)):
            if i == j:
                continue
            elif boxes[j] == '1':
                    count+= abs(i-j)
        arr.append(count)
    print(arr)
                    


move_all_ball('001')