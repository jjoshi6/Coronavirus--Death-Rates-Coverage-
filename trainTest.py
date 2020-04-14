import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#1 is for a shelter in place law
#2 is for don't get out of your house law

#Run these 5 csv files for linear regression testing

France_CSV = 'France.csv'
Germany_CSV = 'Germany.csv'
USA_CSV = 'USA.csv'
Italy_CSV = 'Italy.csv'
Spain_CSV = 'Spain.csv'
Italy_Corona_Virus_Test = 'ItalyCoronaVirusTest.csv'
US_Corona_Virus_Test = 'USACoronaVirusTest.csv'

x = []
y = []

count = 0
newDeathPercentage = 0

#run whichever file you need to run here

with open(Italy_Corona_Virus_Test,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(count != 0 and row != []):
            x.append(count)
            newDeathPercentage = int(row[1])
            y.append(newDeathPercentage)
        count = count + 1

#reversing the features because latest data should appear last

y.reverse()




regression_model = LinearRegression()

trainingSetX = []
trainingSetY = []
testSetX = []

trainingLength = int(len(x))



for i in range(trainingLength):
    trainingSetX.append([x[i]])
trainingSetX = np.asarray(trainingSetX)


for i in range(trainingLength):
    trainingSetY.append([y[i]])
trainingSetY = np.asarray(trainingSetY)

for i in range(len(x) - trainingLength):
    testSetX.append([x[trainingLength + i]])
testSetX = np.asarray(testSetX)

regression_model.fit(trainingSetX, trainingSetY)

y_predicted = regression_model.predict(trainingSetX)



# model evaluation
rmse = mean_squared_error(trainingSetY, y_predicted)
r2 = r2_score(trainingSetY, y_predicted)
print("rmse",rmse)
print("r2", r2)

# data points
plt.scatter(trainingSetX, trainingSetY, s=10)
plt.xlabel('Time')
plt.ylabel('Total Test Kits')


# predicted values
plt.title('Predicting Test Kits')
plt.plot(trainingSetX, y_predicted, color='r')
plt.show()




