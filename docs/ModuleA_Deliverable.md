# Module A — Design & Prototyping Deliverable
**Project:** AgriDrone Optimization  
**Team:** [Your Name] — Mechanical / CAD (remote)  
**Competition Skill:** Drone Assembling & Electronic Engineering

---

## 1. One-line summary
A compact dual-nozzle quadcopter sprayer demonstrator optimized for low-drift, high-uniformity application at demo scale (1 L tank) with validated simulation and a clear BOM and control plan.

---

## 2. Objectives & Requirements (from task)
- Application rate: **30–100 L/ha** (adjustable)  
- Droplet size: **0.5–2.5 mm** (configurable via pressure/nozzle)  
- Target uniformity: **≥ 85%** (coefficient-of-variation based metric)  
- Maximum allowed drift at wind 5 m/s: **≤ 5 m**  
- Spray range: **1.5–4 m** (altitude window)  
- Max frame diagonal: **≤ 10 in (~25 cm)** (demo-sized)

---

## 3. Concept description (final selection)
**Concept:** Mini dual-nozzle quadcopter sprayer.

**Why:** Simple, demonstrable, and easy to simulate: two nozzles produce a narrow overlapping swath enabling adjustable swath width via nozzle spacing and flight speed. Keeps payload small and system safely demonstrable during competition.

---

## 4. System architecture (high level)
- **Airframe:** 250 mm diagonal quadcopter frame (carbon-fiber arms / 3D-printed mounts).  
- **Payload:** 1.0 L HDPE tank with gravity feed to pump.  
- **Pump:** Mini diaphragm/peristaltic, pressure range ~0.2–0.5 MPa.  
- **Nozzles:** 2 × agricultural flat-fan/hollow-cone (selectable).  
- **Control:** Pixhawk (flight control) + Raspberry Pi 4 (companion computer) for mission logic and logging.  
- **Sensors:** Inline flow sensor, pressure sensor, ultrasonic altimeter / lidar for height keeping.  
- **Safety:** RC Kill-switch wired to pump power cutoff; software watchdog on companion computer.

*(Block diagram image placeholder: `design/Renders/block_diagram.png`)*

---

## 5. Key engineering decisions & justification
1. **1 L tank** — minimizes payload and enables multiple short demonstration flights; enough volume to show parametric effect on coverage.  
2. **Dual nozzles** — simpler than a long boom, easier to mount on small airframe and still lets us demonstrate overlap and uniformity optimization.  
3. **Peristaltic pump** — self-priming and precise flow via PWM (closed-loop with flow sensor) and safe for agricultural chemicals.  
4. **Flow control by PWM & feedback** — maintain target L/ha independent of battery voltage or nozzle wear.  
5. **Small frame ≤10″ diag** — satisfies competition constraint for multi-rotor testability.

---

## 6. Deliverables (files included)
- `design/CAD_Files/assembly.step` — SolidWorks assembly (skeleton).  
- `design/Drawings/assembly_drawings.pdf` — exploded & production drawings.  
- `design/Renders/` — KeyShot renders and demo frames.  
- `electronics/BOM.csv` — parts list with estimated pricing.  
- `electronics/schematics/pump_driver_netlist.txt` — pump-driver wiring plan.  
- `simulation/solidworks_flow/` — Flow Simulation screenshots (to be added).  
- `simulation/python_model/spray_sim.py` — analytical particle model + results (see simulation/results/).  
- `docs/ModuleA_Deliverable.md` — (this document).  

---

## 7. BOM snapshot (key items)
| Part # | Part name | Qty | Est. unit price (USD) |
|--------|-----------|-----:|-----------------------:|
| 001 | 1 L HDPE tank | 1 | 5.00 |
| 002 | Mini diaphragm/peristaltic pump (0.2–0.5 MPa) | 1 | 18.00 |
| 003 | Agricultural nozzle (flat/hollow cone) | 2 | 6.00 ea |
| 004 | Pixhawk-compatible flight controller | 1 | 100.00 |
| 005 | Raspberry Pi 4 (4GB) | 1 | 50.00 |
| 006 | Flow sensor (0.5–5 L/min) | 1 | 15.00 |

*(Full BOM in `electronics/BOM.csv`)*

---

## 8. Manufacturing notes & critical dimensions
- Nozzle spacing: **X = 0.12 m (example)** (optimize with simulation).  
- Tank mount to CG: place within 10 mm of center for balance; show mass properties file `design/mass_properties.txt`.  
- Fastener callouts included in `design/Drawings/assembly_drawings.pdf`.

---

## 9. Control pseudocode (pump control)
```text
# Pump control loop (high-level)
set_target_flow(L_per_ha, flight_speed, swath_width):
    Q_target_Ls = L_per_ha * flight_speed * swath_width / 10000  # L/s

main_loop():
    while mission_active:
        flow = read_flow_sensor()  # L/s
        error = Q_target_Ls - flow
        pwm = pid_controller.update(error)
        set_pwm_to_pump(pwm)
        log(timestamp, flow, pwm, pressure)
        if kill_switch_pressed(): shutdown_pump_and_return()
