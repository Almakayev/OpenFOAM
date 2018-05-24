import math

L = 1.06
R = 0.01825
x0 = 3e-04
Nx = 100
Ny = 100
CFL = 0.8

T0 = 296
R_const = 286.8
gamma = 1.4
a0 = math.sqrt(gamma * R_const * T0)
print "Sound speed", a0

freq = 0.5 * a0 / L
print "Frequency", freq
omega = 2 * math.pi * freq
u0 = omega * x0
print "U0 ", u0
print "Cyclic freq omega ", omega
period = 1 / freq
print "Period Tw", period

dx = L / Nx
dy = R / Ny
dksi = 1 / (1 / dx + 1 / dy)
dt = CFL / a0 * dksi
print "Timestep ", dt

print "Write control ", (period / dt / 30)
print "100 periods ", 100 * period
