
def preprossingData(InputData):

	data = InputData.split(',')
	data[0] = ord(data[0]) - 64
	data = [float(data[i]) for i in range(len(data))]
	return data

def getDataLetter(environment):



	dataset = open('letter-recognition.data.txt', 'r')
	train = open('TrainSetLetter.txt', 'w') 
	test = open('TestSetLetter.txt', 'w') 

	dataset = dataset.readlines()
	dataset_precessed = [preprossingData(line) for line in dataset]

	if(environment == 'spark'):
		for i in range(len(dataset_precessed)/5, len(dataset_precessed)):
			train.write(str(dataset_precessed[i][0]) + ' ' + '1:' + str(dataset_precessed[i][1]) + ' ' + '2:' + str(dataset_precessed[i][2]) + ' ' + '3:' + str(dataset_precessed[i][3])
			+ ' ' + '4:' + str(dataset_precessed[i][4]) + ' ' + '5:' + str(dataset_precessed[i][5]) + ' ' + '6:' + str(dataset_precessed[i][6]) + ' ' + '7:' + str(dataset_precessed[i][7])
			+ ' ' + '8:' + str(dataset_precessed[i][8]) + ' ' + '9:' + str(dataset_precessed[i][9]) + ' ' + '10:' + str(dataset_precessed[i][10]) + ' ' + '11:' + str(dataset_precessed[i][11])
			+ ' ' + '12:' + str(dataset_precessed[i][12]) + ' ' + '13:' + str(dataset_precessed[i][6]) + ' ' + '14:' + str(dataset_precessed[i][14]) + ' ' + '15:' + str(dataset_precessed[i][15])
			+ ' ' + '16:' + str(dataset_precessed[i][16]) + '\n')

		for i in range(len(dataset_precessed)/5):
			test.write(str(dataset_precessed[i][0]) + ' ' + '1:' + str(dataset_precessed[i][1]) + ' ' + '2:' + str(dataset_precessed[i][2]) + ' ' + '3:' + str(dataset_precessed[i][3])
			+ ' ' + '4:' + str(dataset_precessed[i][4]) + ' ' + '5:' + str(dataset_precessed[i][5]) + ' ' + '6:' + str(dataset_precessed[i][6]) + ' ' + '7:' + str(dataset_precessed[i][7])
			+ ' ' + '8:' + str(dataset_precessed[i][8]) + ' ' + '9:' + str(dataset_precessed[i][9]) + ' ' + '10:' + str(dataset_precessed[i][10]) + ' ' + '11:' + str(dataset_precessed[i][11])
			+ ' ' + '12:' + str(dataset_precessed[i][12]) + ' ' + '13:' + str(dataset_precessed[i][6]) + ' ' + '14:' + str(dataset_precessed[i][14]) + ' ' + '15:' + str(dataset_precessed[i][15])
			+ ' ' + '16:' + str(dataset_precessed[i][16]) + '\n')
	elif(environment == 'sklearn'):
		return dataset_precessed





















