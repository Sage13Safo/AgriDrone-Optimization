# 🌬️ Module B — Testing & Simulation  
*(AgriDrone Optimization — BRICS Russia Future Skills Challenge 2025)*  

---

## 1. Objective  
Validate the designed nozzle system using **SolidWorks Flow Simulation** and complementary **Python modeling** to predict and visualize droplet and airflow behavior.

---

## 2. Simulation Overview  

| Method | Tool | Purpose |
|--------|------|----------|
| **Internal Flow (CAD CFD)** | SolidWorks Flow Simulation | Simulate atomization and internal pressure distribution |
| **External Domain (Environment)** | SolidWorks (4 m spray height box) | Visualize droplet dispersion and drift |
| **Python Model** | NumPy + Matplotlib | Predict flow rate, droplet velocity, and coverage profile |

---

## 3. SolidWorks CFD Setup  

**3.1 Computational Domain:**  
- Enclosure box: *4 m × 4 m × 2 m*  
- Air velocity inlet: 0 m/s (still air baseline)  
- Gravity: 9.81 m/s² (downward Y-axis)  
- Liquid inlet: defined by nozzle outlet (2.13 mm orifice)  

**3.2 Boundary Conditions:**  
- Inlet: volumetric flow (2.7 L/min)  
- Outlet: pressure = 0 Pa  
- Wall: no-slip, adiabatic  
- Environment: standard atmosphere (25 °C, 1 atm)  

**3.3 Droplet Injection (Particle Study):**  
- Particle type: water droplet  
- Mean diameter: 120 μm  
- Particle count: 2000 (uniform)  
- Track time: 3 s  

Upload your SolidWorks simulation package here:  
📁 `/module_B_testing_simulation/simulation/solidworks_flow/`  

---

## 4. Python Flow Model  

To complement the CAD CFD, this Python script approximates nozzle flow and droplet trajectory for verification.

```python
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

