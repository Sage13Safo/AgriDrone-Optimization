# 💰 Module C — Economic Efficiency  
*(AgriDrone Optimization — BRICS Russia Future Skills Challenge 2025)*  

---

## 1. Objective  
Evaluate the **economic feasibility** of the agricultural UAV sprayer system, estimate operational costs, and calculate **Return on Investment (ROI)** under realistic farm operation scenarios.

---

## 2. Baseline Assumptions  

| Parameter | Symbol | Value | Unit | Notes |
|------------|---------|--------|------|-------|
| Drone purchase price | C_d | 4,000 | USD | mid-range 6-rotor sprayer drone |
| Nozzle assembly (4x) | C_n | 160 | USD | 40 USD per unit |
| Pump + piping system | C_p | 120 | USD | including valves, filter |
| Battery set | C_b | 200 | USD | 2 Li-Po packs |
| Payload capacity | W | 30 | L | usable payload for 1 flight |
| Flow rate | Q | 2.7 | L/min | validated in Module B |
| Spray area per flight | A_f | 1.0 | ha | 10–15 min flight duration |
| Chemical cost | C_c | 6 | USD/L | average pesticide |
| Labor & maintenance | C_m | 2 | USD/hr | self-operated |

---

## 3. Operating Cost per Hectare  

**Formula:**

\[
C_{op} = \frac{C_c \times W}{A_f} + \frac{C_m \times t}{A_f}
\]

Where:  
- \( C_c \) = chemical cost per liter  
- \( W \) = payload (L)  
- \( t \) = flight time (hr)  

**Example:**  
For \( W = 30 \) L, \( C_c = 6 \), \( C_m = 2 \), \( t = 0.25 \) hr:

\[
C_{op} = \frac{6 \times 30}{1} + \frac{2 \times 0.25}{1} = 180.5 \, \text{USD/ha}
\]

---

## 4. Revenue Estimation  

Assume:
- Typical service charge for drone spraying = **250 USD/ha**  
- Net operational profit = \( R = 250 - C_{op} = 69.5 \, \text{USD/ha} \)

| Area Covered | Profit (USD) | Time (hrs) | Remarks |
|---------------|--------------|-------------|----------|
| 1 ha | 69.5 | 0.25 | single flight |
| 5 ha | 347.5 | 1.25 | one session |
| 20 ha | 1,390 | 5.0 | full-day spraying |

---

## 5. ROI Model  

**Formula:**
\[
ROI = \frac{(R \times A_{year}) - C_{total}}{C_{total}} \times 100
\]

Where:  
- \( R \) = profit per hectare  
- \( A_{year} \) = total hectares sprayed annually  
- \( C_{total} \) = total capital cost  

Example for 500 ha annual operation:  

\[
C_{total} = 4,000 + 160 + 120 + 200 = 4,480
\]
\[
ROI = \frac{(69.5 \times 500) - 4480}{4480} \times 100 = 675\%
\]

✅ **Result:** ROI ≈ **675% in Year 1** → Break-even achieved within **<2 months** of operation.

---

## 6. Sustainability Benefits  

| Aspect | Advantage |
|--------|------------|
| **Chemical Efficiency** | Reduces over-spraying by 20–30% |
| **Labor Reduction** | Single-operator control |
| **Battery Operation** | Zero carbon emission during use |
| **Precision Delivery** | Low drift ensures minimal waste |

---

## 7. Deliverables  

| Item | Description | File Path |
|------|--------------|-----------|
| Cost Table | CSV breakdown | `/module_C_economic_efficiency/economics/Cost_Table.csv` |
| ROI Model | Excel workbook | `/module_C_economic_efficiency/economics/ROI_Model.xlsx` |
| Module Report | PDF summary | `/module_C_economic_efficiency/deliverables/ModuleC_Deliverable.pdf` |

---

## 8. Next Steps  
- ✅ Verify cost data with local suppliers (Ghana/SA)  
- 🧮 Adjust ROI model for 50 ha, 100 ha, 500 ha scenarios  
- 🧾 Export report + include graphs in Module D slides  

---

**Author:** Sage13 Safo  
**Tools:** Excel • Python (ROI computation optional)  
**Acknowledgment:** AMP CAD South Africa for hardware CFD license reference  

---

> _“A good design pays for itself — precision is profit.”_

