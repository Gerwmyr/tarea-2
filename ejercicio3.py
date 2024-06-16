n1=int(input("ingrese el valor de su nota \n"))
n2=int(input("ingrese el valor de su nota \n"))
n3=int(input("ingrese el valor de su nota \n"))
n4=int(input("ingrese el valor de su nota \n"))
suma=n1+n2+n3+n4
promedio=suma/4

if promedio <= 50:
    if promedio <=10:
        print("F")
    else:
        if promedio <=20:
            print("E")
        else:
            if promedio <=30:
                print("D")
            else:
                if promedio <=40:
                    print("C") 
                else:
                    print("B")
else:
    print("A")
