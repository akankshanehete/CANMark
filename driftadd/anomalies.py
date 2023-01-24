from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# injects random sequence anomalies with upperbound and lowerbound value wherever the user wants in the dataset
def inject_randsequence_anomalies(data: pd.DataFrame, start: float, end: float, lower_bound: float, upper_bound: float):
    pass

# injects point anomalies (user specifies value and amount) into the dataset


def inject_point_anomalies(data: pd.DataFrame, start: float, end: float, lower_bound: float, upper_bound: float, percentage: int):
    pass

# adds (user-specified) scale to a segment of the data, creating a sequence anomaly


def inject_segment_scale_anomalies(data: pd.Dataframe, scale: float, start: int, end: int):
    pass

# adds a custom sequence the user has defined to a segment of the data, injecting custom anomaly


def inject_custom_anomalies(data: pd.DataFrame, anomaly_seq: pd.DataFrame):
    pass

# adds gaussian noise to a segment of data that is desired


def inject_noise(data: pd.DataFrame, start: int, end: int):
    pass
