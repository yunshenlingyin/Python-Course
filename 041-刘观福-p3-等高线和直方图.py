import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.tri as tri

# 解决中文显示的问题，SimSun是宋体，下一行解决的是显示负号的问题，改成‘True’，不显示
# 坐标轴上的负号
plt.rcParams["font.sans-serif"] = ["SimSun"]
plt.rcParams["axes.unicode_minus"] = False
n = 1000
r = np.random.uniform(-50, 50, size=2 * n)
r = np.copy(np.reshape(r, (2, n)))
velocity1 = np.zeros((2, n))
velocity2 = np.zeros((2, n))


def v1():
    vel = np.random.uniform(0, 2 * np.pi, size=n)
    r2 = np.random.uniform(0, 1, size=n)
    velocity1[0, :] = r2 * np.cos(vel)
    velocity1[1, :] = r2 * np.sin(vel)
    return velocity1


def gravity(r):
    x = r[0, :]
    y = r[1, :]
    g = np.zeros((2, n))
    index = x ** 2 + y ** 2 > 0.1
    g[0, index] = -x[index] * 10 / ((x[index] ** 2 + y[index] ** 2) ** 1.5)
    g[1, index] = -y[index] * 10 / ((x[index] ** 2 + y[index] ** 2) ** 1.5)
    return g


def v2(velocity2):
    g = gravity(r)
    velocity2 += g * 0.001
    return velocity2


def dr1(velocity1, velocity2):
    dr = (velocity1 + velocity2) * 0.001
    return dr


for i in tqdm(range(100000)):
    velocity1 = v1()
    velocity2 = v2(velocity2)
    dr = dr1(velocity1, velocity2)
    r += dr

fig1, axScatter = plt.subplots(figsize=(7.0, 7.0))
x = r[0, :]
y = r[1, :]
axScatter.scatter(x, y, s=5)
axScatter.set_aspect(1.)

# create new axes on the right and on the top of the current axes
# The first argument of the new_vertical(new_horizontal) method is
# the height (width) of the axes to be created in inches.
divider = make_axes_locatable(axScatter)
axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=axScatter)
axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=axScatter)

# make some labels invisible
plt.setp(axHistx.get_xticklabels() + axHisty.get_yticklabels(),
         visible=True)

# now determine nice limits by hand:
binwidth = 5
xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
lim = (int(xymax / binwidth) + 1) * binwidth

bins = np.arange(-lim, lim + binwidth, binwidth)
axHistx.hist(x, bins=bins, density=True)
axHisty.hist(y, bins=bins, density=True, orientation='horizontal')

# the xaxis of axHistx and yaxis of axHisty are shared with axScatter,
# thus there is no need to manually adjust the xlim and ylim of these
# axis.

# axHistx.axis["bottom"].major_ticklabels.set_visible(False)
for tl in axHistx.get_xticklabels():
    tl.set_visible(True)
axHistx.set_yticks(np.arange(0, 40, 10) * 0.001)

# axHisty.axis["left"].major_ticklabels.set_visible(False)
for tl in axHisty.get_yticklabels():
    tl.set_visible(True)
axHisty.set_xticks(np.arange(0, 50, 20) * 0.001)
plt.draw()
plt.show()

# 因为x，y是不规则的网格数据，需要处理一下
xi = np.linspace(x.min(), x.max(), 1000)
yi = np.linspace(y.min(), y.max(), 1000)
z = ((velocity1[0, :] + velocity2[0, :]) ** 2 + (velocity1[1, :] + velocity2[1, :]) ** 2) #** 0.5
# Perform linear interpolation of the data (x,y)
# on a grid defined by (xi,yi)
triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)
fig2 = plt.figure(dpi=250)
# cntr1 = plt.contourf(Xi, Yi, zi, levels=16, cmap="RdBu_r")
# plt.contour(Xi, Yi, zi, levels=16, linewidths=0.5, colors='k')
lim = np.linspace(z.min(), z.max(), 16)
cntr1 = plt.contourf(Xi, Yi, zi, lim, cmap="RdBu_r")
plt.contour(Xi, Yi, zi, lim, linewidths=0.5, colors='k')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
#fig2.colorbar(cntr1)#, ax=ax1)
#plt.subplots_adjust(hspace=0.5)
plt.colorbar(cntr1)
plt.show()
