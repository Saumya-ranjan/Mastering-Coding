def printSubSequences(STR, subSTR=""):
  
    if len(STR) == 0:
        print(subSTR, end=" ")
        return
 
    # we add adding 1st character in string
    printSubSequences(STR[:-1], subSTR + STR[-1])
    
    printSubSequences(STR[:-1], subSTR)
    return
 
 
def main():
  
    STR = "abc"
    printSubSequences(STR)
 
 
if __name__ == "__main__":
    main()