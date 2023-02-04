import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


class createDriftIntervals:
    def __init__(self, dataset: pd.DataFrame) -> None:
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

    def add_drifts(self, *drift_modules):
        if len(drift_modules) != len(self.points):
            # throw exception here because the number of drift modules must be the same as the number of intervals
            raise ValueError(
                'The number of drift modules given is not the same as the number of intervals specified.')

        for i in range(0, len(self.points)):
            # print(drift_modules[i])
            self.inject_drift(int(self.points[i][0]), int(self.points[i][1]), drift_modules[i].drift_type,
                              drift_modules[i].drift_scale, drift_modules[i].transition_period)

    def inject_drift(self, start: float, end: float, drift_type: str, drift_scale: float, transition_period=0) -> pd.DataFrame:
        if start < 1:
            cd1 = round(len(self.dataset)*start)
        if end < 1:
            cd2 = round(len(self.dataset)*end)
        if start > 1:
            cd1 = start
        if end > 1:
            cd2 = end

        if transition_period != 0:
            width = round((cd2-cd1)*transition_period)

        label = self.dataset.iloc[:, 1].to_numpy()
        self.dataset = self.dataset.iloc[:, 0].to_numpy()

        if drift_type == 'mean':
            # change to interval of that section only
            val = drift_scale * self.dataset[start:end].mean()

        if drift_type == 'dist':
            val = drift_scale

        if transition_period == 0:
            if drift_type == 'mean':
                data2 = np.concatenate(
                    (self.dataset[:cd1], self.dataset[cd1:cd2] + val, self.dataset[cd2:]))
                label2 = label
            # warning: the length of the overall self.dataset is changed when adding this type of drift
            elif drift_type == 'dist':
                # in here, val = ratio (if ratio < 1 -> inc. freq.)
                d_temp = self.dataset[cd1:cd2]
                wid_len = int((cd2-cd1)*val)
                d_mod = signal.resample(d_temp, wid_len)
                l_temp = label[cd1:cd2]
                l_mod = signal.resample(l_temp, wid_len)
                l_mod = np.round(l_mod)
                # caution! the length of self.dataset is changed here
                data2 = np.concatenate(
                    (self.dataset[:cd1], d_mod, self.dataset[cd2:]))
                # caution! the length of self.dataset is changed here
                label2 = np.concatenate((label[:cd1], l_mod, label[cd2:]))
        elif transition_period != 0:
            if drift_type == 'mean':
                add1 = np.arange(width)*val/width
                add2 = add1[::-1]
                data2 = np.concatenate(
                    (self.dataset[:cd1], self.dataset[cd1:cd1+width]+add1, self.dataset[cd1+width:cd2]+val, self.dataset[cd2:cd2+width]+add2, self.dataset[cd2+width:]))
                label2 = label
            elif drift_type == 'dist':
                ratio = val
                d_temp1 = self.dataset[cd1:cd1+width]
                wid_len = int(width*(1+ratio)/2)
                mod1 = signal.resample(d_temp1, wid_len)
                l_temp1 = label[cd1:cd1+width]
                l1 = signal.resample(l_temp1, wid_len)
                l1 = np.round(l1)

                d_temp2 = self.dataset[cd1+width:cd2]
                wid_len = int((cd2-cd1-width)*ratio)
                mod2 = signal.resample(d_temp2, wid_len)
                l_temp2 = label[cd1+width:cd2]
                l2 = signal.resample(l_temp2, wid_len)
                l2 = np.round(l2)

                d_temp3 = self.dataset[cd2:cd2+width]
                wid_len = int(width*(1+ratio)/2)
                mod3 = signal.resample(d_temp3, wid_len)
                l_temp3 = label[cd2:cd2+width]
                l3 = signal.resample(l_temp3, wid_len)
                l3 = np.round(l3)

                # print('Compare:', len(mod1), len(mod2), len(mod3))

                data2 = np.concatenate(
                    (self.dataset[:cd1], mod1, mod2, mod3, self.dataset[cd2+width:]))
                label2 = np.concatenate(
                    (label[:cd1], l1, l2, l3, label[cd2+width:]))

        self.dataset = pd.DataFrame(np.column_stack((data2, label2)))

    def plot_dataset(self):
        plt.figure(figsize=(100, 30))
        plt.plot(self.dataset.iloc[:, 0])
        for point in self.points:
            plt.axvline(x=point[0], color='r', linestyle="--", linewidth=4)
            plt.axvline(x=point[1], color='g', linestyle="--", linewidth=4)
        plt.show()


# testing code: remove later
ECG = pd.read_csv(
    '/Users/akanksha/Desktop/DriftGen/driftgen/MBA_ECG805_data.out')
ECG_intervals = createDriftIntervals(ECG)
ECG_intervals.create_intervals(5, 500)
