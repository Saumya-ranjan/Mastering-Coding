# NGE -- >
for test in range(int(input())):
    n =  int(input().split()[1])
    arr = [int(j) for j in input().split()]  
    stack = []
    a = ''
    for i in arr:
        while n and stack and stack[-1]<i:
            stack.pop()
            n-=1
        stack.append(i)
    for k in stack:
        a+=str(k)+" "
    print(a)
            
