import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


class Anomaly:
    def __init__(self) -> None:
        self.interval = (None, None)


class RandSeqAnomaly:
    def __init__(self, length: int, upperbound=None, lowerbound=None) -> None:
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.seqlength = length


class PointAnomaly:
    def __init__(self, possible_values: list[float], percentage: float) -> None:
        self.possible_values = possible_values
        self.percentage = percentage


class NoiseAnomaly:
    def __init__(self) -> None:
        pass


class SegmentScaleAnomaly:
    def __init__(self) -> None:
        pass
