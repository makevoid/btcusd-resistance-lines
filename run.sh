
set -xe

cd ml

source /tmp/chart-annotator/bin/activate

time python3 ml.py data.csv

echo "Done. Visit http://localhost:3000"
