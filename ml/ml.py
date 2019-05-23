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


def main(filename):
    # Prepare
    # ---
    # read csv files with daily data per tick
    df = pandas.read_csv(filename, parse_dates=[0], index_col=0, names=['Date_Time', 'Buy', 'Sell'],
                         date_parser=lambda x: pandas.to_datetime(x, unit="s"))

    # group by day and drop NA values (usually weekends)
    grouped_data = df.dropna()
    ticks_data = grouped_data['Buy'].resample('24H').ohlc()

    # use 'ask'
    price_data = grouped_data[['Buy']].values

    # Configure
    # ---

    # TODO: write smart configuration based on period (number of days) and frequency (price-range, a higher quantile will create more clusters volatility)

    # calculate bandwidth (expirement with quantile and samples)
    # quantile=0.07 # for 20900000
    quantile=0.12 # for 12000000
    bandwidth = estimate_bandwidth(price_data, quantile=quantile, n_samples=4000)
    ms = MeanShift(n_jobs=12, bandwidth=bandwidth, bin_seeding=True)


    # Fit
    # ---

    # fit the data
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
    ticks_data.to_json('ticks.json', date_format='iso', orient='index')

    # export ml support resisistance
    with open('ml_results.json', 'w') as f:
        f.write(json.dumps(ml_results))


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print('ml.py <inputfile.csv>')
        sys.exit(2)
    main(sys.argv[1])


# from sklearn.externals.joblib import Parallel, parallel_backend

# TODO: add parallel
# from sklearn.externals.joblib import Parallel, parallel_backend

# TODO: add AWS libs
