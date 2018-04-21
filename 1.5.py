a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b:
    print(a,"es mayor que",b)
    if b>c:
        print(b,"es mayor que",c)
    elif c>b:
        print(c,"es mayor que",b)
    elif c==B:
        print(c,"y",b,"son iguales")
elif b>c:
    print(b,"es mayor que",c)
    if c>a:
        print(c,"es mayor que",a)
    elif a>c:
        print(a,"es mayor que",c)
    elif a==c:
        print(a,"y",c,"son iguales")
elif c>a:
    print(c,"es mayor que",a)
    if a>b:
        print(a,"es mayor que",b)
    elif b>a:
        print(b,"es mayor que",a)
    elif a==b:
        print(a,"y",b,"son iguales")    
if a==b and b==c:
    print("todos son iguales")
elif a==b and b!=c:
    print(a,"es igual que",b,"y es diferente de",c)
elif a==c and c!=b:
    print(a,"es igual que",c,"y es diferente de",b)
elif c==b and b!=a:
    print(c,"es igual que",b,"y es diferente de",a)
elif a!=b and b!=c and a!=c:
    print("Todos son diferentes")
input(...)
