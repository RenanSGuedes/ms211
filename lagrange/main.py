from sympy.abc import x, y, _clash1
from sympy.plotting import plot
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

coordinates = [] # Armazena as coordenadas do input construindo umas lista da forma [(P1), (P2), ..., (Pn)]

print('Coordenadas (Duplo <enter> finaliza o input)')
print('x y')
i = input()
while i != '':
    coordinates.append([float(s) for s in i.split()])
    i = input()

idx = int(input("Grau (De 1 a {}): ".format(len(coordinates) - 1))) # Limita o intervalo do input em função do número de coordenadas fornecidos
xk = float(input("xk = ")) # Valor de x a ser substituido no polinômio P(x) obtido em result
index = [] # Recebe os índices como número inteiro a partir da quantidade de coordenadas
for i in range(idx + 1):
  index.append(i)

coordinatesRef = index.copy() # Lista cópia do índice sujeita a alterações no próximo laço for
g = [] # Armazena os fatores do numerador de cada L calculado
h = [] # Armazena os fatores do denominador de cada L calculado
pList = [] # Armazena os produtos yn * Ln(x)
lagrangeList = [] # Armazena os valores de Ln(x) calculados para todas as combinações de xi

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
  result = expand("+".join(str(x) for x in pList)) # Armazena o polinômio que interpola o conjunto de pontos

print("Para xk = {} => P(x) = {}".format(xk, result.subs(x, xk)))
print("P(x) = {}".format(simplify(result)))

x_coordinates = [] # Armazena a posição de x para cada sublista de coordinates
y_coordinates = [] # Armazena a posição de y para cada sublista de coordinates

for i in range(len(coordinates)):
  x_coordinates.append(coordinates[i][0])

for i in range(len(coordinates)):
  y_coordinates.append(coordinates[i][1])

interval = np.linspace(coordinates[0][0], coordinates[-1][0], num=100)
fx = []
for i in range(len(interval)):
  fx.append(result.subs(x, interval[i]))

plt.plot(interval, fx, color='b')
plt.grid(True, linewidth=.5, linestyle='--', color='r')
plt.scatter(x_coordinates, y_coordinates, color='g')
plt.show()