from decimal import*
nome = input()
salariofixo = float(input())
vendasrealizadas = float(input())

bonus = vendasrealizadas*0.15
total = bonus + salariofixo

print("TOTAL = R$",Decimal(str(total)).quantize(Decimal('1.00'), rounding=ROUND_DOWN))