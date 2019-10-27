# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:13:23 2019

@author: Iakunin.Sergey
"""

import numpy as np
import matplotlib.pyplot as plt


L = 1000                                  #dimension N
minJ = 5
maxJ = 30
Eps = 0.0001

#print matrix in pretty manner
def MPrint(M):
    for i in M:
        ss = ["%.03f"%f for f in i]
        print("\t".join(ss))

#generate Krylov matrix
def Lanczos1(A, maxJ):
    w = np.random.rand(L) - 0.5
    w /= np.linalg.norm(w)
    Q = [w]
    r = 1
    z = w
    while (r > Eps) and (len(Q) < maxJ):
        z = np.dot(A, z)                  #z = A * z
        for v in Q:
            z -= np.dot(z, v) * v         #to leave only a relevant part
        r = np.linalg.norm(z)
        z /= r                            #to norm z
        Q.append(z)
    Q = np.array(Q)                       #turn Q into numpy array
    T = np.dot(Q, np.dot(A, Q.T))         #T = Q.T * A * Q
    TVal, TVec = np.linalg.eig(T)
    return (TVal, TVec)

#generate symmetric matrix A
A = np.random.rand(L, L) - 0.5
A = (A + A.T) * 0.5

AVal, AVec = np.linalg.eig(A)
AVal = np.sort(AVal)
for i in range(10):
    plt.plot([minJ, maxJ], [AVal[i], AVal[i]], 'b-')
    plt.plot([minJ, maxJ], [AVal[-i], AVal[-i]], 'b-')

for i in range(minJ, maxJ + 1):
    x = [i for j in range(i)]
    y = np.sort(Lanczos1(A, i)[0])
    plt.plot(x, y, '.')
    
plt.show()
