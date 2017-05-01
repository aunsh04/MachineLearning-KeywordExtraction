import pandas as pd
import numpy as np
from scipy import sparse
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.feature_selection import VarianceThreshold


#from subprocess import check_output
#print(check_output(["ls", "2012-and-2016-presidential-elections"]).decode("utf8"))

votes = pd.read_csv('Workbook1.csv')
                                                                    

votesp = votes [['tf-idf','length','position','present_early','present_end','keyword']]
votesp.dropna(inplace=True)
Xp = np.array(votesp.drop(['keyword'],1))
Xp = preprocessing.scale(Xp)
yp = np.array(votesp['keyword'])
Xp_train, Xp_test , yp_train , yp_test = cross_validation.train_test_split(Xp,yp, test_size=0.2)
#print (len(Xp),len(yp))
#clfp = LinearRegression()
clfp = svm.SVC(kernel='poly')
#train
clfp.fit(Xp_train,yp_train)
#test
accuracyp = clfp.score(Xp_test,yp_test)
print (accuracyp)

#####################################################

