from funcy import memoize

@memoize
def draha_funkcia(x):
    print("Volám funkciu...")
    return x * 2

print(draha_funkcia(10))  # vypočíta
print(draha_funkcia(10))  # použije cache, nevypíše "Volám funkciu..."