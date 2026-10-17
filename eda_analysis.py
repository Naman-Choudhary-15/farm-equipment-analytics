import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- Farm Equipment Utilization: Exploratory Data Analysis ---")

# 1. Load the data
if not os.path.exists('telemetry_data.csv'):
    print("Error: telemetry_data.csv not found. Please run generate_mock_data.py first.")
    exit()

df = pd.read_csv('telemetry_data.csv')
print("\n[1] Initial Data Loaded:")
print(df.head())

# 2. Data Cleaning
print("\n[2] Data Cleaning:")
missing_values = df.isnull().sum()
print("Missing values before cleaning:\n", missing_values[missing_values > 0])

# Fill missing fuel consumption with the median based on Machine Type
df['Fuel_Consumption_Liters'] = df.groupby('Machine_Type')['Fuel_Consumption_Liters'].transform(lambda x: x.fillna(x.median()))
print("\nMissing values after cleaning: ", df['Fuel_Consumption_Liters'].isnull().sum())

# 3. Exploratory Data Analysis (EDA)
print("\n[3] Generating EDA Visualizations...")

# Set visualization style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))

# Plot A: Fuel Consumption vs Idle Time
plt.subplot(2, 2, 1)
sns.scatterplot(data=df, x='Idle_Hours', y='Fuel_Consumption_Liters', hue='Machine_Type', alpha=0.7)
plt.title('Fuel Consumption vs. Idle Hours')
plt.xlabel('Idle Hours')
plt.ylabel('Fuel Consumption (Liters)')

# Plot B: Actual vs Planned Hours by Machine Type
plt.subplot(2, 2, 2)
df_melted = pd.melt(df, id_vars=['Machine_Type'], value_vars=['Operating_Hours_Planned', 'Operating_Hours_Actual'], 
                    var_name='Hour_Type', value_name='Hours')
sns.boxplot(data=df_melted, x='Machine_Type', y='Hours', hue='Hour_Type')
plt.title('Planned vs Actual Operating Hours')

# Plot C: Engine Load Distribution (Machine Health)
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='Engine_Load_Percent', hue='Maintenance_Required', multiple="stack", bins=20)
plt.title('Engine Load & Maintenance Alerts')

# Plot D: Total Idle Time by Season
plt.subplot(2, 2, 4)
sns.barplot(data=df, x='Season', y='Idle_Hours', estimator=sum, errorbar=None, order=['Spring', 'Summer', 'Autumn', 'Winter'])
plt.title('Total Idle Time Across Seasons')

plt.tight_layout()
plt.savefig('eda_results.png')
print("Visualizations saved as 'eda_results.png'. Open the image to view the graphs!")
print("EDA complete.")
