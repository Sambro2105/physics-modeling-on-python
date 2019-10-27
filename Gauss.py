# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:36:44 2019

@author: Iakunin.Sergey
"""
import pylab as plt
import numpy as np
from scipy.optimize import curve_fit


def gauss(x, a, x0, sigma):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma))


x = list(range(1, 9))
y = [1, 3, 5, 7, 5, 2, 1, 0]
popt, pcov = curve_fit(gauss, x, y)

dots = np.linspace(1, 10, 100)
plt.plot(dots, gauss(dots, *popt), label = 'Нормальное распределение')
plt.plot(x, y, 'k', label = 'Ломанная кривая')
plt.legend()
plt.show()
                    