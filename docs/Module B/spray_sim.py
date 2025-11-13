# spray_sim.py
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
rho = 1000           # kg/m³, water density
Cd  = 0.62           # discharge coefficient
P   = 2e5            # Pa (2 bar)
D   = 2.13e-3        # m, nozzle diameter
A   = np.pi * (D**2) / 4

# Flow rate (m³/s)
Q = Cd * A * np.sqrt(2 * P / rho)
L_min = Q * 60000
print(f"Flow rate: {L_min:.2f} L/min")

# Droplet velocity model
v_exit = np.sqrt(2 * P / rho)
time = np.linspace(0, 3, 300)
y = 4 - 0.5 * 9.81 * time**2      # 4 m initial height
valid = y > 0

plt.figure()
plt.plot(time[valid], y[valid])
plt.title('Droplet Free Fall from 4 m Height')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()
