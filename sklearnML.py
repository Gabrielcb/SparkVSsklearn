import sklearn
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn import svm
import CarDatasetProcessing
import LetterDatasetProcessing
import random
from time import time



def LogReg(data, FileResults):

	if(data == 'Letter'):
		dataset = LetterDatasetProcessing.getDataLetter('sklearn')
		random.shuffle(dataset)

		part = len(dataset)

		DataTrain = dataset[part/5:]
		DataTest = dataset[:part/5]


		X_train = [x[1:] for x in DataTrain]
		Y_train = [x[0] for x in DataTrain]

		X_test = [x[1:] for x in DataTest]
		Y_test = [x[0] for x in DataTest]

	else:
		dataset = CarDatasetProcessing.getDataCar('sklearn')
		random.shuffle(dataset)

		part = len(dataset)

		DataTrain = dataset[part/5:]
		DataTest = dataset[:part/5]


		X_train = [x[:6] for x in DataTrain]
		Y_train = [x[6] for x in DataTrain]

		X_test = [x[:6] for x in DataTest]
		Y_test = [x[6] for x in DataTest]


	logreg = linear_model.LogisticRegression()

	to = time()
	logreg.fit(X_train, Y_train)
	pred = logreg.predict(X_test)
	tf = time()
	dt = tf - to

	acc = accuracy_score(Y_test, pred)
	print acc

	FileResults.write("Logistic Regression:\n")
	FileResults.write("Accuracy: %f\n" % acc)
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")


def LinReg(data, FileResults):
	if(data == 'Letter'):
		dataset = LetterDatasetProcessing.getDataLetter('sklearn')
		random.shuffle(dataset)

		part = len(dataset)

		DataTrain = dataset[part/5:]
		DataTest = dataset[:part/5]


		X_train = [x[1:] for x in DataTrain]
		Y_train = [x[0] for x in DataTrain]

		X_test = [x[1:] for x in DataTest]
		Y_test = [x[0] for x in DataTest]

	else:
		dataset = CarDatasetProcessing.getDataCar('sklearn')
		random.shuffle(dataset)

		part = len(dataset)

		DataTrain = dataset[part/5:]
		DataTest = dataset[:part/5]


		X_train = [x[:6] for x in DataTrain]
		Y_train = [x[6] for x in DataTrain]

		X_test = [x[:6] for x in DataTest]
		Y_test = [x[6] for x in DataTest]


	regr = linear_model.LinearRegression()
	to = time()
	regr.fit(X_train, Y_train)

	pred = regr.predict(X_test)
	tf = time()
	dt = tf - to
	acc = mean_squared_error(Y_test, pred)
	print mean_squared_error(Y_test, pred)

	FileResults.write("Linear Regression:\n")
	FileResults.write("MSE: %f\n" % acc)
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")


def SVM(FileResults):

	dataset = CarDatasetProcessing.getDataCar('sklearn', True)
	random.shuffle(dataset)

	part = len(dataset)

	DataTrain = dataset[part/5:]
	DataTest = dataset[:part/5]


	X_train = [x[:6] for x in DataTrain]
	Y_train = [x[6] for x in DataTrain]

	X_test = [x[:6] for x in DataTest]
	Y_test = [x[6] for x in DataTest]

	clf = svm.SVC(kernel='linear')
	to = time()
	clf.fit(X_train, Y_train) 

	pred = clf.predict(X_test)
	tf = time()
	dt = tf - to

	acc = accuracy_score(Y_test, pred)
	print acc

	FileResults.write("SVM:\n")
	FileResults.write("Accuracy: %f\n" % acc)
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")


def main():

	FileResults = open("ResultsSklearn.txt", "w")

	FileResults.write("Results for Car evaluation dataset:\n")
	LogReg('Car', FileResults)
	print "Linear Regression:"
	LinReg('Car', FileResults)
	print "SVM:"
	SVM(FileResults)

	FileResults.write("\n")
	FileResults.write("Results for Letter Recognition dataset:\n")
	print "Logistic Regression:"
	LogReg('Letter', FileResults)
	print "Linear Regression:"
	LinReg('Letter', FileResults)
	



if __name__ == '__main__':
	main()