#entrar 3 numeros e ver se eh triangulo
#condicao de existencia:
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
#se negativo, calcular a area de um trapezio usando a e b como base e c como altura
#1 casa decimal em qq caso


a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
perimetro = a + b + c
area = (a+b)*c/2
if (abs(b-c) < a < b+c):
    print("Perimetro = %0.1f" % perimetro)

elif (abs(a-c) < b < a+c):
    print("Perimetro = %0.1f" % perimetro)

elif (abs(a-b) < c < a+b):
    print("Perimetro = %0.1f" % perimetro)

else:
    print("Area = %0.1f" % area)
