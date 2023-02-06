import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


# injects a random sequence of anomalies (i.e collective anomaly)
class CollectiveAnomaly:
    def __init__(self, length: int, percentage: float, upperbound: float = None, lowerbound: float = None) -> None:
        # if upperbound and lowerbound not given, then random sequence anomaly can be generated using random values already present in the data
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.seqlength = length  # specifies the length of the random sequence
        self.percentage = percentage


# injects point anomalies in the dataset, the fraction of anomalous data can be specified by the percentage parameter that the user can specify
class PointAnomaly:
    def __init__(self, percentage: float, possible_values: list[float] = None) -> None:
        # if possible values are not given, a set of possible values will be generated from the dataset as default
        self.possible_values = possible_values
        self.percentage = percentage


class DistPointAnomaly:
    def __init__(self, percentage: float, distribution: str = 'uniform', mu: float = None, std: float = None, num_values: int = 5) -> None:
        self.percentage = percentage
        self.dist = distribution
        self.mean = mu
        self.std = std
        self.num_values = num_values


# injects sequential anomalies into the dataset (collective anomalies that keep repeating)
class SequentialAnomaly:
    def __init__(self, length: int, percentage: float, values: list, lowerbound: float = None, upperbound: float = None, distribution: str = None, mu: float = None, std: float = None) -> None:
        self.length = length  # length of recurrent anomaly sequence
        # frequence of recurrence (period between recurrencies will be defined solely by length and percentage)
        self.percentage = percentage
        # upperbound float of values for random sequence, if given
        self.upperbound = upperbound
        # lowerbound float of values for random sequence, if given
        self.lowerbound = lowerbound
        if distribution == None:
            self.dist = 'uniform'
        else:
            self.dist = distribution
        # uniform, normal, skewed (mean and standard deviation given)
        self.distribution = distribution
