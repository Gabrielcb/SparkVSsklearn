
def preprossingData(InputData, binary):


	buying_maint = ['low', 'med', 'high', 'vhigh']
	doors = ['2','3','4', '5more']
	persons = ['2','4', 'more']
	lug_boot = ['small', 'med', 'big']
	safety = ['low', 'med', 'high']  

	target = ['unacc', 'acc', 'good', 'vgood']


	data = InputData.split(',')
	data[6] = data[6][:-1]


	data[0] = buying_maint.index(data[0])*10
	data[1] = buying_maint.index(data[1])*10
	data[2] = doors.index(data[2]) + 2
	data[3] = persons.index(data[3]) + 2
	data[4] = lug_boot.index(data[4])*2
	data[5] = safety.index(data[5])*10
	data[6] = target.index(data[6])

	if(binary == True):
		if(data[6] <= 1):
			data[6] = 0
		else:
			data[6] = 1
	


	return data

def getDataCar(environment, binary=False):



	dataset = open('car.data.txt', 'r')
	train = open('TrainSetCar.txt', 'w') 
	test = open('TestSetCar.txt', 'w') 

	dataset = dataset.readlines()
	dataset_precessed = [preprossingData(line, binary) for line in dataset]


	if(environment == 'spark'):
		for i in range(len(dataset_precessed)/5, len(dataset_precessed)):
			train.write(str(dataset_precessed[i][6]) + ' ' + '1:' + str(dataset_precessed[i][0]) + ' ' + '2:' + str(dataset_precessed[i][1]) + ' ' + '3:' + str(dataset_precessed[i][2])
			+ ' ' + '4:' + str(dataset_precessed[i][3]) + ' ' + '5:' + str(dataset_precessed[i][4]) + ' ' + '6:' + str(dataset_precessed[i][5]) + '\n')

		for i in range(len(dataset_precessed)/5):
			test.write(str(dataset_precessed[i][6]) + ' ' + '1:' + str(dataset_precessed[i][0]) + ' ' + '2:' + str(dataset_precessed[i][1]) + ' ' + '3:' + str(dataset_precessed[i][2])
			+ ' ' + '4:' + str(dataset_precessed[i][3]) + ' ' + '5:' + str(dataset_precessed[i][4]) + ' ' + '6:' + str(dataset_precessed[i][5]) + '\n')
	elif(environment == 'sklearn'):
		return dataset_precessed












