# Simulation Engine

Mathematical Authority: See ../../MATH.md.

The simulation engine estimates coherence gain, risk, migration cost, curvature change, noise change, and cost change before any production plan is proposed.

Simulations must support broad-spectrum domains from ../standards/INDUSTRY_STANDARDS_MATRIX.md and emerging facility scenarios from ../facility/EMERGING_FACILITY_NEEDS.md before actuation is considered.

Replayable scenario fixtures live in ../../data/simulation_scenarios.json. The deterministic report generator at ../../scripts/generate_simulation_report.py computes before/after `Q`, `DeltaDCCO`, risk, migration cost, and `PlanScore`, then writes ../../reports/simulation_latest.md and ../../reports/simulation_latest.json.
