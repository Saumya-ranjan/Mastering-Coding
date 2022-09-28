def weeks(day , k):
    arr = ['monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
    while k>7:
        k-=7
    for i in range(len(arr)):
        if arr[i] == day:
            return arr[i+k]

print(weeks("monday" , 7))