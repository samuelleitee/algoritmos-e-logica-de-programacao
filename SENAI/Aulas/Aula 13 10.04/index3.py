def fatorial(n):
    if n == 0:
        return 1
    else:
        print(f'{n} x ', end='')
        return n * fatorial(n - 1)
    
