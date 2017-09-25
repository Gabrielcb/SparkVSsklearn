from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel

from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
from pyspark.mllib.regression import LabeledPoint
import pyspark
import numpy as np
import random
from time import time

# $example on$
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import LogisticRegressionModel
# $example off$
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, RegressionEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVC
from pyspark.ml.regression import LinearRegression

import CarDatasetProcessing
import LetterDatasetProcessing



def LogReg(spark, data, FileResults):


	if(data == 'Letter'):
		LetterDatasetProcessing.getDataLetter('spark')
		training = spark.read.format("libsvm").load("TrainSetLetter.txt")
		test = spark.read.format("libsvm").load("TestSetLetter.txt")
	else:
		CarDatasetProcessing.getDataCar('spark')
		training = spark.read.format("libsvm").load("TrainSetCar.txt")
		test = spark.read.format("libsvm").load("TestSetCar.txt")



	lr = LogisticRegression()


    # Fit the model
	to = time()
	lrModel = lr.fit(training)

	l = lrModel.transform(test)
	tf = time()

	dt = tf - to
	predictionAndLabels = l.select("prediction", "label")
	
	#predictions = lrModel.coefficientMatrix
	evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
	FileResults.write("Logistic Regression:\n")
	FileResults.write("Accuracy: %s\n" % str(evaluator.evaluate(predictionAndLabels)))
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")
	print("Accuracy LogReg:" + str(evaluator.evaluate(predictionAndLabels)))

	
	#print predictionAndLabels

def SVM(spark, FileResults):

	
	CarDatasetProcessing.getDataCar('spark', True)
	training = spark.read.format("libsvm").load("TrainSetCar.txt")
	test = spark.read.format("libsvm").load("TestSetCar.txt")


	lsvc = LinearSVC()

    # Fit the model
	to = time()
	lsvcModel = lsvc.fit(training)

	l = lsvcModel.transform(test)
	tf = time()

	dt = tf - to

	predictionAndLabels = l.select("prediction", "label")
	
	#predictions = lrModel.coefficientMatrix
	evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
	FileResults.write("SVM:\n")
	FileResults.write("Accuracy: %s\n" % str(evaluator.evaluate(predictionAndLabels)))
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")
	print("Accuracy SVM:" + str(evaluator.evaluate(predictionAndLabels)))

	
	#print predictionAndLabels


def LinReg(spark, data, FileResults):

	if(data == 'Letter'):
		LetterDatasetProcessing.getDataLetter('spark')
		training = spark.read.format("libsvm").load("TrainSetLetter.txt")
		test = spark.read.format("libsvm").load("TestSetLetter.txt")
	else:
		CarDatasetProcessing.getDataCar('spark')
		training = spark.read.format("libsvm").load("TrainSetCar.txt")
		test = spark.read.format("libsvm").load("TestSetCar.txt")


	lreg = LinearRegression()

	# Fit the model
	to = time()
	lregModel = lreg.fit(training)

	l = lregModel.transform(test)
	tf = time()

	dt = tf - to
	predictionAndLabels = l.select("prediction", "label")
	

	#predictions = lrModel.coefficientMatrix
	evaluator = RegressionEvaluator(metricName="mse")
	FileResults.write("Linear Regression:\n")
	FileResults.write("MSE: %s\n" % str(evaluator.evaluate(predictionAndLabels)))
	FileResults.write("Time taken to train and to test: %f seconds\n" % dt)
	FileResults.write("\n")
	print("MSE:" + str(evaluator.evaluate(predictionAndLabels)))

	
	#print predictionAndLabels



def main():
	FileResults = open("ResultsSpark.txt", 'w')
	sc = pyspark.SparkContext()
	spark = SparkSession\
        .builder\
        .appName("MC855")\
        .getOrCreate()

    
	# ---- it is gonna be in the final version - Car dataset ----
	FileResults.write("Results for Car evaluation dataset:\n")
	LogReg(spark, 'Car', FileResults)
	SVM(spark, FileResults)
	LinReg(spark, 'Car', FileResults)
	# ------------------------------------------

	FileResults.write('\n')
    # ---- it is gonna be in the final version ----
	FileResults.write("Results for Letter Recognition dataset:\n")
	LogReg(spark, 'Letter', FileResults)
	LinReg(spark, 'Letter', FileResults)
	# ------------------------------------------
	
if __name__ == '__main__':
	main()