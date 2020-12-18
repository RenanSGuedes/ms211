from sympy.abc import x, y, _clash1
from sympy.plotting import plot
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

coord = []

print('Coordenadas (Duplo <enter> finaliza o input)')
print('x y')
i = input()
while i != '':
    coord.append([float(s) for s in i.split()])
    i = input()

index = int(input("Índice: (De 1 a {}): ".format(len(coord) - 1)))
xk = float(input("xk = "))

deltas = [[] for _ in range(len(coord) - 1)]

for i in range(len(coord) - 1):
  deltas[0].append(round((coord[i + 1][1] - coord[i][1])/(coord[i + 1][0] - coord[i][0]), 3))

for k in range(len(deltas) - 1):
  for i in range(len(deltas[k]) - 1):
    deltas[k + 1].append(round((deltas[k][i + 1] - deltas[k][i])/(coord[i + 2 + k][0] - coord[i][0]), 3))

firstItem = [item[0] for item in deltas]
firstItem.insert(0, coord[0][1])

factors = []

for i in range(len(coord) - 1):
  factors.append('(x - {})'.format(coord[i][0]))

newFactors = []

for i in range(len(factors)):
  newFactors.append(factors[:i + 1])

newFactConc = ['*'.join(sub_list) for sub_list in newFactors]
print(newFactConc)

finalFactors = []

for i in range(1, index + 1):
  finalFactors.append('{}*{}'.format(newFactConc[i - 1], firstItem[i]))

parseResult = "{}+".format(coord[0][1]) + '+'.join(finalFactors)

result = sympify(parseResult, locals=_clash1)

print("Para xk = {} => p({}) = {}".format(xk, xk, round(result.subs(x, xk), 3)))
print("p(x) = {}".format(expand(result)))

x_coord = [] 
y_coord = []

for i in range(len(coord)):
  x_coord.append(coord[i][0])

for i in range(len(coord)):
  y_coord.append(coord[i][1])

interval = np.linspace(coord[0][0], coord[-1][0], num=100)
fx = []
for i in range(len(interval)):
  fx.append(result.subs(x, interval[i]))

plt.plot(interval, fx, color='b')
plt.grid(True, linewidth=.5, linestyle='--', color='r')
plt.scatter(x_coord, y_coord, color='g')
plt.show()
print("Feche a aba da plotagem para encerrar o programa.")
