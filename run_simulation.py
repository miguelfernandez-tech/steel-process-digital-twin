import random
import simpy
import pandas as pd
import config
from src.plant import SteelPlantModel, casting_process, rolling_process, periodic_monitor
from src.analysis import calculate_kpis
from src.visualizer import plot_scenarios_comparison

def execute_simulation(prescriptive_mode=False):
    random.seed(config.RANDOM_SEED)
    env = simpy.Environment()
    plant = SteelPlantModel(env, prescriptive_mode=prescriptive_mode)

    env.process(casting_process(env, plant))
    env.process(rolling_process(env, plant))
    env.process(periodic_monitor(env, plant, interval=2.0))

    env.run(until=config.SIM_TIME)

    df = pd.DataFrame(plant.log_data).drop_duplicates(subset=['Time']).sort_values('Time')
    return plant, df

if __name__ == '__main__':
    print("Initializing Process Digital Twin (ArcelorMittal Gijon)...")

    # Execute simulations for both scenarios
    plant_base, df_base = execute_simulation(prescriptive_mode=False)
    plant_opt, df_opt = execute_simulation(prescriptive_mode=True)

    # Export logs to the results/logs/ folder
    df_base.to_csv("results/logs/scenario_base.csv", index=False)
    df_opt.to_csv("results/logs/scenario_prescriptive.csv", index=False)

    # Calculate KPIs
    kpi_base = calculate_kpis(plant_base, df_base)
    kpi_opt = calculate_kpis(plant_opt, df_opt)

    # Print comparative summary of operations
    print("\n" + "="*65)
    print("   COMPARATIVE SUMMARY OF OPERATIONS (8H SHIFT / 480 MIN)")
    print("="*65)
    print(f"{'Operational Metric':<32} | {'Baseline':<12} | {'Optimized':<12}")
    print("-"*65)
    for k in kpi_base.keys():
        print(f"{k:<32} | {str(kpi_base[k]):<12} | {str(kpi_opt[k]):<12}")
    print("="*65)

    # Generate and save the figure
    plot_scenarios_comparison(df_base, df_opt)
