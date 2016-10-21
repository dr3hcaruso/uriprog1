

qntd = int(input())
soma = 0
while qntd != 0:
    numero = int(input())
    qntd -= 1
    soma = 0
    for i in range(1,numero):
        if (numero % i == 0):
            soma = soma + i

    if soma == numero:
        print("%d eh perfeito" %numero)
    else:
        print("%d nao eh perfeito" %numero)
