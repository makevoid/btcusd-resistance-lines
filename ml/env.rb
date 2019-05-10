# env
require 'rjs'

# pycall env
require 'pycall/import'
include PyCall::Import

pyfrom :sklearn, import: :datasets
pyfrom :sklearn, import: :svm
pyfrom :'sklearn.model_selection', import: :train_test_split

# alias :trainTestSplit :train_test_split
trainTestSplit = train_test_split

clf.fit = -> (trainingSetA, trainingSetB) { clf.fit( trainingSetA, trainingSetB ) }
