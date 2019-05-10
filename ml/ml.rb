require './env' # rjs loaded - more infos:
Require.('pandas')
Require.('sklearn/cluster')
Require.('sklearn/cluster/meanshift')

main = ->
  # digits = datasets.load_digits()
  # puts digits.images[0]
  #
  #
  # # group by day and drop NA values (usually weekends)
  # grouped_data = df.dropna()
  # ticks_data = grouped_data['Buy'].resample('24H').ohlc()

main.()
