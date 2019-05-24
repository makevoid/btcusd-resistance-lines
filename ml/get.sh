set -xe

curl https://api.bitcoincharts.com/v1/csv/bitstampUSD.csv.gz > bitstampUSD.csv.gz
gunzip -f bitstampUSD.csv.gz

# Cut only latest period (from previous cycle high)
# tail -20900000 bitstampUSD.csv > data.csv

# Cut only latest period (from this year)
# tail -12000000 bitstampUSD.csv > data.csv

# Cut only latest period (recent uptrend)
tail -5000000 bitstampUSD.csv > data.csv


rm -f bitstampUSD.csv.gz bitstampUSD.csv
