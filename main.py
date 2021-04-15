import numpy as np
import matplotlib.pyplot as plt

#parametry sterujące
c = 0
f = 0

#geometria
x_a = 0
x_b = 1



WEZLY = np.array([[1, 0],
                  [2, 1],
                  [3, 0.5],
                  [4, 0.75]])

ELEMENTY = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [4, 3, 4]])

#warunki brzegowe
twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1

#funkcja generująca geometrie
def generujTabliceGeometrii(x_0,x_p, n):
    temp = (x_p - x_0) / (n - 1)
    matrix = np.array([0, 0 * temp+x_0])

    for i in range(1, n, 1):
        matrix = np.block([
            [matrix],
            [i, i * temp+x_0],
        ])
    return matrix

def rusujGeom():
    return 0
