from sympy.abc import x, y, _clash1
from sympy import sympify, expand, simplify

coordinates = [(1, 0), (2, 1), (3, 4)] 
index = [0, 1, 2] # 0, 1, 2
coordinatesRef = index.copy()
l = []
g = []
h = []
r = []

for j in range(0, len(index)):
  del coordinatesRef[j]
  print(coordinatesRef)
  for i in range(len(coordinatesRef)):
    g.append("x - {}".format(coordinates[coordinatesRef[i]][0]))
    h.append("{} - {}".format(coordinates[j][0], coordinates[coordinatesRef[i]][0]))
  print(g)
  print(h)
  g = []
  h = []
  coordinatesRef = index.copy()



'''
coordinates -> Quando i = 0, deleta o item de índice 0 de coordinates e 
utiliza o restante no numerador 


'''


