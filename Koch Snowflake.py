# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:32:19 2019

@author: Iakunin.Sergey
"""
import numpy as np
import matplotlib.pyplot as plt


def Build_triangle(point1, point2):
    a = point1[0]
    b = point1[1]
    c = point2[0]
    d = point2[1]
    e = (2 * a + c) / 3
    f = (2 * b + d) / 3
    i = (a + 2 * c) / 3
    j = (b + 2 * d) / 3
    g = 0.5 * (i + e) - (np.sqrt(3) / 2) * (j - f)
    h = (np.sqrt(3) / 2) * (i - e) + 0.5 * (j + f)
    return [(e, f), (g, h), (i ,j)]

def Koch_iteration(Koch_snowflake):
    iterations = len(Koch_snowflake) - 1
    for i in range(iterations):
        p1 = 4 * i
        p2 = p1 + 1
        point1 = Koch_snowflake[p1]
        point2 = Koch_snowflake[p2]
        triangle = Build_triangle(point1, point2)
        Koch_snowflake[p2:p2] = triangle

def Build_snowflake(Koch_snowflake, depth):
    for i in range(depth):
        Koch_iteration(Koch_snowflake)

def Paint_snowflake(Koch_snowflake, depth):
    Build_snowflake(Koch_snowflake, depth)
    length = len(Koch_snowflake)
    x = [Koch_snowflake[i][0] for i in range(length)]
    y = [Koch_snowflake[i][1] for i in range(length)]
    plt.plot(x, y, 'b-')
    plt.show()
    
    
# Глубина снежинки
depth = 4

# Координаты точек для первого треугольника
Koch_snowflake = [(-1, 0), (0, np.sqrt(3)), (1, 0), (-1, 0)]

Paint_snowflake(Koch_snowflake, depth)
