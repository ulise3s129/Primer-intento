print("""Suma(1\n resta(2)\ndiviciòn(3)\nimprimir dador de usuario(4)\nmultiplicaciòn(5)\nejercicio anterior(6)\n salir(7)\n """)
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
input(...)
