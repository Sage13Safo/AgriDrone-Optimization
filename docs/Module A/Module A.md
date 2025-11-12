# 🧩 Module A — Design & Prototyping  
*(AgriDrone Optimization — BRICS Russia Future Skills Challenge 2025)*  

---

## 1. Objective  
Design and demonstrate an **agricultural drone spray system** using a **custom nozzle prototype** optimized for uniform coverage, low drift, and efficient payload utilization.

---

## 2. System Overview  

| Component | Function | Status |
|------------|-----------|---------|
| **Nozzle** | Atomizes liquid into fine droplets for uniform spray | ✅ Designed |
| **Pump & Pipe Network** | Maintains flow rate and pressure | 🕓 Prototype planning |
| **Drone Frame** | Carries 30 L payload and distributes load evenly | ✅ Basic CAD modeled |
| **Control Electronics** | Synchronizes pump + flight control | ⏳ To be added later |

---

## 3. Nozzle Variants and Parameters  

| Variant | Orifice Diameter (mm) | Flow Rate (L/min) | Pressure (bar) | Comment |
|----------|----------------------|-------------------|----------------|----------|
| **A1** | 0.5 | 1.2 | 1.5 | Fine mist, light coverage |
| **A2** | 1.5 | 2.7 | 2.0 | Balanced atomization |
| **A3** | 2.5 | 4.0 | 2.5 | Heavy flow, coarse spray |

### Selection Justification  
Simulation and manual calculations show **~2.13 mm** gives optimal flow rate (~2.7 L/min) that supports a **30 L/Ha** target application within **10–15 min** flight.  
This value minimizes drift while ensuring full coverage, balancing droplet momentum and dispersion.

---

## 4. Design Description  

### 4.1. 3D Modeling  
Created in **SOLIDWORKS**. Assembly includes:
- Four-nozzle system mounted to drone boom
- Pump housing and filter
- Liquid tank, motor mount, and delivery tubing

Upload location:  
📁 `/module_A_design_prototyping/design/CAD_Files/`  

### 4.2. Drawings & Renders  
- Exploded and assembled views (PDFs)  
- Nozzle detailed drawings for A1, A2, A3 (with dimensions)  
- High-resolution KeyShot renders  

Upload location:  
📁 `/module_A_design_prototyping/design/Renders/`  
📁 `/module_A_design_prototyping/design/Drawings/`  

---

## 5. Calculations Summary  

**Flow Rate Equation**  
\[
Q = C_d \cdot A \cdot \sqrt{\frac{2 \cdot \Delta P}{\rho}}
\]
Where:  
- \(C_d = 0.62\) (discharge coefficient)  
- \(A = \frac{\pi D^2}{4}\) (orifice area)  
- \(\Delta P = 2.0 \times 10^5\) Pa  
- \(\rho = 1000\) kg/m³  

**Example (for 2.13 mm):**  
\( Q = 0.62 × π(2.13×10^{-3})^2/4 × √(2×2×10^5 / 1000) ≈ 2.7 L/min \)

---

## 6. Deliverables  

| Item | Description | File/Folder |
|------|--------------|-------------|
| Technical Description | Overview + calculations | `docs/A2_Technical_Description.md` |
| Bill of Materials | Drone + nozzle components | `docs/A3_BOM_and_Roles.md` |
| Rendered Model | KeyShot output | `design/Renders/` |
| Flow Simulation | SolidWorks internal CFD | `../module_B_testing_simulation/` |

---

## 7. Next Steps  
- ✅ Complete 3 nozzle variants in SolidWorks  
- 🕓 Run CFD (Module B) for droplet behavior and flow visualization  
- 🧮 Validate via Python spray simulation (Module B helper)  
- 🎞️ Export render + drawing for presentation (Module D)

---

**Author:** Sage13 Safo  
**Toolchain:** SolidWorks • KeyShot • Python (CFD validation)  
**Acknowledgment:** AMP CAD South Africa for SolidWorks Flow Simulation trial license  

---

> _“Precision agriculture starts from precision design.”_

