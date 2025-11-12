#  AgriDrone Optimization  
**Solo UAV Sprayer Design, Simulation & ROI Analysis**  
*BRICS Future Skills & Tech Challenge — 2025*  

---

##  Project Summary  

This project demonstrates the **design and computational analysis** of a small unmanned aerial vehicle (UAV)–based agricultural sprayer system.  
Developed by a **solo participant**, the system focuses on **nozzle optimization**, **spray uniformity**, and **cost efficiency** for small-scale farm use.  

The workflow combines **engineering calculations**, **3D CAD modeling**, and **flow simulations** in SolidWorks — supported by **Python scripts** for predicting droplet and flow behaviors.  
Renderings and ROI estimates complete the prototype demonstration.

---

##  Core Goals  

-  **Derive and justify nozzle parameters** using fluid mechanics equations.  
-  **Model three nozzle variants** (0.5 mm, 1.5 mm, 2.5 mm orifice) using SolidWorks.  
-  **Run CFD simulations** to visualize droplet velocity and pressure distribution.  
-  **Use Python** for analytical prediction of flow behavior and spray coverage.  
-  **Estimate economic efficiency** using ROI and cost models.  
-  **Prepare presentation visuals** with renders and animations.  

---
## 📐 Design Basis
---
| Parameter                | Symbol | Value           | Unit  | Description                    |
| ------------------------ | ------ | --------------- | ----- | ------------------------------ |
| Nozzle orifice diameters | d      | 0.5 / 1.5 / 2.5 | mm    | Three variants for comparison  |
| Drone altitude           | h      | 4               | m     | Above target surface           |
| Flow rate target         | Q      | 2.7             | L/min | Desired for 30 L/ha spray rate |
| Pressure differential    | ΔP     | 3×10⁵           | Pa    | Typical small pump             |
| Discharge coefficient    | Cₑ     | 0.7             | —     | Orifice efficiency             |
| Fluid density            | ρ      | 1000            | kg/m³ | Water                          |

---
##CFD Simulation Overview
----

- **Software**: SolidWorks Flow Simulation

- **Type**: Internal fluid flow with air domain enclosure

## Boundary conditions:

- Inlet pressure = 3×10⁵ Pa

- Outlet = atmospheric

- Injection: Water droplets, 100–200 μm

- Visualization: Velocity & pressure contours, heatmap plots, streamline animation





---
## Acknowledgments
- **SolidWorks Flow Simulation 7-Day TrialLicense** AMP CAD/CAM Solutions (Pty) Ltd, South Africa – Educational License) **Dassualt Systemes SOLIDWORKS Reseller**

- **Python Libraries**: NumPy, Matplotlib

- **Developed by**: Solo Participant — AgriDrone Optimization 2025

---
## Future Extensions
---

- Integration of pump-electronic control system (KiCAD or Fritzing diagram)

- Payload and motor selection optimization

- AI-based spray path planning

- Onboard camera for field pattern mapping

---
## Author
- **Name**: Sarfo Kusi
- **Role**: Solo Participant, BRICS Future Skills Challenge UAS 2025
- **Email**: dokwas13africa@gmail.com
- **Telephone/Telegran**: +233249213044/ @sage_13_safo



---
##  Repository Structure  

```text
AgriDrone-Optimization/
│
├── README.md
└── docs/
    ├── ModuleA/
    │   ├── ModuleA.md
    │   ├── nozzle_variants/
    │   ├── renders/
    │   └── drawings/
    │
    ├── ModuleB/
    │   ├── ModuleB.md
    │   ├── flow_sim/
    │   └── python_model/
    │
    ├── ModuleC/
    │   ├── ModuleC.md
    │   ├── roi_model.py
    │   └── charts/
    │
    └── ModuleD/
        ├── ModuleD.md
        ├── slides/
        └── video/
