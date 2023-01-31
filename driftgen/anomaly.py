import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


# injects a random sequence of anomalies
class RandSeqAnomaly:
    def __init__(self, length: int, upperbound: float = None, lowerbound: float = None) -> None:
        # if upperbound and lowerbound not given, then random sequence anomaly can be generated using random values already present in the data
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.seqlength = length  # specifies the length of the random sequence


# injects point anomalies in the dataset, the fraction of anomalous data can be specified by the percentage parameter that the user can specify
class PointAnomaly:
    def __init__(self, percentage: float, possible_values: list[float] = None) -> None:
        # if possible values are not given, a set of possible values will be generated from the dataset as default
        self.possible_values = possible_values
        self.percentage = percentage

# allows user to insert gaussian or random noise according to user-specified scale, mean, standard deviation


class NoiseAnomaly:
    def __init__(self, scale: float, gaussian: bool = False, mu: float = None, std: float = None) -> None:
        self.scale = scale
        self.gaussian = gaussian  # if gaussian is false, the anomalies use random noise
        self.mean = mu
        self.std = std

# a user-specified scale is applied to a certain segment of the data, affecting the variance of data in that region


class SegmentScaleAnomaly:
    def __init__(self, scale: float) -> None:
        self.scale = scale
