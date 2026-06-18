import numpy as np

list_energy = [10, 20, 30]          # Eita normal Python er box
arr_energy = np.array([10, 20, 30]) # Eita NumPy er box

print("NumPy Addition:")
print(arr_energy + 5)  # Eita perfectly kaj korbe

print("Python Addition:")
print(list_energy + 5) # Eita crash korbe!

