import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy.stats import skewnorm
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
            # depending on type of anomaly module, the insertion parameters are different
            if type(anomaly_modules[i]) == PointAnomaly:
                self.add_dist_point_anomaly(
                    self.points[i][0], self.points[i][1], anomaly_modules[i].percentage, anomaly_modules[i].dist,
                    anomaly_modules[i].mean, anomaly_modules[i].std, anomaly_modules[i].num_values,
                    anomaly_modules[i].upperbound, anomaly_modules[i].lowerbound, anomaly_modules[i].skew)

            elif type(anomaly_modules[i]) == CollectiveAnomaly:
                self.add_Collective_Anomaly(
                    self.points[i][0], self.points[i][1], anomaly_modules[i].length, anomaly_modules[i].percentage,
                    anomaly_modules[i].dist, anomaly_modules[i].mean, anomaly_modules[i].std, anomaly_modules[i].num_values,
                    anomaly_modules[i].upperbound, anomaly_modules[i].lowerbound, anomaly_modules[i].skew
                )

            elif type(anomaly_modules[i]) == CorrelationAnomaly:
                self.add_correlation_anomaly(self.points[i][0], self.points[i][1], anomaly_modules[i].percentage, anomaly_modules[i].min_noise,
                                             anomaly_modules[i].max_noise, anomaly_modules[i].correlation_min, anomaly_modules[
                                                 i].correlation_max, anomaly_modules[i].correlation_step,
                                             anomaly_modules[i].length)
            elif type(anomaly_modules[i]) == SequentialAnomaly:
                self.add_sequential_anomaly(
                    self.points[i][0], self.points[i][1], anomaly_modules[i].percentage,
                    anomaly_modules[i].noise_factor, anomaly_modules[i].start, anomaly_modules[i].end, anomaly_modules[i].length
                )
            else:
                raise ValueError(
                    "Wrong type of input parameter, must be anomaly modules.")

    # adds point anomalies within specified intervals

    def add_Point_Anomaly(self, start: int, end: int, percentage: float, possible_values: list[float] = None) -> None:
        insertion_indexes = np.random.choice(
            np.arange(start, end), int(percentage*(end-start)))
        for index in insertion_indexes:
            self.dataset.loc[index, 0] = self.dataset.loc[index, 0] * \
                np.random.choice(possible_values)  # setting the anomaly
            self.dataset.loc[index, 1] = 1  # setting the label as anomalous

    # adds point anomalies according to a distribution
    def add_dist_point_anomaly(self, start: int, end: int, percentage: float, distribution, mu, std, num_values, upperbound, lowerbound, skew):
        if mu == None:
            mu = self.dataset[int(start):int(end)].mean() * 3
        if std == None:
            std = self.dataset[int(start):int(end)].std() * 3
        if distribution == 'uniform':
            possible_values = np.random.uniform(
                lowerbound, upperbound, num_values)
        elif distribution == 'skew':
            possible_values = skewnorm.rvs(
                a=skew, loc=upperbound, size=num_values)
            possible_values = possible_values - min(possible_values)
            possible_values = possible_values / max(possible_values)
            possible_values = possible_values * upperbound
            # plotting histogram for debugging
            # plt.hist(possible_values, 30, density=True, color='red', alpha=0.1)
            # plt.show()

        elif distribution == 'gaussian':
            possible_values = np.random.normal(mu, std, num_values)
        else:
            raise ValueError(
                'Wrong distribution specification. Please enter either uniform, skew, or gaussian')

        # indexes where the anomaly will be inserted
        # print(possible_values)
        insertion_indexes = np.random.choice(
            np.arange(start, end-1), int(percentage*(end-start)))
        # print("insertion indexes:")
        # print(insertion_indexes)

        for index in insertion_indexes:
            # print(index)
            # setting the anomaly
            self.dataset.iloc[int(
                index), 0] += self.dataset.iloc[int(index), 0] * np.random.choice(possible_values)
            # setting the label as anomalous
            self.dataset.iloc[int(index), 1] = 1

    def add_Collective_Anomaly(self, start: int, end: int, length: int, percentage: float, distribution, mu, std, num_values, upperbound, lowerbound, skew):

        number_anomalies = math.ceil(((end-start)/length)*percentage)
        # print("number of anomalies")
        # print(number_anomalies)

        if mu == None:
            mu = self.dataset[int(start):int(end)].mean() * 3
        if std == None:
            std = self.dataset[int(start):int(end)].std() * 3
        if distribution == 'uniform':
            possible_values = np.random.uniform(
                lowerbound, upperbound, num_values)
        elif distribution == 'skew':
            possible_values = skewnorm.rvs(
                a=skew, loc=upperbound, size=num_values)
            possible_values = possible_values - min(possible_values)
            possible_values = possible_values / max(possible_values)
            possible_values = possible_values * upperbound
            # plotting histogram for debugging
            # plt.hist(possible_values, 30, density=True, color='red', alpha=0.1)
            # plt.show()

        elif distribution == 'gaussian':
            possible_values = np.random.normal(mu, std, num_values)
        else:
            raise ValueError(
                'Wrong distribution specification. Please enter either uniform, skew, or gaussian')

        insertion_indexes = np.random.choice(
            np.arange(start, end, length), number_anomalies)
        # creating the collective sequence
        collective_sequences = []
        for _ in range(number_anomalies):
            collective_sequences.append(
                np.random.choice(possible_values, length))

        # inserting collective anomalies at required index
        for i in range(0, len(insertion_indexes)):
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 0] = np.multiply(collective_sequences[i], self.dataset.iloc[int(insertion_indexes[i]): int(
                    insertion_indexes[i]) + length, 0]) + self.dataset.iloc[int(insertion_indexes[i]): int(
                        insertion_indexes[i]) + length, 0]
            # setting the label as anomalous
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 1] = 1

    def add_correlation_anomaly(self, start, end, percentage, min_noise, max_noise, correlation_min, correlation_max, correlation_step, length):
        # creating an anomaly sequence that we will gradually add noise to
        starting = int(np.random.choice(np.arange(start, end-length)))
        anomaly_sequence = self.dataset.iloc[starting:starting +
                                             length, 0].to_numpy()
        possible_values = np.random.uniform(min_noise, max_noise, length)

        processed_anomaly_sequence = np.add(np.multiply(
            possible_values, anomaly_sequence), anomaly_sequence)
        number_anomalies = math.ceil(((end-start)/length)*percentage)

        anom_sequences = []
        counter = 0
        for i in range(correlation_min, correlation_max, correlation_step):
            counter += 1
            anom_sequences.append(processed_anomaly_sequence + i)

        if len(anom_sequences) > number_anomalies:
            anom_sequences = anom_sequences[:number_anomalies]
        elif len(anom_sequences) < number_anomalies:
            last = anom_sequences[-1]
            for i in range(len(anom_sequences), number_anomalies-1):
                anom_sequences[i] = last

        # for debugging purposes
        # print(anom_sequences)

        insertion_indexes = np.random.choice(
            np.arange(start, end, length), number_anomalies)
        for i in range(0, len(insertion_indexes)):
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 0] = anom_sequences[i]
            # setting the label as anomalous
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 1] = 1

    def add_sequential_anomaly(self, start, end, percentage, noise_factor, starting, ending, length):
        if starting == None and ending == None:
            starting = int(np.random.choice(np.arange(start, end-length)))
            anomaly_sequence = self.dataset.iloc[starting:starting +
                                                 length, 0].to_numpy()

        if ending == None:
            anomaly_sequence = self.dataset.iloc[starting:starting +
                                                 length, 0].to_numpy()
        else:
            anomaly_sequence = self.dataset.iloc[starting:ending, 0].to_numpy()
            length = ending - starting

        # print("anomaly sequence: " + str(anomaly_sequence))

        num_anomalies = math.ceil(((end-start)/length)*percentage)
        # print("number of anomalies:" + str(num_anomalies))

        mid_insertions = np.linspace(start, end, num_anomalies)
        insertion_indexes = []
        for index in mid_insertions:
            insertion_indexes.append(int(math.ceil(index-length/2)))

        # add noise processing here
        noise = np.random.normal(0, noise_factor, len(anomaly_sequence))
        # print(noise)
        anomaly_sequence = anomaly_sequence + noise

        # insertine sequential anomalies at required index
        for i in range(0, len(insertion_indexes)):
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 0] = anomaly_sequence
            # setting the label as anomalous
            self.dataset.iloc[int(insertion_indexes[i]): int(
                insertion_indexes[i]) + length, 1] = 1

    def plot_dataset(self):
        plt.figure(figsize=(100, 30))
        plt.plot(self.dataset.iloc[:, 0])
        for point in self.points:
            plt.axvline(x=point[0], color='r', linestyle="--", linewidth=4)
            plt.axvline(x=point[1], color='r', linestyle="--", linewidth=4)
        plt.show()
