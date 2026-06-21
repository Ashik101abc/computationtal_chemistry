import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Load Data (Simulating HER catalyst parameters)
print("Loading HER Catalyst Data...")
data = {
    'Binding_Energy_H': [-0.25, -0.10, 0.05, 0.20, -0.40, 0.15, -0.05, 0.30],
    'Electronegativity': [2.1, 1.9, 2.5, 2.0, 1.8, 2.2, 2.0, 1.7],
    'Overpotential_mV': [50, 20, 120, 150, 200, 130, 40, 180]
}
df = pd.DataFrame(data)

# 2. Define Features (X) and Target (y)
X = df[['Binding_Energy_H', 'Electronegativity']] # Inputs
y = df['Overpotential_mV'] # What we want to predict

# 3. Train-Test Split (25% data reserved for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Initialize and Train the Model
print("Training Random Forest Model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Predict and Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("\n--- Machine Learning Baseline Results ---")
print(f"Mean Absolute Error (MAE): {mae:.2f} mV")
print(f"Test Sample 1 -> Predicted: {predictions[0]:.2f} mV | Actual: {y_test.iloc[0]} mV")
print(f"Test Sample 2 -> Predicted: {predictions[1]:.2f} mV | Actual: {y_test.iloc[1]} mV")

