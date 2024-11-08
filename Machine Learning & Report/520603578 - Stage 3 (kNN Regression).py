import pandas as pd
import numpy
firstline = True

pd.set_option("display.width",400)
pd.set_option("display.max_columns",10)

dic = {}

#predict infant mortality rate from region, maternal mortality ratio, neonatal mortality rate, and births attended by personnel

with open("C:\\Users\\Kylie\\Downloads\\SDG_goal3_clean (1).csv") as file:
    for line in file:
        if firstline:
            firstline = False
        else:
            elements = line.split(",")
            country = elements[0]
            year = elements[1]
            region = elements[2]
            maternal = float(elements[3])
            skilledpersonnel = float(elements[4])
            infant = float(elements[5])
            neonatal = float(elements[11])

            temp = country + " " + year

            dic[temp] = [region, maternal, skilledpersonnel, neonatal, infant]

    df = pd.DataFrame(dic, index=["Region", "Maternal mortality ratio", "Births attended by skilled health personnel (%)", "Neonatal mortality rate", "Infant mortality rate"])
    df = df.transpose()
    df.columns = ["Region", "Maternal mortality ratio", "Births attended by skilled health personnel (%)", "Neonatal mortality rate", "Infant mortality rate"]

#splitting into training and test data, then splitting into x and y
training_data = df.sample(frac=0.8, random_state=24)
test_data = df.drop(training_data.index)

'''PRE-PROCESSING STAGE'''
#making into float and splitting into input & output
training_data = training_data.replace(["Africa","Americas","Asia","Europe","Oceania"],[int(1),int(2),int(3),int(4),int(5)])
test_data = test_data.replace(["Africa","Americas","Asia","Europe","Oceania"],[int(1),int(2),int(3),int(4),int(5)])

x_train = training_data.drop('Infant mortality rate', axis=1)
y_train = training_data['Infant mortality rate']

x_test = test_data.drop('Infant mortality rate', axis=1)
y_test = test_data['Infant mortality rate']

#scaling to 0-1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

x_train_scaled = scaler.fit_transform(x_train)
x_train_named = pd.DataFrame(x_train_scaled,columns=x_train.columns, index=x_train.index)
x_train = pd.DataFrame(x_train_scaled)

x_test_scaled = scaler.fit_transform(x_test)
x_test_named = pd.DataFrame(x_test_scaled,columns=x_test.columns,index=x_test.index)
x_test = pd.DataFrame(x_test_scaled)

#importing packages
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

'''PROCESSING'''
#checking for k
for K in range(17):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)

    model.fit(x_train, y_train)
    pred = model.predict(x_test) #make prediction
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    if K == 1:
        smallesterror = error
        ksmallesterror = str(K)
    elif smallesterror >= error:
        smallesterror = error
        ksmallesterror = str(K)
print("k value with the smallest RMSE:", str(ksmallesterror))
print("\n")

'''actually doing the regression'''
from sklearn.neighbors import KNeighborsRegressor

#predicting on the test set
knn_model = KNeighborsRegressor(n_neighbors=int(ksmallesterror))
knn_model.fit(x_train,y_train)
predict = knn_model.predict(x_test)

finalmodel = x_test_named.copy()
headers = ["Region", "MMR", "Births Attended by Skilled Health Personnel (%)", "Neonatal MR"]
finalmodel.columns = headers
finalmodel["Predicted IMR"] = predict
finalmodel["Actual IMR"] = y_test
finalmodel["Region"] = finalmodel["Region"].replace([float(0),float(0.25),float(0.5),float(0.75),float(1)],["Africa","Americas","Asia","Europe","Oceania"])

pred_actl = x_test_named.drop(["Region", "Maternal mortality ratio", "Births attended by skilled health personnel (%)", "Neonatal mortality rate"], axis=1)
pred_actl["Predicted infant mortality rate"] = predict
pred_actl["Actual infant mortality rate"] = y_test
print(finalmodel)
print("\n")

plt.scatter(pred_actl["Predicted infant mortality rate"],pred_actl["Actual infant mortality rate"])
a, b = numpy.polyfit(pred_actl["Predicted infant mortality rate"],pred_actl["Actual infant mortality rate"],1)
plt.plot(pred_actl["Predicted infant mortality rate"],a*pred_actl["Predicted infant mortality rate"]+b)
plt.show()

'''EVALUATION STAGE'''
#RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt
mse = mean_squared_error(pred_actl["Actual infant mortality rate"],pred_actl["Predicted infant mortality rate"])
rmse = sqrt(mse)
print("RMSE: "+ str(rmse))

#R2
from sklearn.metrics import r2_score
r2score = r2_score(pred_actl["Predicted infant mortality rate"],pred_actl["Actual infant mortality rate"])
print("R2 Score: "+ str(r2score))
