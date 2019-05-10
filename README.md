# Chart Annotator - Resistance Lines

### Automatically find resistance lines in pricing trading data

This repo has an example of an annotated SciKit Learn example of ML Classification using the Clustering Algo Meanshift

The target of this code is to find resistance lines in trading chart data (OHLC)

The target was to have a useful example with very little code


### Installation


Run:

    ./setup.sh

This will install everything and it will also automatically starts an HTTP server

Otherwise you can run the http server via

    python -m SimpleHTTPServer 3000


### Running


To execute the "data crunching" and "chart annotating" job, use run.sh:

    ./run.sh

Then visit http://localhost:3000/


### Docs

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html

https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-adds-scikit-learn-support/

### Sources / Extra

https://github.com/aws/sagemaker-scikit-learn-container


Project forked from https://github.com/jonromero/forex_algotrading
