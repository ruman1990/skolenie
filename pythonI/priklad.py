import copy

w = [[1,2],6,8,1,7,20,35,55]


c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)

w[0][0] = 999

print(w)
print(c1)
print(c2)
print(c3)
print(c4)