import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from anomaly import *


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
        for i in range(0, len(self.points)):
            if type(anomaly_modules[i]) == PointAnomaly:
                self.add_Point_Anomaly(
                    self.points[i][0], self.points[i][1], anomaly_modules[i].percentage, anomaly_modules[i].possible_values)

            elif type(anomaly_modules[i]) == CollectiveAnomaly:
                pass
            elif type(anomaly_modules[i] == SequentialAnomaly):
                pass

            else:
                raise ValueError(
                    "Wrong type of input parameter, must be anomaly modules.")

    def add_RandSeqAnomaly(self, length: int, percentage: float, upperbound: float = None, lowerbound: float = None) -> None:
        pass

    # adds point anomalies within specified intervals
    def add_Point_Anomaly(self, start: int, end: int, percentage: float, possible_values: list[float] = None) -> None:
        insertion_indexes = np.random.choice(
            np.arange(start, end), int(percentage*(end-start)))
        for index in insertion_indexes:
            self.dataset.loc[index, 0] = np.random.choice(
                possible_values)  # setting the anomaly
            self.dataset.loc[index, 1] = 1  # setting the label as anomalous

    def add_Noise_Anomaly(self, start: int, end: int, scale: float, gaussian: bool = False, mu: float = None, std: float = None) -> None:
        pass

    def add_SegmentScaleAnomaly(self, start: int, end: int, scale: float, width: int) -> None:
        self.dataset.iloc[start:end, 0] = scale * \
            self.dataset.iloc[start:end, 0]

    def add_CustomAnomaly(self, start: int, end: int, anomaly_segment: pd.DataFrame) -> None:
        pass

    def plot_dataset(self):
        plt.figure(figsize=(100, 30))
        plt.plot(self.dataset.iloc[:, 0])
        for point in self.points:
            plt.axvline(x=point[0], color='r', linestyle="--", linewidth=4)
            plt.axvline(x=point[1], color='r', linestyle="--", linewidth=4)
        plt.show()
