"""
Visualizer module for the Process Digital Twin (ArcelorMittal Gijon).
Generates comparative figures for the operational report.
"""

import matplotlib.pyplot as plt
import config

def plot_scenarios_comparison(df_base, df_opt, save_path="results/figures/results_comparison.png"):
    """
    Plots and exports the WIP dynamic comparison between baseline and prescriptive twin.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True, sharey=True)

    # 1. Baseline Scenario (Reactive Policy)
    ax1.plot(
        df_base['Time'], 
        df_base['WIP'], 
        color='#d9381e', 
        linewidth=2, 
        label='Actual WIP (Intermediate Buffer)'
    )
    ax1.axhline(
        y=config.BUFFER_CAPACITY, 
        color='black', 
        linestyle='--', 
        label=f'Max Physical Capacity ({config.BUFFER_CAPACITY} billets)'
    )
    ax1.set_title(
        'Baseline Scenario (Reactive Control) - Buffer Saturation & Cold Yard Stacking', 
        fontsize=11, 
        fontweight='bold'
    )
    ax1.set_ylabel('WIP Level (Billets)', fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper left', frameon=True)

    # 2. Optimized Scenario (Prescriptive Digital Twin)
    ax2.plot(
        df_opt['Time'], 
        df_opt['WIP'], 
        color='#1a73e8', 
        linewidth=2, 
        label='WIP Level (Prescriptive Pacing)'
    )
    ax2.axhline(
        y=config.BUFFER_CAPACITY, 
        color='black', 
        linestyle='--', 
        label=f'Max Physical Capacity ({config.BUFFER_CAPACITY} billets)'
    )
    ax2.axhline(
        y=config.THROTTLE_THRESHOLD, 
        color='#f2994a', 
        linestyle=':', 
        linewidth=1.8,
        label=f'Dynamic Safety Threshold 80% ({config.THROTTLE_THRESHOLD} billets)'
    )
    ax2.set_title(
        'Optimized Scenario (Prescriptive Digital Twin) - Dynamic Pacing Control', 
        fontsize=11, 
        fontweight='bold'
    )
    ax2.set_xlabel('Shift Elapsed Time (minutes)', fontsize=10)
    ax2.set_ylabel('WIP Level (Billets)', fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left', frameon=True)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"\n[OK] Comparative plot successfully generated and saved to: {save_path}")