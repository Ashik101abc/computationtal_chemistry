import numpy as np

# HER Overpotential data in Volts
raw_volts = np.array([0.25, 0.32, 0.18, 0.41])

# Convert to milliVolts
milli_volts = raw_volts * 1000

print("Raw Data (V):")
print(raw_volts)
print("Converted Data (mV):")
print(milli_volts)
