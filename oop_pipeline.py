import pandas as pd
import numpy as np

class CatalystPipeline:
    """
    Object-Oriented Pipeline for filtering Catalyst Data.
    Focused on exploring research interests in HER and OER processes.
    """
    
    def __init__(self, dataset_name):
        # __init__ is the constructor. It runs immediately when the object is created.
        self.name = dataset_name
        self.data = None # Placeholder for our dataframe
        print("Pipeline Initialized for: " + self.name)
        
    def generate_dummy_data(self):
        # Creating mock data to simulate your CSV files
        print("Generating catalyst test data...")
        self.data = pd.DataFrame({
            'Catalyst': ['Pt', 'Ni-Fe', 'MoS2', 'Graphene', 'CoP'],
            'Overpotential_mV': [30, 250, 150, np.nan, 80] # Note the NaN value
        })
        
    def clean_data(self):
        # Using 'self' to access the data created in the previous method
        print("Cleaning data (Removing NaNs)...")
        initial_count = len(self.data)
        self.data = self.data.dropna()
        final_count = len(self.data)
        print("Removed " + str(initial_count - final_count) + " invalid rows.")
        
    def filter_best_catalysts(self, threshold):
        print("Filtering catalysts with overpotential < " + str(threshold) + " mV...")
        best = self.data[self.data['Overpotential_mV'] < threshold]
        print("\n--- Top Performers ---")
        print(best)


# === Execution Block ===
# 1. Create an instance (object) of the class
her_pipeline = CatalystPipeline("HER_Simulation_Batch_01")

# 2. Call the methods sequentially
her_pipeline.generate_dummy_data()
her_pipeline.clean_data()
her_pipeline.filter_best_catalysts(threshold=100)

