#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2,
#o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

#Entrada
0
#O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e
#um valor com 2 casas decimais.


##COMEÇO DO SCRIPT
#cada linha é composta pela entrada do código, do numero e do valor
#ou seja, em uma linha, 3 valores diferentes

#linha 1
cod1, qntd1, valor1 = input().split()
qntd1 = float(qntd1)
valor1 = float(valor1)

#linha 2
cod2, qntd2, valor2 = input().split()
qntd2 = float(qntd2)
valor2 = float(valor2)

total = qntd1*valor1 + qntd2*valor2
total = float(total)
print("VALOR A PAGAR: R$ %0.2f" % total)