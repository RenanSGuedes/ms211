from sympy.abc import x, y, _clash1
from sympy import sympify, expand, simplify

coordinates = [] 

i = input()
while i != '':
    coordinates.append([int(s) for s in i.split()])
    i = input()

idx = int(input("Índice: "))
xk = int(input("xk = "))
index = []
for i in range(idx + 1):
  index.append(i)

print(index)

coordinatesRef = index.copy()
l = []
g = []
h = []
r = []
pList = []
lagrangeList = []

for j in range(len(index)):
  del coordinatesRef[j]
  for i in range(len(coordinatesRef)):
    g.append("(x - {})".format(coordinates[coordinatesRef[i]][0]))
    h.append("({} - {})".format(coordinates[j][0], coordinates[coordinatesRef[i]][0]))
  numerador = expand("*".join(str(x) for x in g))
  denominador = expand("*".join(str(x) for x in h))
  lagrange = expand(numerador/denominador)
  lagrangeList.append(lagrange)
  g = []
  h = []
  coordinatesRef = index.copy()

for i in range(len(lagrangeList)):
  pList.append(lagrangeList[i] * coordinates[i][1])
  result = expand("+".join(str(x) for x in pList))

print("Para xk = {} => P(x) = {}".format(xk, result.subs(x, xk)))
print("P(x) = {}".format(simplify(result)))