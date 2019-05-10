#// skearn generic example


#// ....
samples = digits.images.shape[0]
X = digits.images.reshape([samples,-1])

#// ML set
X_train, X_test, y_train, y_test  = trainTestSplit.(X, digits.target, test_size: 0.2, random_state: Time.now.to_i)

#// Initialize ML engine with parameters gamma=0.001
clf = svm.SVC.new( gamma: 0.001 )

#// FIT (run)
clf.fit.(X_train, y_train)

#// ETC
#// #//Score our fit using the test data
#//classification_score = clf.score(X_test,y_test)
#//puts "Prediction score for our SVM #{(classification_score*100).round(2)}%"
#
#// #//Do a prediction for one sample
#//puts clf.predict([X_test[0]])
#// #//Reshape back to 2 dimmensions and print
#//puts X_test[0].reshape(8,8)
