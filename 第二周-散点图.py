# -*- encoding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.rcParams["font.sans-serif"] = ["SimSun"]
plt.rcParams["axes.unicode_minus"] = False
n = 1000
r = np.random.uniform(-50, 50, size=2*n)
r = np.copy(np.reshape(r, (2, n)))
velocity1 = np.zeros((2, n))


def v1():
    vel = np.random.uniform(0, 2 * np.pi, size=n)
    r2 = np.random.uniform(0, 1, size=n)
    velocity1[0, :] = r2*np.cos(vel)
    velocity1[1, :] = r2*np.sin(vel)
    return velocity1


def gravity(r):
    x = r[0, :]
    y = r[1, :]
    g = np.zeros((2, n))
    index = x**2 + y**2 > 0.1
    g[0, index] = -x[index]*10/((x[index]**2+y[index]**2)**1.5)
    g[1, index] = -y[index]*10/((x[index]**2+y[index]**2)**1.5)
    return g


velocity2 = np.zeros((2, n))


def v2(velocity2):
    g = gravity(r)
    velocity2 += g*0.001
    return velocity2


def dr1(velocity1, velocity2):
    dr = (velocity1 + velocity2)*0.001
    return dr


for i in tqdm(range(100000)):
    velocity1 = v1()
    velocity2 = v2(velocity2)
    dr = dr1(velocity1, velocity2)
    r += dr
fig = plt.figure(dpi=250)
plt.scatter(r[0, :], r[1, :], s=5)
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.title("黑洞引力下的游走")
plt.tight_layout()
plt.show()
