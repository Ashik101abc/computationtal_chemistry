import pandas as pd
df=pd.read_csv('her_data.csv').dropna()
mean_op=df['overpotential_mV'].mean()
print("average overpotential:" +str(round(mean_op,2))+ " mV\n")
print("---HIGH EFFICIENCY CATALYSTS(<100mV)---")
best_catalysts=df[df['overpotential_mV'] < 100]
print(best_catalysts[['catalyst','overpotential_mV']])
