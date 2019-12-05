# # # # -*- coding: utf-8 -*-
# # import numpy as np
# # import matplotlib.pyplot as plt
# # # from tqdm import tqdm
# # # n = 10000
# # # a1 = np.zeros((2, n))
# # # v2 = np.zeros((2,))
# # # # a1[0] = np.random.uniform(-50, 50)
# # # a1[:, 0] = np.array([np.random.uniform(-50, 50), np.random.uniform(-50, 50)])
# # # # a1[:,0] = np.array([-30, 0])
# # # for i in tqdm(range(n-1)):
# # #     r1 = np.random.uniform(0, 1)
# # #     r2 = np.random.uniform(0, 2*np.pi)
# # #     v1 = r1*np.array([np.cos(r2), np.sin(r2)])
# # #     v2 += -10*a1[:, i]/((a1[0, i]**2 + a1[1, i]**2)**1.5)*0.001
# # #     a1[:, i+1] = a1[:, i]+v1+v2
# # # fig = plt.figure(dpi=250)
# # # plt.scatter(a1[0, :], a1[1, :], s=0.5)
# # # plt.tight_layout()
# # #
# # # plt.show()
# # jk = np.arange(10)
# # lk = jk<6
# # jk[lk]=0
# import numpy as np
# import matplotlib.pyplot as plt
# from tqdm import tqdm
# import math
# samples_num=1000
# x2=np.arange(0,samples_num,1.0)
# y2=np.arange(0,samples_num,1.0)
# distance=np.arange(0,samples_num,1.0)
# ax=np.arange(0,samples_num,1.0)
# ay=np.arange(0,samples_num,1.0)
# vx=np.zeros((samples_num,))
# vy=np.zeros((samples_num,))
# x0 = np.random.uniform(size=samples_num)*100
# y0 = np.random.uniform(size=samples_num)*100
#
# #生成在100*100区域内随机均匀分布的1000个点
#
# for j in tqdm(range(500)):
# #让这1000个点在单位圆内随机运动
#     t = np.random.uniform(0,2*np.pi,size=samples_num)
#     x1 = np.cos(t)
#     y1 = np.sin(t)
#     len = np.random.uniform(0,1)
#     x1 = x1 * len
#     y1 = y1 * len
#     for i in range(1000):
#     #1000个粒子在中心引力势场下的运动
#         distance[i]=np.sqrt((x0[i]-50)**2+(y0[i]-50)**2)
#         if distance[i]>=0.1:
#             ax[i]=-10*(x0[i]-50)/(distance[i]**3)
#             ay[i]=-10*(y0[i]-50)/(distance[i]**3)
#         else:
#             ax[i]=0
#             ay[i]=0
#         vx[i]=vx[i]+ax[i]*0.001/2
#         vy[i]=vy[i]+ay[i]*0.001/2
#         x2[i]=vx[i]*0.001
#         y2[i]=vy[i]*0.001
#         x0[i]=x0[i]+x1[i]+x2[i]
#         y0[i]=y0[i]+y1[i]+y2[i]
# #最终结果
# plt.figure(figsize=(10,10.1),dpi=125)
# plt.scatter(x0, y0, s=5)
# # plt.xlim(0,100)
# # plt.ylim(0,100)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Random Scatter')
# plt.savefig('imag.png')
# plt.show()
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

np.random.seed(19680801)
npts = 200
ngridx = 100
ngridy = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)

fig, (ax1, ax2) = plt.subplots(nrows=2)

# -----------------------
# Interpolation on a grid
# -----------------------
# A contour plot of irregularly spaced data coordinates
# via interpolation on a grid.

# Create grid values first.
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

# Perform linear interpolation of the data (x,y)
# on a grid defined by (xi,yi)
triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

# Note that scipy.interpolate provides means to interpolate data on a grid
# as well. The following would be an alternative to the four lines above:
#from scipy.interpolate import griddata
#zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')


ax1.contour(xi, yi, zi, levels=14, linewidths=0.5, colors='k')
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")

fig.colorbar(cntr1, ax=ax1)
# ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('grid and contour (%d points, %d grid points)' %
              (npts, ngridx * ngridy))


# ----------
# Tricontour
# ----------
# Directly supply the unordered, irregularly spaced coordinates
# to tricontour.

ax2.tricontour(x, y, z, levels=14, linewidths=0.5, colors='k')
cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")

fig.colorbar(cntr2, ax=ax2)
# ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(-2, 2), ylim=(-2, 2))
ax2.set_title('tricontour (%d points)' % npts)

plt.subplots_adjust(hspace=0.5)
plt.show()
