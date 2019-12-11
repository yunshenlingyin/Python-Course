# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams["font.sans-serif"] = ["SimSun"]
plt.rcParams["axes.unicode_minus"] = False

# Plot functions
x1 = np.linspace(-16, 16, 2000)
x2 = np.linspace(1, 20, 2000)
x3 = np.linspace(10.00, 20, 600)
fig = plt.figure(figsize=(10, 12))
plt.plot(x1, x1, label=r"$N$")
plt.plot(x2, np.sqrt(x2), label=r"$N^{2}$")
plt.plot(x2, x2 ** 1.5, label=r"$N_{1.5}$")
plt.plot(x2, x2 * np.log(x2), color="red", linestyle="-.", label=r"$Nln(N)$")
plt.plot(x3, x3 * np.log(np.log(x3)), label=r"$Nln(lnN))$")
plt.plot(x2, x2 * np.log(x2) ** 2, label=r"$Nln^{2}N$")
plt.plot(x2, x2 * np.log(x2 ** 2), color="red", linestyle="-.", label=r"$Nln(N^{2})$")
plt.plot(x1[:1000], 2 / x1[:1000], x1[1000:], 2 / x1[1000:], label=r"$\frac{2}{N}$")
plt.plot(x1, 2 ** x1, label=r"$2^{N}$")
plt.plot(x1, 2 ** (x1 / 2), label=r"$2^{\frac{N}{2}}$")
plt.plot(x2, x2 ** 2 * np.log(x2), label=r"$N^{2}lnN$")
plt.plot(x1, x1 ** 3, label=r"$N^{3}$")
plt.legend(fontsize="large")
plt.ylim(-20, 20)
plt.xlim(-20, 20)
ax = plt.gca()
ax.spines["right"].set_visible(False)
# ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))
plt.grid()
plt.ion()
plt.show()


# Time cost analysis
def find_time(N, func):
    # Input the N and function, return the time  the function with the parameter N takes
    start0 = time.time()
    func(N)
    end0 = time.time()
    elapse0 = end0 - start0
    return elapse0


def sum1(N):
    # Time complexity: O(N)
    sum10 = 0
    for i in range(N):
        sum10 += 1
    return sum10


def sum2(N):
    # Time complexity: O(N^2)
    sum20 = 0
    for i in range(N):
        for j in range(N):
            sum20 += 1
    return sum20


def sum3(N):
    # Time complexity: O(N^3)
    sum30 = 0
    for i in range(N):
        for j in range(N*N):
            sum30 += 1
    return sum30


def sum4(N):
    # Time complexity: O(N^2)
    sum40 = 0
    for i in range(N):
        for j in range(i):
            sum40 += 1
    return sum40


def sum5(N):
    # Time complexity: O(N^5)
    sum50 = 0
    for i in range(N):
        for j in range(i*i):
            for k in range(j):
                sum50 += 1
    return sum50


def sum6(N):
    # Time complexity: O(N^5)
    sum60 = 0
    for i in range(N):
        for j in range(i*i):
            if j % i == 0:
                for k in range(j):
                    sum60 += 1
    return sum60


elapse = find_time(1000, sum1)
print("{0:-<40.6f}".format(elapse))


# Fast power algorithm
def fast_power(base, power):
    result = 1
    while power:
        if power & 1:
            result *= base
        base *= base
        power >>= 1
    return result
