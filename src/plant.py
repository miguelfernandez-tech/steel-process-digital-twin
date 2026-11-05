import simpy
import random
import config

class SteelPlantModel:
    def __init__(self, env, prescriptive_mode=False):
        self.env = env
        self.prescriptive_mode = prescriptive_mode
        self.buffer = simpy.Container(env, capacity=config.BUFFER_CAPACITY, init=config.INITIAL_BUFFER_WIP)
        self.rolling_mill = simpy.Resource(env, capacity=1)
        
        self.produced_billets = 0
        self.cold_diverted_billets = 0
        self.log_data = []

    def log_state(self):
        """Tracks system status in temporal series."""
        self.log_data.append({
            'Time': round(self.env.now, 2),
            'WIP': self.buffer.level,
            'Buffer_Cap': self.buffer.capacity,
            'Throughput': self.produced_billets,
            'Cold_Diverted': self.cold_diverted_billets
        })

def casting_process(env, plant):
    """Continuous Casting Process with regulation."""
    while True:
        # Control: If buffer reaches the boundary, it reduces the speed
        if plant.prescriptive_mode and plant.buffer.level >= config.THROTTLE_THRESHOLD:
            mean_cycle = config.CASTING_MEAN * 1.35  # It reduces 35%
        else:
            mean_cycle = config.CASTING_MEAN

        yield env.timeout(max(1.0, random.normalvariate(mean_cycle, config.CASTING_STD)))

        if plant.buffer.level < plant.buffer.capacity:
            yield plant.buffer.put(1)
        else:
            plant.cold_diverted_billets += 1  # Thermal loss beacuse of being in the cold place
        
        plant.log_state()

def rolling_process(env, plant):
    """Rolling Process with random stops."""
    while True:
        yield plant.buffer.get(1)
        with plant.rolling_mill.request() as req:
            yield req
            # Rolling in hot
            yield env.timeout(max(1.0, random.normalvariate(config.ROLLING_MEAN, config.ROLLING_STD)))

            # Random stop of the rolling mill
            if random.random() < config.FAILURE_PROBABILITY:
                downtime = random.uniform(config.MTTR_MIN, config.MTTR_MAX)
                yield env.timeout(downtime)

            plant.produced_billets += 1
            plant.log_state()

def periodic_monitor(env, plant, interval=2.0):
    """Periodic continuous sampling of variables."""
    while True:
        plant.log_state()
        yield env.timeout(interval)
