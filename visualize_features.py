import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

print("Initializing Visualization Engine...")

# 1. Load the exact same data from your ML baseline
data = {
    'Binding_Energy_H': [-0.25, -0.10, 0.05, 0.20, -0.40, 0.15, -0.05, 0.30],
    'Electronegativity': [2.1, 1.9, 2.5, 2.0, 1.8, 2.2, 2.0, 1.7],
    'Overpotential_mV': [50, 20, 120, 150, 200, 130, 40, 180]
}
df = pd.DataFrame(data)

# 2. Train XGBoost Model to generate prediction data
X = df[['Binding_Energy_H', 'Electronegativity']]
y = df['Overpotential_mV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Set the visual style for publication-ready aesthetics
sns.set_theme(style="whitegrid")

# --- PLOT 1: Correlation Heatmap ---
plt.figure(figsize=(6, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.close()
print("-> Saved: correlation_heatmap.png")

# --- PLOT 2: Actual vs Predicted Scatter Plot ---
plt.figure(figsize=(6, 5))
sns.scatterplot(x=y_test, y=y_pred, s=100, color="blue", edgecolor="k", alpha=0.7)

# Draw the red diagonal line (The 'Perfect Prediction' line)
min_val = min(min(y_test), min(y_pred)) - 10
max_val = max(max(y_test), max(y_pred)) + 10
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label="Perfect Prediction")

plt.xlabel("Actual Overpotential (mV)")
plt.ylabel("Predicted Overpotential (mV)")
plt.title("XGBoost: Actual vs Predicted Performance")
plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=300)
plt.close()
print("-> Saved: actual_vs_predicted.png")

# --- PLOT 3: Feature Importance Bar Chart ---
plt.figure(figsize=(6, 4))
importance = model.feature_importances_
sns.barplot(x=importance, y=X.columns, palette="viridis")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.title("XGBoost Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=300)
plt.close()
print("-> Saved: feature_importance.png")

print("\nVisualization complete. All artifacts generated successfully.")
