from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# injects random sequence anomalies with upperbound and lowerbound value wherever the user wants in the dataset
def inject_randsequence_anomalies(data: pd.DataFrame, start: float, end: float, lower_bound=0, upper_bound=0, step=0):
    rand_seq_length = end - start
    sample = data.iloc[:, 0].to_numpy()
    data = data.to_numpy()
    decimal_places = len(str(sample[0]).split(".")[1])
    if lower_bound == 0 and upper_bound == 0 and step == 0:
        sequence = np.random.choice(sample, rand_seq_length)
    else:
        num = round((upper_bound - lower_bound)/step)
        sequence = np.random.choice(np.round(np.linspace(
            lower_bound, upper_bound, num=num), decimal_places), rand_seq_length)

    sequence = np.c_[sequence, np.full(len(sequence), 1)]
    data = np.concatenate((data[:start], sequence, data[end:]))

    return pd.DataFrame(data)


# injects point anomalies (user specifies value and amount) into the dataset
def inject_point_anomalies(data: pd.DataFrame, start: float, end: float, lower_bound: float, upper_bound: float, percentage: int):
    pass

# adds (user-specified) scale to a segment of the data, creating a sequence anomaly


def inject_segment_scale_anomalies(data: pd.DataFrame, scale: float, start: int, end: int):
    pass

# adds a custom sequence the user has defined to a segment of the data, injecting custom anomaly


def inject_custom_anomalies(data: pd.DataFrame, anomaly_seq: pd.DataFrame):
    pass

# adds gaussian noise to a segment of data that is desired


def inject_noise(data: pd.DataFrame, start: int, end: int):
    pass


# testing code (remove later)
ECG = pd.read_csv('driftadd/MBA_ECG805_data.out')
print(ECG)

ECG = inject_randsequence_anomalies(
    ECG, 100, 200, lower_bound=-1, upper_bound=2, step=0.01)
plt.plot(ECG.iloc[0:500, 0])
plt.show()
