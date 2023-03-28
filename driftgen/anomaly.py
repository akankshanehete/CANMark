import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


# injects a random sequence of anomalies (i.e collective anomaly)
class CollectiveAnomaly:
    def __init__(self, length: int, percentage: float, distribution: str = 'uniform', upperbound: float = None, lowerbound: float = None, mu: float = None, std: float = None, skew=None, num_values: int = 5) -> None:
        # if upperbound and lowerbound not given, then random sequence anomaly can be generated using random values already present in the data
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.length = length  # specifies the length of the random sequence
        self.percentage = percentage
        self.dist = distribution
        self.mean = mu
        self.std = std
        self.num_values = num_values
        self.skew = skew


class CorrelationAnomaly:
    def __init__(self, percentage, min_noise, max_noise, correlation_min, correlation_max, correlation_step, length=20) -> None:
        self.min_noise = min_noise
        self.max_noise = max_noise
        self.percentage = percentage
        self.correlation_min = correlation_min
        self.correlation_max = correlation_max
        self.correlation_step = correlation_step
        self.length = length


# # injects point anomalies in the dataset, the fraction of anomalous data can be specified by the percentage parameter that the user can specify
# class PointAnomaly:
#     def __init__(self, percentage: float, possible_values: list[float] = None) -> None:
#         # if possible values are not given, a set of possible values will be generated from the dataset as default
#         self.possible_values = possible_values
#         self.percentage = percentage


class PointAnomaly:
    def __init__(self, percentage: float, distribution: str = 'uniform', mu: float = None, std: float = None, num_values: int = 5, lowerbound=None, upperbound=None, skew=None) -> None:
        self.percentage = percentage
        self.dist = distribution
        self.mean = mu
        self.std = std
        self.num_values = num_values
        self.skew = skew
        self.lowerbound = lowerbound
        self.upperbound = upperbound

# injects sequential anomalies into the dataset (collective anomalies that keep repeating)


class SequentialAnomaly:
    def __init__(self, percentage: float, noise_factor: int, start=None, end=None, length=15):
        self.length = length
        self.percentage = percentage
        self.noise_factor = noise_factor
        self.start = start
        self.end = end
