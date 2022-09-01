# cook your dish here
T=int(input())
for i in range(1,T+1):
    X,Y=list(map(int,input().split()))
    l=[int(i) for i in input().split()][: 2] # 2 --> Number of length

print(X,Y)