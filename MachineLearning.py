#!/usr/bin/env python -W ignore::DeprecationWarning
import _pickle as cPickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
import csv
import numpy as np
from Vectorizer import vectorize
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

with open ('SeminarVectored.csv') as input:
    reader=csv.reader(input, delimiter=',')
    a=np.zeros(shape=(1999,300))
    b=np.zeros(shape=(1999,))
    i=0
    for row in reader:
        vector = np.asarray(row[0][1:].split(' '))
        vector = vector.astype(float)
        a[i] = vector
        b[i] = row[1]
        i=i+1

    b=b.astype(int)
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.2)

    #X_scaler = StandardScaler()
    #X_train = X_scaler.fit_transform(X_train)
    #X_test = X_scaler.fit_transform(X_test)

    '''
    ml=SVC()
    param_grid = [
        {'C': [2**i for i in range(-15,7)], 'kernel': ['linear']},
        {'C': [2**i for i in range(-15,7)], 'gamma': [10**i for i in range(-9,0)], 'kernel': ['rbf']}
        ]
    svm_best = GridSearchCV(ml, param_grid, verbose=3, n_jobs=8)

    '''
    ml=SVC(kernel='rbf', C=2, gamma=0.01)
    ml=ml.fit(X_train, y_train)


    with open('model.txt', 'wb') as model_save:
       cPickle.dump(ml, model_save)

    '''
    ml=SVC()
    with open('modelR2|0.01.txt','rb') as model1:
        ml=cPickle.load(model1)
   '''
    print(ml)
    print(ml.score(X_train,y_train))
    i=0
    for x in X_test:
        orijen=ml.predict(x)
        if (orijen==2):
            i=i+1
    print(i)
    print(ml.score(X_test,y_test))