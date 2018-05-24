import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate  import griddata

#Y, X = np.mgrid[0:1:100j, 0:1:100j]
#U = -1 - X**2 + Y
#V = 1 + X - Y**2

x = np.loadtxt("x.txt")
y = np.loadtxt("y.txt")
u = np.loadtxt("u.txt")
v = np.loadtxt("v.txt")

# (N, 2) arrays of input x,y coords and u,v values
pts = np.vstack((x, y)).T
vals = np.vstack((u, v)).T

# the new x and y coordinates for the grid, which will correspond to the
# columns and rows of u and v respectively
nx, ny = 200, 150

xi = np.linspace(0, 1, nx)
yi = np.linspace(1, 0, ny)
#xi = x[0:nx*ny:nx]
#yi = y[0:ny]


# an (nx * ny, 2) array of x,y coordinates to interpolate at
ipts = np.vstack(a.ravel() for a in np.meshgrid(yi, xi)[::-1]).T

# an (nx * ny, 2) array of interpolated u, v values
ivals = griddata(pts, vals, ipts, method='cubic')

# reshape interpolated u,v values into (ny, nx) arrays
ui, vi = ivals.T
ui.shape = vi.shape = (ny, nx)

#speed = np.sqrt(U*U + V*V)

fig, ax = plt.subplots(1, 1)
ax.hold(True)
ax.streamplot(xi, yi, ui, vi)
#ax.quiver(x, y, u, v)
plt.show()