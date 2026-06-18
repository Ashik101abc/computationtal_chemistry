import pandas as pd 
import matplotlib.pyplot as plt
df= pd.read_csv('her_data.csv').dropna()
print("generating bar chart..")
plt.bar(df['catalyst'],df['overpotential_mV'],color=['gray','orange','red'])
plt.xlabel('electrocartalyst')
plt.ylabel('Overpotential(mV)')
plt.title('HER perfprmance comparison')
plt.savefig('catalyst_plot.png')
print("saved the graph")

