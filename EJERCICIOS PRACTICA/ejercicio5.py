lista = [0, 3, 5, 9]
n = -1

while (n < 0 or n > 9):

    n = int(input('Ingresa un numero del 0 al 9: '))

if (n in lista):
    print('El numero esta en la lista')
else:
    print('El numero no esta en la lista')

