import pandas as pd

import numpy as np
from scipy import sparse
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
from sklearn.feature_selection import VarianceThreshold

style.use('ggplot')

#from subprocess import check_output
#print(check_output(["ls", "2012-and-2016-presidential-elections"]).decode("utf8"))

votes = pd.read_csv('Workbook1.csv')


def CorrelationCoeff(X,Y):
    mu_x = np.mean(X)
    mu_y = np.mean(Y)
    N = len(X)
    r = (sum([ X[i]*Y[i] for i in range(N) ]) - N*mu_x*mu_y) \
        / (math.sqrt( sum(X**2)-N*(mu_x**2) )) \
        / (math.sqrt( sum(Y**2)-N*(mu_y**2) ))
    return r



votesp = votes [['tf-idf','length','position','present_early','present_end','keyword']]
votesp.dropna(inplace=True)

plt.scatter(votesp['present_early'], votesp['keyword'], s=8, c='g', label='present early vs is a keyword')
plt.legend()



plt.show()
