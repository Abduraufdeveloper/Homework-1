a = input("Isimni kiriting :")
b = input("Isimni kiriting :")
c = input("Isimni kiriting :")

d = 0
def names(a,b,c):
    while d < len(a):
        w = a[0]
        e = w.capitalize()
        print(e)
        break
    while d < len(b):
        u = b[0]
        i = u.capitalize()
        print(i)
        break
    while d < len(c):
        p = c[0]
        o = p.capitalize()
        print(o)
        break
    return (names(a,b,c))
    