# Technical Description — AgriDrone Optimization (Module A)

## Purpose
Scaled demonstrator for agricultural spraying: dual-nozzle quadcopter module designed to deliver configurable application rates (30–100 L/ha) with emphasis on spray uniformity and reduced drift.

## Major components
- Frame: 250 mm diagonal carbon-fiber arms (3D printed motor mounts)
- Tank: 1.0 L HDPE with mounting bracket
- Pump: Diaphragm/peristaltic pump (0.3–0.5 MPa)
- Nozzles: 2 × flat-fan / hollow-cone agricultural nozzles
- Flight controller: Pixhawk (MAVLink)
- Companion computer: Raspberry Pi 4 (for CV & logging)
- Sensors: flow sensor, pressure sensor, ultrasonic altimeter

## Key engineering decisions
1. **Small tank (1 L)** to keep mass low and comply with demo flight limits—enough to show behaviour.
2. **Dual nozzles** create a controllable overlap swath; nozzle spacing optimized using deposition simulations.
3. **Pump with pressure control** allows changing droplet sizes by pressure and flow.
4. **Mounting**: Nozzle mounts are rigid with rubbers for vibration isolation; electronics are on sheet-metal tray for EMI shielding.

## Control logic (brief)
- On takeoff, companion computer sets pump to idle.
- While spraying mission active: set pump PWM to target flow; log flow & pressure; adjust PWM in closed-loop to maintain target L/ha.
- Manual kill-switch (RC) rigged to cut pump power and trigger immediate return-to-home.

## Files in repository
- `design/CAD_Files/assembly.step` — full assembly
- `design/Drawings/assembly_drawings.pdf` — production drawings
- `electronics/BOM.csv` — parts list
