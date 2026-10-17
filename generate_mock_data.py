import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(num_records=500):
    np.random.seed(42)
    
    # Base data
    machine_types = ['Tractor', 'Harvester', 'Irrigation Pump']
    seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
    
    data = []
    start_date = datetime(2026, 1, 1)
    
    for i in range(num_records):
        machine_type = np.random.choice(machine_types)
        season = np.random.choice(seasons)
        
        # Simulate some logical data relationships
        planned_hours = np.random.uniform(6, 12)
        
        # Actual hours can be slightly more or less than planned
        actual_hours = planned_hours * np.random.uniform(0.7, 1.1)
        
        # Idle hours
        idle_hours = actual_hours * np.random.uniform(0.1, 0.4)
        
        # Fuel consumption depends on actual operating hours + idle hours
        fuel_consumption = (actual_hours * 15) + (idle_hours * 5) + np.random.normal(0, 5)
        fuel_consumption = max(0, fuel_consumption)
        
        # Engine load percent
        engine_load = np.random.normal(65, 15)
        engine_load = min(100, max(0, engine_load))
        
        # Maintenance flag logic (high idle or high load increases breakdown chance)
        maintenance_flag = 'No'
        if engine_load > 85 or idle_hours > 3:
            if np.random.random() > 0.5:
                maintenance_flag = 'Yes'
                
        data.append({
            'Date': start_date + timedelta(days=np.random.randint(0, 180)),
            'Machine_ID': f"{machine_type[:3].upper()}-{np.random.randint(100, 999)}",
            'Machine_Type': machine_type,
            'Season': season,
            'Operating_Hours_Planned': round(planned_hours, 2),
            'Operating_Hours_Actual': round(actual_hours, 2),
            'Idle_Hours': round(idle_hours, 2),
            'Fuel_Consumption_Liters': round(fuel_consumption, 2),
            'Engine_Load_Percent': round(engine_load, 2),
            'Maintenance_Required': maintenance_flag
        })
        
    df = pd.DataFrame(data)
    
    # Introduce some synthetic "missing data" to show data cleaning capability
    idx_to_null = df.sample(frac=0.05).index
    df.loc[idx_to_null, 'Fuel_Consumption_Liters'] = np.nan
    
    df.to_csv('telemetry_data.csv', index=False)
    print("Successfully generated 'telemetry_data.csv' with", num_records, "records.")

if __name__ == "__main__":
    generate_data()
