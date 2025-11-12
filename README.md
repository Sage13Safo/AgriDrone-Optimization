# 🌾 AgriDrone Optimization  
*(BRICS RUSSIA FUTURE SKILLS & TECH CHALLENGE — UAS_Drones Hackathon 2025)*

**Scaled demonstration agricultural UAV sprayer** — optimized spray uniformity and low-drift deposition.  
Tools: **SolidWorks (Flow Simulation trial via AMP CAD)** • KeyShot • KiCAD • Python (NumPy + Matplotlib) • Excel.

---

## 🚀 Quick Links
| Module | Purpose | Folder |
|---------|----------|---------|
| **Module A — Design & Prototyping** | CAD, BOM, technical description | [`module_A_design_prototyping/`](module_A_design_prototyping/) |
| **Module B — Testing & Simulation** | SolidWorks CFD + Python validation | [`module_B_testing_simulation/`](module_B_testing_simulation/) |
| **Module C — Economic Efficiency** | ROI model & cost analysis | [`module_C_economic_efficiency/`](module_C_economic_efficiency/) |
| **Module D — Presentation & Defense** | Slides + scripts + demo video | [`module_D_presentation_defense/`](module_D_presentation_defense/) |
| **Supporting Files** | References + templates | [`supporting_files/`](supporting_files/) |

---

## 🧩 Repository Structure

```text
AgriDrone-Optimization/
├── README.md
├── LICENSE
│
├── module_A_design_prototyping/
│   ├── docs/
│   │   ├── A1_Project_Brief.md
│   │   ├── A2_Technical_Description.md
│   │   ├── A3_BOM_and_Roles.md
│   │   └── ModuleA_Deliverable.pdf
│   ├── design/
│   │   ├── CAD_Files/
│   │   ├── Drawings/
│   │   ├── Renders/
│   │   └── mass_properties.txt
│   ├── electronics/
│   │   ├── schematics/
│   │   ├── BOM.csv
│   │   └── pump_driver_netlist.txt
│   └── deliverables/
│       └── ModuleA_Deliverable.pdf
│
├── module_B_testing_simulation/
│   ├── docs/
│   │   ├── B1_Test_Plan.md
│   │   ├── B2_Simulation_Procedure.md
│   │   └── B3_Test_Report.md
│   ├── simulation/
│   │   ├── python_model/
│   │   │   ├── spray_sim.py
│   │   │   └── results/
│   │   └── solidworks_flow/
│   │       └── README.md
│   └── deliverables/
│       └── ModuleB_Testing_Report.pdf
│
├── module_C_economic_efficiency/
│   ├── docs/
│   │   ├── C1_Cost_Assumptions.md
│   │   └── C2_ROI_Calculations.md
│   ├── economics/
│   │   ├── ROI_Model.xlsx
│   │   └── Cost_Table.csv
│   └── deliverables/
│       └── ModuleC_Deliverable.pdf
│
├── module_D_presentation_defense/
│   ├── docs/
│   │   ├── D1_Slide_Content.md
│   │   ├── D2_Pitch_Scripts.md
│   │   └── D3_QA_Preparation.md
│   ├── presentation/
│   │   ├── slides.pptx
│   │   ├── slides.pdf
│   │   ├── demo_video.mp4
│   │   └── figures/
│   │       ├── flow_vs_python.png
│   │       ├── roi_chart.png
│   │       ├── drone_render.png
│   │       └── uniformity_heatmap.png
│   └── deliverables/
│       └── ModuleD_Presentation_Package.zip
│
└── supporting_files/
    ├── references/
    └── templates/

