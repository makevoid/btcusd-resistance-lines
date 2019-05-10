"""
Find the support/resistance lines in a chart

@JonV / May 2015
@makevoid / May 2019
"""

# https://api.bitcoincharts.com/v1/csv/
# 'Date_Time', 'Buy', 'Sell'

import sys
import json
import pandas
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

# from joblib import parallel
from joblib import parallel_backend
from joblib.parallel import register_parallel_backend

# from joblib._parallel_backends import AutoBatchingMixin
from dask.distributed import Client, LocalCluster
import dask.dataframe as dataf
import multiprocessing as mp
import os

# min_ideal_batch_duration = 1.
# AutoBatchingMixin.MIN_IDEAL_BATCH_DURATION = min_ideal_batch_duration
# AutoBatchingMixin.MAX_IDEAL_BATCH_DURATION = 10 * min_ideal_batch_duration

def main(filename):
    cluster = LocalCluster(n_workers=1, threads_per_worker=1, processes=False)
    client = Client(cluster)

    # Prepare
    # ---
    # read csv files with daily data per tick
    df = pandas.read_csv(filename, parse_dates=[0], index_col=0, names=['Date_Time', 'Buy', 'Sell'],
                         date_parser=lambda x: pandas.to_datetime(x, unit="s"))

    # df2 = pandas.read_csv(filename, parse_dates=[0], index_col=0, names=['Date_Time', 'Buy', 'Sell'],
                         # date_parser=lambda x: pandas.to_datetime(x, unit="s"))

    # df2 = pandas.read_csv(filename, parse_dates=[0],  names=['Date_Time', 'Buy', 'Sell'],
    #                      date_parser=lambda x: pandas.to_datetime(x, unit="s")).set_index('Date_Time')

    df = dataf.from_pandas(df, npartitions=1)

    # group by day and drop NA values (usually weekends)
    grouped_data = df.dropna()
    ticks_data = grouped_data['Buy'].resample('24H').ohlc()

    price_data = grouped_data[['Buy']].values
    price_data = price_data.compute()

    # print(price_data)


    # Configure
    # ---

    # TODO: write smart configuration based on number of days

    # calculate bandwidth (expirement with quantile and samples)
    bandwidth = estimate_bandwidth(price_data, quantile=0.07, n_samples=4000)

    print("meanshift")
    ms = MeanShift(n_jobs=12,  bandwidth=bandwidth, bin_seeding=True, cluster_all=True, min_bin_freq=1)


    # Fit
    # ---

    # fit the data
    print("Fit")


    with parallel_backend('dask'):
        ms.fit(price_data)

    # Export
    # ---
    ml_results = []
    for k in range(len(np.unique(ms.labels_))):
        my_members = ms.labels_ == k
        values = price_data[my_members, 0]

        # find the edges
        ml_results.append(min(values))
        ml_results.append(max(values))


    # Save
    # ---
    # export the data for the visualizations
    ticks_data.to_json('ticks', date_format='iso', orient='index')

    os.system('mv ticks/0.part ticks/ticks.json')

    # export ml support resisistance
    with open('ml_results.json', 'w') as f:
        f.write(json.dumps(ml_results))


if __name__=='__main__':
    # mp.freeze_support()

    if (len(sys.argv) < 2):
        print('ml.py <inputfile.csv>')
        sys.exit(2)

    main(sys.argv[1])


# TODO: add AWS libs
