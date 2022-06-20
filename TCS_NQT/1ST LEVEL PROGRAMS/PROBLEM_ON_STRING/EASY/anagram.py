def func(n,x):
    n = sorted(n)
    x = sorted(x)
    if n==x:
        print("anagram")
    else:
        print("Not anagram")


func('cat','act')