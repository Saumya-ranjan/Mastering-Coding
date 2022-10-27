class Solution:
    def intervalIntersection(firstList , secondList):
        aptr = 0
        bptr = 0
        res = []
        
        while aptr < len(firstList) and bptr <len(secondList):
            if firstList[aptr][0] <= secondList[bptr][1] and firstList[aptr][1] >= secondList[bptr][0]:
                res.append([max(firstList[aptr][0] , secondList[bptr][0]) , min(firstList[aptr][1] , secondList[bptr][1])])
                
            if firstList[aptr][1] <= secondList[bptr][1] :
                aptr+=1
            else:
                bptr+=1
        return res
                         
            
            