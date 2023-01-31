import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


class Anomaly:
    def __init__(self) -> None:
        self.interval = (None, None)


class RandSeqAnomaly:
    def __init__(self, length: int, upperbound=None, lowerbound=None) -> None:
        # if upperbound and lowerbound not given, then random sequence anomaly can be generated using random values already present in the data
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.seqlength = length


class PointAnomaly:
    def __init__(self, percentage: float, possible_values=None) -> None:
        # if possible values are not given, a set of possible values will be generated from the dataset as default
        self.possible_values = possible_values
        self.percentage = percentage


class NoiseAnomaly:
    def __init__(self) -> None:
        pass


class SegmentScaleAnomaly:
    def __init__(self, scale) -> None:
        self.scale = scale
