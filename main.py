from sympy.abc import x, y, _clash1
from sympy import sympify, expand, simplify

coordinates = [(1, 0), (2, 1), (3, 4), (5,6), (7,8)] 
index = [0, 1, 2, 3, 4] # 0, 1, 2
coordinatesRef = index.copy()
l = []
g = []
h = []
r = []

pList = []

lagrangeList = []

for j in range(len(index)):
  del coordinatesRef[j]
  print(coordinatesRef)
  for i in range(len(coordinatesRef)):
    g.append("(x - {})".format(coordinates[coordinatesRef[i]][0]))
    h.append("({} - {})".format(coordinates[j][0], coordinates[coordinatesRef[i]][0]))
  print(g)
  print(h)
  numerador = expand("*".join(str(x) for x in g))
  denominador = expand("*".join(str(x) for x in h))
  print(numerador)
  print(denominador)
  lagrange = expand(numerador/denominador)
  lagrangeList.append(lagrange)
  print(lagrangeList)
  g = []
  h = []
  coordinatesRef = index.copy()


for i in range(len(lagrangeList)):
  pList.append(lagrangeList[i] * coordinates[i][1])
  result = expand("+".join(str(x) for x in pList))

print("+".join(str(x) for x in pList))
print(simplify(result))


