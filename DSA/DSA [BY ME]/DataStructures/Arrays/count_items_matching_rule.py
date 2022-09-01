def func(items,ruleKey,ruleValue):
    type = []
    color = []
    name = []
    for i in items:
        type.append(i[0])
        color.append(i[1])
        name.append(i[2])
    
    count = 0  
    if ruleKey == "type":
        for i in type:
            if ruleValue == i:
                count+=1
   
    elif ruleKey == "color":
        for i in color:
            if ruleValue == i:
                count+=1
    elif ruleKey == "name":
        for i in name:
            if ruleValue == i:
                count+=1
    print(count)
    return count
    
    # for k,v in hash.items():
    #     if v == ruleKey:
    #         if k == ruleValue:
    #             count+=1
    # if count>0:
    #     print(count)
    # else:
    #     print(count)
func([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone")