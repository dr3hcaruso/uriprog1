nome = input()
salariofixo = float(input())
vendasrealizadas = float(input())

bonus = float(vendasrealizadas * (15/100))

total = salariofixo + bonus

print("TOTAL = R$ %0.2f" %total)