from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def add_drift(data: pd.DataFrame, start: float, end: float, drift_type: str, drift_scale: float, transition_period=0) -> pd.DataFrame:
    if start < 1:
        cd1 = round(len(data)*start)
    if end < 1:
        cd2 = round(len(data)*end)
    if start > 1:
        cd1 = start
    if end > 1:
        cd2 = end

    if transition_period != 0:
        width = round((cd2-cd1)*transition_period)

    label = data.iloc[:, 1].to_numpy()
    data = data.iloc[:, 0].to_numpy()

    if drift_type == 'mean':
        val = drift_scale * data.mean()

    if drift_type == 'dist':
        val = drift_scale

    if transition_period == 0:
        if drift_type == 'mean':
            data2 = np.concatenate(
                (data[:cd1], data[cd1:cd2] + val, data[cd2:]))
            label2 = label
        # warning: the length of the overall data is changed when adding this type of drift
        elif drift_type == 'dist':
            # in here, val = ratio (if ratio < 1 -> inc. freq.)
            d_temp = data[cd1:cd2]
            wid_len = int((cd2-cd1)*val)
            d_mod = signal.resample(d_temp, wid_len)
            l_temp = label[cd1:cd2]
            l_mod = signal.resample(l_temp, wid_len)
            l_mod = np.round(l_mod)
            # caution! the length of data is changed here
            data2 = np.concatenate((data[:cd1], d_mod, data[cd2:]))
            # caution! the length of data is changed here
            label2 = np.concatenate((label[:cd1], l_mod, label[cd2:]))
    elif transition_period != 0:
        if drift_type == 'mean':
            add1 = np.arange(width)*val/width
            add2 = add1[::-1]
            data2 = np.concatenate(
                (data[:cd1], data[cd1:cd1+width]+add1, data[cd1+width:cd2]+val, data[cd2:cd2+width]+add2, data[cd2+width:]))
            label2 = label
        elif drift_type == 'dist':
            ratio = val
            d_temp1 = data[cd1:cd1+width]
            wid_len = int(width*(1+ratio)/2)
            mod1 = signal.resample(d_temp1, wid_len)
            l_temp1 = label[cd1:cd1+width]
            l1 = signal.resample(l_temp1, wid_len)
            l1 = np.round(l1)

            d_temp2 = data[cd1+width:cd2]
            wid_len = int((cd2-cd1-width)*ratio)
            mod2 = signal.resample(d_temp2, wid_len)
            l_temp2 = label[cd1+width:cd2]
            l2 = signal.resample(l_temp2, wid_len)
            l2 = np.round(l2)

            d_temp3 = data[cd2:cd2+width]
            wid_len = int(width*(1+ratio)/2)
            mod3 = signal.resample(d_temp3, wid_len)
            l_temp3 = label[cd2:cd2+width]
            l3 = signal.resample(l_temp3, wid_len)
            l3 = np.round(l3)

            # print('Compare:', len(mod1), len(mod2), len(mod3))

            data2 = np.concatenate(
                (data[:cd1], mod1, mod2, mod3, data[cd2+width:]))
            label2 = np.concatenate(
                (label[:cd1], l1, l2, l3, label[cd2+width:]))

    data = pd.DataFrame(np.column_stack((data2, label2)))
    return data


# testing (remove code later)
ECG = pd.read_csv('driftadd/MBA_ECG805_data.out')
print(ECG)

ECG = add_drift(ECG, 200, 1600, 'dist', 1.5)

plt.plot(ECG.iloc[0:2500, 0])
plt.show()
