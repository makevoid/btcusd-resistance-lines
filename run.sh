set -xe

cd ml

ls ../data

# ~/.local/bin/aws s3 ls s3://$S3BUCKET/
./get.sh

date
python3 ml.py data.csv
ls
date

~/.local/bin/aws s3 cp ml_results.json  s3://$S3BUCKET/
~/.local/bin/aws s3 cp ticks.json       s3://$S3BUCKET/

echo "Done. Visit http://localhost:3000"
