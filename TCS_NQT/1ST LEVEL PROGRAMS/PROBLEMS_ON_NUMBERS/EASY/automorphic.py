def func(n):
    r  = n * n 
    a = str(r)[::-1]
    b = str(n)[::-1]
    a = a[:len(b)]
    if a == b:
        print("automorphic")
    else:
        print("Not AUtoMorphic")
func(6)