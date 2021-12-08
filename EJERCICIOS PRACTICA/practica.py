n = -1
n1 = int(input('Ingrese primer numero: '))
n2 = int(input('Ingrese segundo numero: '))

while (n > 0 or n < 3):
    x = int(input('Ingrese la opcion deseada: \n 1-Sumar \n 2-Restar \n 3-Multiplicar \n\n'))
    if x == 1:
        print(n1+n2)
        break
    elif x == 2:
        print(n1-n2)
        break
    elif x == 3:
        print(n1*n2)
        break
    else:
        print('La opcion ingresada no es correcta')
        break
