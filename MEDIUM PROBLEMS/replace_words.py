# a.startswith()

def replaceWords( dictionary , sentence):
    setenceAsList = sentence.split(" ")
    for i in range(len(setenceAsList)):
        for j in dictionary:
            if setenceAsList[i].startswith(j):
                setenceAsList[i] = j
    return " ".join(setenceAsList)


# TLE: 

#         arr = sentence.split()
#         for i in range(len(arr)):
#             for j in range(len(arr[i])):
#                 if arr[i][:j] in dictionary:
#                     arr[i] = arr[i][:j]
        
#         return (' '.join(arr))
  