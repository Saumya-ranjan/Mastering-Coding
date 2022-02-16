def func(x):
    day_cover = 7
    night_cover = -2
    days = 0
    total_cover = 0
    while True:
        total_cover += day_cover
        days+=1
        if total_cover >= x:
            break
        total_cover += night_cover
    print(days)
func(31)