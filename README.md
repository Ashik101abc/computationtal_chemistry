# Computational Chemistry Data Pipeline

**Author:** Md Ashikur Rahman Azad  
**Research Interest:** Water Splitting Electrocatalysts (HER and OER for Green Hydrogen Production)

## Project Overview
This repository contains Python-based data processing scripts for the high-throughput screening and analysis of electrocatalyst performance. The objective is to transition from raw simulation data to clean, publishable insights.

## Core Files & Tools Used
* **`clean_data.py` (Pandas):** Ingests raw CSV outputs, identifies missing structures (NaN), and sanitizes the dataset.
* **`analyze_data.py` (Pandas/NumPy):** Executes mathematical filtering to isolate highly efficient catalysts with an overpotential of < 100 mV.
* **`plot_data.py` (Matplotlib):** Generates automated, publication-ready bar charts (`catalyst_plot.png`) for visual performance comparison.
