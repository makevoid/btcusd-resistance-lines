# Chart Annotator - Resistance Lines

### Automatically find resistance lines in pricing trading data 

This repo has an example of an annotated SciKit Learn example of ML Classification using the Clustering Algo Meanshift

The target of this code is to find resistance lines in trading chart data (OHLC)

The target was to have a useful example with very little code


### Installation


pip install -r requirements.txt


### Running 

Then run the ml.py
> python ml.py data/sample.csv

When the algorithm completes, start a python webserver

> python3 -m http.server 3000

or 

> python -m SimpleHTTPServer 3000

and open your browser to http://0.0.0.0:3000/chart.html



### Docs

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html

https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-adds-scikit-learn-support/

### Sources / Extra

https://github.com/aws/sagemaker-scikit-learn-container


Project forked from https://github.com/jonromero/forex_algotrading
 
