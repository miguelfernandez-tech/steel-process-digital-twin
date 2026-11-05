"""
Config and operational parameters of the Digital Twin(ArcelorMittal Gijon).
"""

# Sim parameters
SIM_TIME = 480          # 1 full shift  = 480 minutes (8 hours)
RANDOM_SEED = 42        # Methodologic standard for simulation

# Buffer place
BUFFER_CAPACITY = 12    # (C_max)
INITIAL_BUFFER_WIP = 5  # Initial ammount of pieces (it is rarely 0)

# Nominal cycle times (minutes)
CASTING_MEAN = 11.5     
CASTING_STD = 1.5       
ROLLING_MEAN = 11.0     
ROLLING_STD = 1.0       

# Rolling mill reliability
FAILURE_PROBABILITY = 0.15  # (15%)
MTTR_MIN = 12.0              # Minimum fix time (minutes)
MTTR_MAX = 30.0             # Maximum fix time (minutes)

# Control Prescriptivo (Gemelo Digital Activo)
THROTTLE_THRESHOLD = 6     # Security bound for stopping (50% of the capacity of the buffer)
