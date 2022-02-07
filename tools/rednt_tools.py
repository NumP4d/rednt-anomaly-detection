# Import all needed Python modules
import os
import pandas as pd
import numpy as np
import time
import datetime
import scipy
from hampel import hampel
import matplotlib.pyplot as plt

#plt.rcParams["figure.figsize"]=30,30

DATA_DIR = 'data'
VIBRATION_FILENAME = os.path.join(DATA_DIR, 'SCUd_134t_drgania.csv')
TEMPERATURE_FILENAME = os.path.join(DATA_DIR, 'SCUd_134t_temperatura.csv')
V_HEADER_NAMES = ['timestamp', 'vibration']
T_HEADER_NAMES = ['timestamp', 'temperature']
SEP = ';'
SAMPLE_TIME_SEC = 4*60


def plot_timeseries_data(df_in, style='.'):
    fig, axes = plt.subplots(nrows=2, ncols=1)
    df_in.vibration.plot(ax=axes[0], title='vibrations',
                         legend=False, style=style)
    df_in.temperature.plot(ax=axes[1], title='temperature',
                           legend=False, style=style)
    plt.show()


def date_parser(date):
    return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')


def remove_outliers(data):
    [filtered_data, _] = hampel(data)
    return filtered_data
