from funcy import lmap, lfilter, partial, compose

print(lmap(lambda x: x + 1, [1, 2, 3]))  # [2, 3, 4]
print(lfilter(lambda x: x % 2 == 0, range(10)))  # [0, 2, 4, 6, 8]


def nasobok_dvoch(x):
    return x * 2

# Zreťazenie funkcií (compose)
f = compose(str, nasobok_dvoch,abs)
print(f(-15))  # '15'


print(str(nasobok_dvoch(abs(-15))))