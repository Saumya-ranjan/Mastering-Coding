
def detectCapitalUse(word):
    value = 0
    for i in range(0,len(word)):
        if word[i].islower():
            value = value+1
        else:
            value = value+0
    if value >=1:
        print('false')
            
    else:
        print('true')

detectCapitalUse(input("Enter a string: "))