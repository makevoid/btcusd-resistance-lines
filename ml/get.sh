wget https://api.bitcoincharts.com/v1/csv/bitstampUSD.csv.gz
gunzip bitstampUSD.csv.gz

# Cut only latest period
# tail -20900000 bitstampUSD.csv > data.csv
tail -100000 bitstampUSD.csv > data.csv
