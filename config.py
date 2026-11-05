"""
Config and operational parameters of the Digital Twin(ArcelorMittal Gijon).
"""

# Sim parameters
SIM_TIME = 480          # 1 full shift  = 480 minutes (8 hours)
RANDOM_SEED = 42        # Methodologic standard for simulation

# Buffer place
BUFFER_CAPACITY = 25    # (C_max)
INITIAL_BUFFER_WIP = 5  # Initial ammount of pieces (it is rarely 0)

# Nominal cycle times (minutes)
CASTING_MEAN = 12.0     
CASTING_STD = 1.5       
ROLLING_MEAN = 10.0     
ROLLING_STD = 1.0       

# Rolling mill reliability
FAILURE_PROBABILITY = 0.10  # (10%)
MTTR_MIN = 8.0              # Minimum fix time (minutes)
MTTR_MAX = 20.0             # Maximum fix time (minutes)

# Control Prescriptivo (Gemelo Digital Activo)
THROTTLE_THRESHOLD = 20     # Security bound for stopping (80% of the capacity of the buffer)
