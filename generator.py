import numpy as np
import matplotlib.pyplot as plt

### basics of vectors
# vector = np.array([1,2,3,4])
# print('Vector:\n', vector)

# matriz = np.array(
#     [[1,2,3],
#     [4,5,6],
#     [7,8,9]])
# print('\nMatriz:\n', matriz)


# tensor = np.array([
#                    [[1,2,3], [7,8,9]],
#                    [[1,2,3], [7,8,9]],
#                    [[0,0,0], [255,255,255]],
#                    [[0,0,0], [255,255,255]]
# ])
# print('\nMatriz:\n', tensor)


### no se pero grafica
# plt.imshow(tensor, interpolation='nearest')
# plt.show()

### sistema de ecuaciones sin solucion

# x = np.arange(-6,6)

# y_1 = 3*x+5
# y_2 = -x+3
# y_3 = 2*x+1
# plt.figure()
# plt.plot(x, y_1)
# plt.plot(x, y_2)
# plt.plot(x, y_3)

# plt.xlim(-8,8)
# plt.ylim(-8,8)

# plt.axvline(x=0, color='grey')
# plt.axhline(y=0, color='grey')

# plt.show()



### combinacion lineal
def graficarVectores(vecs, cols, alpha=1):

  plt.figure()
  plt.axvline(x=0, color='grey', zorder=0)
  plt.axhline(y=0, color='grey', zorder=0)

  for i in range(len(vecs)):
    x = np.concatenate([[0,0], vecs[i]])
    plt.quiver([x[0]],
               [x[1]],
               [x[2]],
               [x[3]],
               angles='xy', scale_units='xy', scale=1, color=cols[i], alpha=alpha)

# v1 = np.array([2,5])
# v2 = np.array([3,2])
# v1v2 = 2*v1 + 1*v2
# v1v2
# graficarVectores([v1, v2, v1v2], ['orange', 'blue', 'red'])
# plt.xlim(-1,8)
# plt.ylim(-1,12)
# for a in range(-10, 10):
#   for b in range(-10,10):
#     plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, marker = '.', color='orange')
  
# plt.xlim(-100,100)
# plt.ylim(-100,100)

# plt.axvline(x=0, color='grey')
# plt.axhline(y=0, color='grey')

# plt.show()


### subespacio 
v1 = np.array([1,1])
v2 = np.array([-1,-1])
for a in range(-10, 10):
  for b in range(-10,10):
    plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b, marker = '.', color='orange')
  
plt.xlim(-25,25)
plt.ylim(-25,25)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

plt.show()