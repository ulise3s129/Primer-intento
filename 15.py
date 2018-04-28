print("1º-si")
print("2ª-no")
f= int(input("¿Quieres hacer una operaciòn?"))
while f==1:
    print("""Suma(1\nresta(2)\ndiviciòn(3)\nimprimir dador de usuario(4)\nmultiplicaciòn(5)\nejercicio anterior(6)\nsalir(7)\ncomparaciòn de numeros(8)\n """)
    a=int (input())
    if a==1:
            b=int(input("dame un numero:"))
            c=int(input("dame otro numero:"))
            resultado=b+c;
            print("el resultado es:",resultado)
    if a==2:
                b=int(input("dame un numero:"))
                c=int(input("dame otro numero:"))
                resultado=b-c;
                print("el resultado es:",resultado)
    if a==3:
          b=int(input("dame un numero:"))
          c=int(input("dame otro numero:"))
          resultado=b/c;
          print("el resultado es:",resultado)

    if a==4:
          b=input("nombre")
          c=input("edad")
          d=input("peso")
          print("tu nombre es:",b,"\ntu edad es:",c,"\ntu peso es:",d)
    if a==5:
           b=int(input("dame un numero:"))
           c=int(input("dame otro numero:"))
           resultado=b*c;
           print("El resultado es:",resultado)
    if a==6:
          a=int(input("que tabla quiere?"))
          b=int(input("hasta que rango?"))
          for var in range(1,b+1):
              print(var,"x",a,"=",var*a)
    if a==7:
           print("adios")
    if a==8:
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
    print("1º-si")
    print("2ª-no")
    f= int(input("¿Quieres hacer una operaciòn?"))


input(...)
