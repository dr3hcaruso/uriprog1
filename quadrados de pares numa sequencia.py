entrada = int(input())
lista = list(range(1,entrada+1))

for i in lista:
    if i%2 == 0:
        print ("%d^2 =" %i, i**2)
