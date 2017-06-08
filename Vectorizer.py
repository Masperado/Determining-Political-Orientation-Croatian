import _pickle as cPickle
import csv
import numpy as np
from Croatian_stemmer import stem
from nltk.tokenize import word_tokenize
from sklearn.preprocessing import StandardScaler

def getVectorDict():

    vectors=dict()
    with open('Vector_dict.txt', 'rb') as dict_items_open:
        vectors = cPickle.load(dict_items_open)
    return vectors


def vectorize(input):
    vector = getVectorDict()
    result = np.zeros(300,)
    rijeci = word_tokenize(input)
    for i in range(0, len(rijeci)):
        word=stem(rijeci[i])
        if (word in vector):
            result = np.add(result, vector[word])
    #print(result)
    #X_scaler = StandardScaler()
    #result = X_scaler.fit_transform(result)
    #print(result)
    return result



if __name__ == "__main__":
    with open('SeminarVectored.csv', 'w', newline='') as stemFile:
        with open('SeminarStem.csv', newline='') as csvfile:
            writer=csv.writer(stemFile, delimiter=',')
            reader=csv.reader(csvfile, delimiter=',')
            vector=getVectorDict()
            for row in reader:
                result=np.zeros(300)
                words=row[0].split(' ')
                for i in range (0,len(words)):
                    if (words[i] in vector):
                        result=np.add(result,vector[words[i]])
                result=result.astype('|S10')
                print(result)
                score=row[1]
                writer.writerow([b' '.join(result), score])