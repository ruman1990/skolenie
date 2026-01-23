import timeit

def sucet():
    return sum(range(100))

cas = timeit.timeit("sucet()", setup="from __main__ import sucet", number=1000000)
print(cas)