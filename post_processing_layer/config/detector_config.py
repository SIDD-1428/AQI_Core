"""
Configuration for all detector modules.
"""


SPIKE_THRESHOLDS = {
    "temperature": 5.0,
    "humidity": 15.0,
    "pressure": 8.0,
    "pm1_0": 20.0,
    "pm2_5": 25.0,
    "pm10": 30.0,
    "co": 20.0,
    "no2": 20.0,
    "so2": 20.0,
    "o3": 20.0,
    "nh3": 20.0,
    "aqi": 25.0,
}

DRIFT_THRESHOLDS = {
    "temperature": 2.0,
    "humidity": 5.0,
    "pressure": 3.0,
    "pm1_0": 10.0,
    "pm2_5": 10.0,
    "pm10": 10.0,
    "co": 10.0,
    "no2": 10.0,
    "so2": 10.0,
    "o3": 10.0,
    "nh3": 10.0,
    "aqi": 10.0,
}
DRIFT_WINDOW_SIZE=10
DRIFT_MIN_TREND_RATIO=0.7


STAGNATION_LIMITS = {
    "temperature": 10,
    "humidity": 10,
    "pressure": 10,
    "pm1_0": 10,
    "pm2_5": 10,
    "pm10": 10,
    "co": 10,
    "no2": 10,
    "so2": 10,
    "o3": 10,
    "nh3": 10,
    "aqi": 10,
}
STAGNATION_TOLERANCE=0.01

ANOMALY_THRESHOLDS = {}