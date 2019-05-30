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

### Screenshot

Images sometimes are better than many words :D 

recent image (may '19)


![](https://raw.githubusercontent.com/makevoid/chart-annotator-resistance-lines/a380830360e6b0dbc2c1c98b2639dccf3d9007b1/tmp/4-years-cycle-restarting-1.png?raw=true)

first image produced 1 month before

![](https://github.com/makevoid/chart-annotator-resistance-lines/blob/master/tmp/resistance-lines-ml-classification-meanshift.png?raw=true)

If you want to use it "as it is" you will need to configure the AWS S3 credentials as that's the current way I'm saving/publishing the results. You want to comment all that code if you just to run it locally instead of automated inside docker. 

You probably want also to tune `quantile` for the MeanShift clusterization to match the current price action. A range in between x and x should do that (The target is to find a `quantile` value that generates min 3-4 to max 8-10 clusters)

Enjoy!

@makevoid

