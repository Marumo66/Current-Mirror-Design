#!/usr/bin/env python3
"""Plot the selected LTspice cursor readings recorded in the CSV file."""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "Phase_1_Basic_Current_Mirror/results/data/dc_sweep_cursor_readings.csv"
OUT_PATH = ROOT / "Phase_1_Basic_Current_Mirror/results/figures/current_mirror_cursor_comparison.png"

series: dict[float, list[tuple[float, float]]] = {}
with CSV_PATH.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        lam = float(row["lambda_v_inv"])
        series.setdefault(lam, []).append((float(row["vout_v"]), float(row["iout_uA"])))

fig, ax = plt.subplots(figsize=(8.5, 5.2), constrained_layout=True)
for lam in sorted(series, reverse=True):
    points = sorted(series[lam])
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    ax.plot(xs, ys, marker="o", linewidth=1.5, label=f"λ = {lam:g} V⁻¹")

ax.axhline(100.0, linestyle="--", linewidth=1.0, label="IREF = 100 µA")
ax.set_xlabel("Output voltage VOUT (V)")
ax.set_ylabel("Output current IOUT (µA)")
ax.set_title("Basic NMOS Current Mirror — selected LTspice cursor readings")
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_xlim(0, 1.85)
ax.set_ylim(45, 106)
ax.text(
    0.01,
    -0.23,
    "Markers show selected cursor readings, not the complete sweep dataset.",
    transform=ax.transAxes,
    fontsize=8,
)
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PATH, dpi=180)
print(f"Saved {OUT_PATH}")
