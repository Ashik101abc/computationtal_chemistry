import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Load Data
print("Loading HER Catalyst Data...")
data = {
    'Binding_Energy_H': [-0.25, -0.10, 0.05, 0.20, -0.40, 0.15, -0.05, 0.30],
    'Electronegativity': [2.1, 1.9, 2.5, 2.0, 1.8, 2.2, 2.0, 1.7],
    'Overpotential_mV': [50, 20, 120, 150, 200, 130, 40, 180]
}
df = pd.DataFrame(data)

# 2. Define Features and Target
X = df[['Binding_Energy_H', 'Electronegativity']]
y = df['Overpotential_mV']

# 3. Train-Test Split (25% hidden data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Train Model A: Random Forest
print("\nTraining Random Forest...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# 5. Train Model B: XGBoost
print("Training XGBoost...")
xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)
xgb_preds = xgb_model.predict(X_test)

# 6. Deep Error Analysis
rf_mae = mean_absolute_error(y_test, rf_preds)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))

xgb_mae = mean_absolute_error(y_test, xgb_preds)
xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_preds))

print("\n--- Algorithm Benchmark Results ---")
print(f"Random Forest -> MAE: {rf_mae:.2f} mV | RMSE: {rf_rmse:.2f} mV")
print(f"XGBoost       -> MAE: {xgb_mae:.2f} mV | RMSE: {xgb_rmse:.2f} mV")
