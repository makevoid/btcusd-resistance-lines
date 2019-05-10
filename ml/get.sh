wget https://api.bitcoincharts.com/v1/csv/bitstampUSD.csv.gz
gunzip bitstampUSD.csv.gz

# Cut only latest period (from previous cycle high)
tail -20900000 bitstampUSD.csv > data.csv

# Cut only latest period (from this year)
# tail -12000000 bitstampUSD.csv > data.csv
