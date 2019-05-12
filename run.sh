set -xe

cd ml

ls ../data

~/.local/bin/aws s3 cp ml.py s3://$S3BUCKET/

date
python3 ml.py ../data/data.csv
ls
date

~/.local/bin/aws s3 cp ml_results.json  s3://$S3BUCKET/
~/.local/bin/aws s3 cp ticks.json       s3://$S3BUCKET/

echo "Done. Visit http://localhost:3000"
