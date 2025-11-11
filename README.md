# 🌾 AgriDrone Optimization (BRICS RUSSIA FUTURE SKILLS & TECH CHALLENGE UAS_Drones Hackathon 2025)

**Scaled demo agricultural UAV sprayer** — optimized spray uniformity and low-drift deposition.  
Tools: SolidWorks (Flow Simulation trial via AMP CAD), KeyShot, KiCAD, Python (NumPy/Matplotlib), Excel.

## Quick links
- `docs/01_Project_Overview.md` — Project brief & goals
- `design/` — CAD & renders
- `electronics/` — KiCAD schematics & BOM
- `simulation/` — SolidWorks CFD screenshots & Python simulation results
- `economics/` — ROI model
- `presentation/` — slides & demo video

## Acknowledgements
SolidWorks Flow Simulation trial courtesy of **AMP CAD (Dassault Systèmes reseller, South Africa)**.

## How to run the Python sim
```bash
cd simulation/python_model
python spray_sim.py



---

# 4) `docs/01_Project_Overview.md` — paste now (Module A base)
```markdown
# Project Overview

## Title
AgriDrone Optimization — scaled demonstration sprayer

## Team
- Mechanical / CAD: [Your Name] (remote)
- Electronics & Simulation: assisted (AI templates + guidance)
- Notes: Project demonstrates remote-ready digital twin + simulations.

## Objective
Deliver a manufacturable small-scale spray drone demonstrator that:
- Achieves 30–100 L/ha adjustable flow,
- Produces droplets 0.5–2.5 mm,
- Achieves ≥85% uniformity in the target swath,
- Keeps drift ≤5 m at wind ≤5 m/s (via nozzle/parameter tuning).

## Deliverables (Module A)
- SolidWorks assembly (.STEP) + 2 production drawings (.PDF)
- BOM CSV with part numbers and prices
- KiCAD schematic (pump driver + sensor + RC kill-switch)
- 1-page technical description (purpose, constraints, major choices)
