#### Prediction based on previous 15 days and 5 international market ####

from datafetch2 import *
import numpy

from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

def create_dataVector(stock_df):
	""" from aailable data create dataVector using Return values, past 15 days values and 
		international market"""

	stock_df=stock_df['Return'].values	
	global cnx,bse,hang_seng,ftse,axjo
	cnx=cnx_nifty['Return'].values
	bse=bse['Return'].values
	hang_seng=hang_seng['Return'].values
	ftse=ftse['Return'].values
	axjo=axjo['Return'].values

	data=[]
	for i in range(0,len(stock_df)):
	    if i>=15 :
	        l=stock_df[i-15:i].tolist()
	        l.append(cnx[i-1])
	        l.append(bse[i-1])
	        l.append(hang_seng[i-1])
	        l.append(ftse[i-1])
	        l.append(axjo[i-1])    
	        data.append(l)
	    else:
	        data.append([0])
	return data

def get_train_test(stock_df):
	bon=len(stock_df)*95/100
	bon=round(bon)
	data=create_dataVector(stock_df)
	features_train=numpy.array(data[1000:bon])
	labels_train=numpy.array(stock_df["Profit"][1000:bon])
	features_test=numpy.array(data[bon:])
	labels_test=numpy.array(stock_df["Profit"][bon:])
	return features_train,labels_train,features_test,labels_test

def predict_stock(stock_df):	
	X,Y,X_test,Y_test=get_train_test(stock_df)
	clfs=[
			("NB",GaussianNB()),
			("SVM",svm.SVC()),
			("Decision tree",tree.DecisionTreeClassifier()),
			("K Nearest Neighbor",KNeighborsClassifier(n_neighbors=100)),
			("RandomForest",RandomForestClassifier(n_estimators=16)),
			("AdaBoost",AdaBoostClassifier(n_estimators=100))
		]
	for i in clfs:
		i[1].fit(X,Y)
		print(i[0],i[1].score(X_test,Y_test))


### stock could be : tata,relcapital,lichfl #####
predict_stock(tata)

