def sundays(day , number_day):
    hash = {'sun':0 ,'mon':1, 'tue': 2 , 'wed': 3,'thu':4, 'fri':5, 'sat':6}
    count = 0
    if day in hash:
        if (7 - (hash[day])) > number_day:
            return count
        else:
            count+=1
            number_day  = number_day - (7-hash[day])
    while number_day - 7 >=0:
        count+=1
        number_day-=7
    return count


print(sundays(input('Enter the Day: ') , int(input('Number Of Days: '))))