import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, ifft2


def convolve_fft(field, filter):
    fr = fft2(field)
    fr2 = fft2(np.flipud(np.fliplr(filter)))
    height, width = fr.shape
    conv = np.real(ifft2(fr*fr2))
    conv = np.roll(conv, -height//2+1, axis=0)
    conv = np.roll(conv, -width//2+1, axis=1)
    return conv


def update(field):
    height, width = field.shape
    filter = np.zeros((height, width))
    filter[height // 2 - 1: height // 2 + 2, width // 2 - 1: width // 2 + 2] = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    neighbors = convolve_fft(field, filter).round()
    f = np.zeros(neighbors.shape)

    f[np.where((neighbors == 2) & (field == 1))] = 1
    f[np.where((neighbors == 3) & (field == 1))] = 1
    f[np.where((neighbors < 2) & (field == 1))] = 0
    f[np.where((neighbors > 3) & (field == 1))] = 0
    f[np.where((neighbors == 3) & (field == 0))] = 1

    return f


height, width = 15, 15
A = np.random.random(height*width).reshape((height, width)).round()

plt.figure()

img_plot = plt.imshow(A, cmap='Accent', interpolation='nearest')
plt.show()

while True:
    A = update(A)
    img_plot = plt.imshow(A, cmap='Accent', interpolation='nearest')
    plt.draw()
    plt.show()
