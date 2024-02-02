a = input("Yu should to type : ")
b = input("Yu should to type : ")
c = 0
def typing(a,b,c):
    while c < len(a) and c < len(b):
        e = len(a)
        d = len(b)
        if e == d:
            print("1s")
        elif e != d:
            print("-1s")
        break
    return (typing(a,b,c))