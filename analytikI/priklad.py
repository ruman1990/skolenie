import matplotlib.pyplot as plt
import numpy as np

# xpoints = [0,6]
# ypoints = [0,250]
# font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
# font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# plt.subplot(2, 1, 1)

# plt.plot(xpoints, ypoints, '-o')
# plt.plot([1,2,3,4], [1,4,9,16], 'r--')

# plt.title('moj graf')
# plt.ylabel('Predaje', fontdict=font2)
# plt.xlabel('mesiace', fontdict=font1)
# plt.grid(axis='y')

# plt.subplot(2, 1, 2)

# #plt.scatter(xpoints, ypoints)
# plt.scatter([1,2,3,4], [1,4,9,16])  
# plt.title('moj graf 2')
# plt.ylabel('Predaje', fontdict=font2)   
# plt.xlabel('mesiace', fontdict=font1)
# plt.suptitle("MY SHOP")
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()