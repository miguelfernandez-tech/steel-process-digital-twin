import pandas as pd

def calculate_kpis(plant, df):
    """Calcula las metricas clave de rendimiento del proceso siderurgico."""
    avg_wip = df['WIP'].mean()
    max_wip = df['WIP'].max()
    throughput = plant.produced_billets
    cold_diverted = plant.cold_diverted_billets
    
    # Ammount of time the buffer is saturated (WIP >= Buffer_Cap)
    time_saturated = len(df[df['WIP'] >= df['Buffer_Cap']]) / len(df) * 100
    
    return {
        'Throughput (billets)': throughput,
        'Cold Diverted (losses)': cold_diverted,
        'Average WIP': round(avg_wip, 2),
        'Max WIP': max_wip,
        'Buffer Saturation (%)': round(time_saturated, 2)
    }
