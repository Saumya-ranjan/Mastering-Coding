def insert(intervals,newInterval):
    #  interval beech mei jayega
    intervals.append(newInterval)
    intervals.sort()
    # Merge Intervals Algorithm:
    arr = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= arr[-1][-1]:
            arr[-1] = [arr[-1][0] , max(intervals[i][1] , arr[-1][-1])]
        else:
            arr.append(intervals[i])
    return arr
insert( [[1,2],[3,5],[6,7],[8,10],[12,16]] , [4,8])