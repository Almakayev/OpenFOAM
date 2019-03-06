import math

L = 1.06
R = 0.012
x0 = 1.5e-04
Nx = 100
Ny = 50
CFL = 0.8

T0 = 300
R_const = 286.8
gamma = 1.4
a0 = math.sqrt(gamma * R_const * T0)
print("Sound speed %f " % a0)

res_freq = 0.5 * a0 / L 
print("Resonance frequency %f " % res_freq)
freq = 1.0 * res_freq
print("Frequency %f " % freq)
omega = 2 * math.pi * freq
u0 = omega * x0
print("U0 %f " % u0)
print("Cyclic freq omega %f " % omega)
period = 1 / freq
print("Period Tw %f " % period)

dx = L / Nx
dy = R / Ny
dksi = 1 / (1 / dx + 1 / dy)
dt = CFL / a0 * dksi
print("Timestep %.8f " % dt)

print("Write interval to file %f " % (period / dt / 30))
print("100 periods %f " % (100 * period))
