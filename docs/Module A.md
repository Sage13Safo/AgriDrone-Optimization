# 🛠️ Module A — Design & Prototyping

**Project:** AgriDrone Optimization — Scaled demonstration agricultural UAV sprayer  
**Focus:** Mechanical & electronic design, CAD deliverables, Bill of Materials (BOM), and design justification.

---

## 🔭 Objective
Design a lightweight, manufacturable UAV sprayer prototype optimized for uniform spray distribution and low drift. Provide CAD models, electronics schematics, BOM, and engineering rationale so Modules B–D can validate and deploy the design.

---

## ✅ Deliverables (Module A)
- `module_A_design_prototyping/docs/A1_Project_Brief.md` — project scope & constraints  
- `module_A_design_prototyping/docs/A2_Technical_Description.md` — CAD & subsystem details  
- `module_A_design_prototyping/docs/A3_BOM_and_Roles.md` — BOM (CSV) + role allocation  
- CAD folder: `module_A_design_prototyping/design/CAD_Files/` (upload your `.sldprt`, `.step`, `.stl`)  
- Electronics: `module_A_design_prototyping/electronics/` (KiCad files, BOM.csv)  
- Deliverable Pack: `module_A_design_prototyping/deliverables/ModuleA_Deliverable.pdf` (final assembled PDF)

> Note: Large files (CAD, renders) should be uploaded in the `design/` and `electronics/` folders. Leave `.md` files as linking/descriptive hubs only.

---

## 📐 Design Overview (Suggested Sections)
1. **System Summary** — short description of chassis, pump/nozzle subassembly, tank, gimbal/mount, and electronics.  
2. **Key Requirements** — payload, flight endurance, max flow rate, resolution of spray deposition, repeatability.  
3. **Mass Budget** — list component masses and center-of-gravity considerations.  
4. **Materials & Manufacturing Notes** — suggested materials (PLA/ABS/Carbon-fiber), fastener types, and tolerances.  
5. **Safety & Regulatory Notes** — weight class, recommended safety interlocks, and flight limits.

---

## 🧾 Example: Mass Budget Table (copy into `A2_Technical_Description.md`)
| Item | Qty | Unit Mass (g) | Total Mass (g) | Notes |
|------|-----:|--------------:|---------------:|-------|
| Airframe (3D printed) | 1 | 650 | 650 | hollow ribs |
| Pump (diaphragm) | 1 | 120 | 120 | selectable flow rates |
| Nozzle assembly | 1 | 30 | 30 | quick-swap nozzle mount |
| Tank (PET) | 1 | 200 | 200 | 2 L nominal |
| Electronics (flight controller + ESCs) | 1 | 220 | 220 | include harness |
| Battery (LiPo) | 1 | 500 | 500 | capacity sized for mission |
| **Total (est.)** |   |     | **1720 g** | exclude payload margin |

---

## 🧾 Example BOM CSV (place in `module_A_design_prototyping/electronics/BOM.csv`)
```csv
part_id,description,qty,unit_price_usd,supplier,part_number
PUMP-01,Diaphragm Pump,1,12.50,SupplierA,PMP-1234
NOZ-001,Standard Flat-Fan Nozzle,2,3.00,SupplierB,NZ-FLAT-06
FC-STM32,Flight Controller (STM32),1,45.00,SupplierC,FC-STM32V2
BAT-2200,LiPo 2200mAh 3S,1,18.00,SupplierD,BAT-3S2200
