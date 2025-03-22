import numpy as np
import matplotlib.pyplot as plt

# definition of constants
nx = 100
ny = 100
dx = 0.01
dy = dx
fp = 10**9
wp = 2*np.pi*fp
vc = wp/1000
w0 = wp/np.sqrt(2)
dt = dx/(6*10**8)
c0 = 3*10**8

y1 = 40  # start of material
y2 = 70  # end of material
sx = 50  # x position of source
sy = 25  # y position of source

# constants of Mur conditions
A = (c0 * dt - dx)/(c0*dt + dx)
B = 2*dx/(c0*dt + dx)
C = (c0*dt)**2/(2*dx*(c0*dt + dx))

# constants of ADE equations
c1 = (wp**2)*dt/vc
c2 = (1-0.5*dt*vc)/(1+0.5*dt*vc)

# definition of EM fields and auxiliary fields,
# with initialization to zero
Dz = np.zeros((nx, ny))
Ez = np.zeros((nx, ny))
Hx = np.zeros((nx, ny))
Bx = np.zeros((nx, ny))
Hy = np.zeros((nx, ny))
By = np.zeros((nx, ny))
Ix = np.zeros((nx, ny))
Iy = np.zeros((nx, ny))
Iz = np.zeros((nx, ny))
Sx = np.zeros((nx, ny))
Sy = np.zeros((nx, ny))
Sz = np.zeros((nx, ny))
Ez_n = np.zeros((nx, ny))
Ez_n_1 = np.zeros((nx, ny))

time_steps = 700
t = 0.0
time_step = 1
while time_step <= time_steps:
    t = time_step*dt

    # update Dz
    for i in range(1, nx):
        for j in range(1, ny):
            Dz[i, j] += 0.5*(Hy[i, j] - Hy[i-1, j] - Hx[i, j]
                             + Hx[i, j-1])

    # pulse of the source
    Dz[sx, sy] = np.sin(w0*t)

    # update Ez
    for i in range(nx):
        for j in range(ny):
            if (j < y1) or (j > y2):  # outside of material
                Ez[i, j] = Dz[i, j]
            else:  # inside the material
                Ez[i, j] = Dz[i, j] - Iz[i, j] - c2*Sz[i, j]
                Iz[i, j] += c1*Ez[i, j]
                Sz[i, j] = c2*Sz[i, j] - c1*Ez[i, j]

    # Mur conditions
    for j in range(ny):
        # x=0
        Ez[0, j] = - Ez_n_1[1, j] + A * (Ez[1, j] + Ez_n_1[0, j]) \
                   + B * (Ez_n[0, j] + Ez_n[1, j])
        # x=nx-1
        Ez[nx - 1, j] = -Ez_n_1[nx - 2, j] \
                        + A * (Ez[nx - 2, j] + Ez_n_1[nx - 1, j]) \
                        + B * (Ez_n[nx - 1, j] + Ez_n[nx - 2, j])
    for i in range(nx):
        # y=0
        Ez[i, 0] = - Ez_n_1[i, 1] + A * (Ez[i, 1] + Ez_n_1[i, 0]) \
                   + B * (Ez_n[i, 0] + Ez_n[i, 1])
        # y=ny-1
        Ez[i, ny - 1] = -Ez_n_1[i, ny - 2] \
                        + A * (Ez[i, ny - 2] + Ez_n_1[i, ny - 1]) \
                        + B * (Ez_n[i, ny - 1] + Ez_n[i, ny - 2])

    # update Bx
    for i in range(nx):
        for j in range(ny-1):
            Bx[i, j] += 0.5 * (Ez[i, j] - Ez[i, j+1])

    # update By
    for i in range(nx-1):
        for j in range(ny):
            By[i, j] += 0.5 * (Ez[i+1, j] - Ez[i, j])

    # update Hx, Hy
    for i in range(nx):
        for j in range(ny):
            if (j < y1) or (j > y2):  # outside of material
                Hx[i, j] = Bx[i, j]
                Hy[i, j] = By[i, j]
            else:  # inside the material
                Hx[i, j] = Bx[i, j] - Ix[i, j] - c2 * Sx[i, j]
                Ix[i, j] += c1 * Hx[i, j]
                Sx[i, j] = c2 * Sx[i, j] - c1 * Hx[i, j]

                Hy[i, j] = By[i, j] - Iy[i, j] - c2 * Sy[i, j]
                Iy[i, j] += c1 * Hy[i, j]
                Sy[i, j] = c2 * Sy[i, j] - c1 * Hy[i, j]

    # update auxiliary fields
    Ez_n_1 = Ez_n.copy()
    Ez_n = Ez.copy()

    # for me
    print(time_step)
    time_step += 1

# Plotting
plt.imshow(Ez.T, cmap='RdBu', interpolation='bilinear',
           origin='lower', extent=[0, nx, 0, ny])
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Ez field snapshot {time_step-1}")
plt.show()
