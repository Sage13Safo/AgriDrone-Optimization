"""
AgriDrone Optimization — ROI and Cost Efficiency Calculator
Author: Sage (Solo Developer)
Description:
Estimates return on investment and payback time
for the agricultural drone sprayer project.
"""

import matplotlib.pyplot as plt

# ---------------------------
# 1️⃣ Input Parameters (Editable)
# ---------------------------

# Equipment Costs (USD)
drone_cost = 1200
pump_system_cost = 150
battery_cost = 250
nozzle_system_cost = 80
controller_cost = 100
maintenance_per_year = 100

# Operational Parameters
chemical_saving_percent = 25      # 25% less pesticide due to precision spraying
farm_area_per_hour = 4.5          # hectares per hour
chemical_cost_per_hectare = 18    # cost without drone
operating_hours_per_year = 150

# Drone Life Expectancy (years)
lifespan = 3

# ---------------------------
# 2️⃣ Calculations
# ---------------------------

# Total Investment
total_cost = drone_cost + pump_system_cost + battery_cost + nozzle_system_cost + controller_cost

# Annual Chemical Cost (traditional vs. drone)
traditional_cost = chemical_cost_per_hectare * farm_area_per_hour * operating_hours_per_year
drone_cost_chem = traditional_cost * (1 - chemical_saving_percent / 100)

# Annual Savings
annual_savings = traditional_cost - drone_cost_chem

# Net Annual Benefit
net_annual_benefit = annual_savings - maintenance_per_year

# ROI and Payback
roi_percent = (net_annual_benefit * lifespan / total_cost) * 100
payback_period = total_cost / net_annual_benefit

# ---------------------------
# 3️⃣ Display Results
# ---------------------------
print("====== AGRIDRONE ROI SUMMARY ======")
print(f"Total Investment: ${total_cost:.2f}")
print(f"Annual Savings: ${annual_savings:.2f}")
print(f"Net Annual Benefit (after maintenance): ${net_annual_benefit:.2f}")
print(f"ROI over {lifespan} years: {roi_percent:.1f}%")
print(f"Estimated Payback Period: {payback_period:.1f} years")

# ---------------------------
# 4️⃣ Visualization
# ---------------------------
years = list(range(1, lifespan + 1))
cumulative_profit = [net_annual_benefit * i - total_cost for i in years]

plt.figure(figsize=(7, 5))
plt.plot(years, cumulative_profit, 'o-', label="Cumulative Profit")
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Years")
plt.ylabel("Cumulative Profit (USD)")
plt.title("AgriDrone ROI Projection")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("roi_projection.png", dpi=300)
plt.show()

print("\n✅ Chart saved to: roi_projection.png")
