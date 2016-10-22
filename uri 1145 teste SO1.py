quebra, final = input().split()
quebra, final = int(quebra), int(final)

for i in range(1, final+1):
    if i % quebra == 0 or i == final:
        print(i)
    else:
        print(i, end=" ")