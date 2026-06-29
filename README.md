# Water Splitting Electrocatalysts: ML Baseline for HER & OER

## Abstract
This project establishes a Machine Learning baseline to predict the Overpotential (mV) of electrocatalysts for Green Hydrogen Production. Instead of relying solely on physical lab experiments, this computational pipeline uses catalyst features (Binding Energy and Electronegativity) to predict efficiency, accelerating the discovery of optimal materials.

## Methodology
1. **Data Pipeline:** Developed an Object-Oriented Programming (OOP) architecture (`oop_pipeline.py`) to automatically ingest raw catalyst data and clean missing/NaN values.
2. **Kinetics Simulation:** Implemented SciPy-based differential equations (`kinetics.py`) to model reaction rates over time.
3. **Machine Learning:** Trained and evaluated two algorithms (Random Forest and XGBoost) on a 75/25 train-test split to predict catalyst overpotential.

## Results & Visual Evidence
* **Random Forest Performance:** MAE = ও] mV | RMSE = [] mV
* **XGBoost Performance:** MAE = [] mV | RMSE = [] mV

### Visualizations
*(Note: Images are generated via `visualize_features.py`)*
1. **Correlation Heatmap:** Demonstrates the mathematical relationship between Binding Energy, Electronegativity, and Overpotential.
2. **Actual vs. Predicted (XGBoost):** Scatter plot with a perfect-prediction baseline to identify outliers.
3. **Feature Importance:** Ranks the impact of input features on the final catalyst efficiency.

## Discussion (Outlier Analysis)
While the XGBoost model establishes a strong baseline, the Root Mean Squared Error (RMSE) indicates specific outliers. These outliers suggest that purely relying on Binding Energy and Electronegativity is insufficient for certain complex catalysts (e.g., Ni-Fe alloys). Future phases will integrate solvent effects and surface resistance to refine the model.
