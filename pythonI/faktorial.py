def faktorial(n):
    if n == 0:
        return 1
    return n * faktorial(n - 1)


def faktorial_while(n):
    vysledok = 1
    while n > 1:
        vysledok = vysledok * n
        n = n - 1
    return vysledok

print(faktorial(5))
print(faktorial_while(5))
