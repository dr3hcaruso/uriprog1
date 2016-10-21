#0 1 1 2 3 5 8 13 21
#0 1 fixos, depois a soma dos 2 anteriores
#ler um numero inteiro n e mostrar os n primeiros termos da sequencia de fibonacci
# fib = (range(fib[1],239498,(fib[i-2]+fib[i-1])))



entrada = int(input())
fib = [0,1]
i = 2


if i != 46:
    while i != entrada:
        inc = (fib[i-2]+fib[i-1])
        fib.append(inc)
        i = i + 1

    else:
        print (*fib)