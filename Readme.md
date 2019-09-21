# btcusd-resistance-lines

### Example of a Chart Annotator script that draws Resistance Lines (.py - scikitlearn - meanshift)

#### Automatically finds resistance lines in pricing trading data

This repo has an example of an annotated SciKit Learn example of ML Classification using the Clustering Algo Meanshift

Uses bitstamp BTC/USD historic value from api.bitcoincharts.com

The target of this code is to find resistance lines in trading chart data (OHLC) 

The codebase is simple, this is a fork of the forex_algotrading project, please check the "sources" section of this readme for info about the original repo


### Installation


Run:

    ./setup.sh

This will install everything and it will also automatically starts an HTTP server


### Running


To execute the "data crunching" and "chart annotating" job, use run.sh:

    ./run.sh

### Running (Docker version)


To build and execute python via docker-compose, run:

    ./recompose.sh

### Serve

Run a server, for example the python SimpleHTTPServer via:

```
./serve.sh
```

Then visit http://localhost:3000/


### Docs

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html


### Sources

Project forked from https://github.com/jonromero/forex_algotrading


### Improvements

Currently it doesn't draws the direction yet - TODO: 'feature', not yet in the backlog)


### Screenshot

Images sometimes are better than many words :D

"recent" image

#### Sep '19

shrinkage around the 9k-12k area


![](http://mkvd.s3.amazonaws.com/tmp/chart-resistance-lines-september-2019.png)


#### Aug '19

![](https://github.com/makevoid/py-scikit-resistance-lines-btcusd-example/blob/master/tmp/2019-aug-15.png?raw=true)

#### Jun '19

![](http://makevoid.s3.amazonaws.com/share/chart-annotator-resistance-line-py-scikitlearn-clustering-example.png?raw=true)

#### First run (Apr '19)

![](https://github.com/makevoid/chart-annotator-resistance-lines/blob/master/tmp/resistance-lines-ml-classification-meanshift.png?raw=true)

If you want to use it "as it is" you will need to configure the AWS S3 credentials as that's the current way I'm saving/publishing the results. You want to comment all that code if you just to run it locally instead of automated inside docker.

You probably want also to tune `quantile` for the MeanShift clusterization to match the current price action. A range in between x and x should do that (The target is to find a `quantile` value that generates min 3-4 to max 8-10 clusters)

---

Enjoy!

@makevoid
