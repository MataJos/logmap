#---
# file: app.py
# purpose: plots logistic map
# author: Josue Mata <jamalugo17@gmail.com>
# license: GPLv3
#---

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# ---- define functions -----
def mapeo_logistico(x_n: float, r: float) -> float:
    return r*x_n*(1-x_n)


def punto_fijo(x0, r1):

    x_1 = x0
    r_1 = r1
    for i in range(1000):
        x_1 = mapeo_logistico(x_1, r_1)
    return x_1


A = np.zeros((1000, 4000), dtype = float)
list_r = np.linspace(0, 4, num=4000)
list_x = np.linspace(0, 1, num=1000)


for i in range(1000):
    for j in range(4000):
        A[i, j] = punto_fijo(list_x[i], list_r[j])


B = np.zeros((4000, 1000),dtype=float)
r = list_r

for j in range(1000):
    for i in range(4000):
        B[i, j] = A[j, i]


ax = plt.figure("Diagrama de Bifurcacion 1", figsize=(40, 10))
plt.subplot()


for i in range(1000):
    plt.scatter(r, B[:, i], s=0.0006, c="black")
