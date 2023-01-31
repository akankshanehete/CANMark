import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


class createAnomalyIntervals:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.num_intervals = None
        self.points = []

    def create_intervals(self, num_intervals: int, gap_size: int):
        starting_points = []  # contains the starting point for each drift interval
        ending_points = []  # contains the ending point for each drift interval
        self.num_intervals = num_intervals
        evenly_spaced = np.linspace(
            0, len(self.dataset), num=(num_intervals+1))
        starting_points.append(0+1/2*gap_size)
        points = []
        for i in range(1, len(evenly_spaced)):
            ending_points.append(evenly_spaced[i]-(gap_size/2))
        for i in range(1, len(evenly_spaced)-1):
            starting_points.append(evenly_spaced[i]+(gap_size/2))
        for i in range(0, len(starting_points)):
            points.append((starting_points[i], ending_points[i]))
            # print(ending_points[i] - starting_points[i])
        self.points = points
        # print(points)

    def add_anomalies(self, *anomaly_modules):
        if len(anomaly_modules) != len(self.points):
            # throw exception here because the number of anomaly modules must be the same as the number of intervals
            raise ValueError(
                'The number of anomaly modules given is not the same as the number of intervals specified.')
