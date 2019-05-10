set -xe

echo "Installing python packages"

python3 -m venv /tmp/chart-annotator

source /tmp/chart-annotator/bin/activate

pip install -r requirements.txt

cd ml

echo "Downloading Bitfinex USD historical prices"
./get.sh

echo "Starting Server"
cd ml

python -m SimpleHTTPServer 3000
