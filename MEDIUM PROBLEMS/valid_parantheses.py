def parantheses(s):
    hash = {')':'(' , ']':'[','}':'{'}
    arr = []
    for i in s:
        if i ==')' or i==']' or i == '}':
            if len(arr)>0 and hash[i] in arr[-1]:
                arr.pop(-1)
            else:
                return False
        else:
            arr.append(i)
    if len(arr) == 0:
        return True
    return False


parantheses("()")