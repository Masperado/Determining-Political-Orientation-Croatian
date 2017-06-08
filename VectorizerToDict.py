import numpy as np
import _pickle as cPickle

i=0
vectorsDict=dict()
with open('vectorstem.txt') as vectors:
        for word in vectors:
            key=word.split(" ")[0]
            values=np.asarray(word.split(" ")[1:301])
            floatValues=values.astype(float)
            vectorsDict[key]=floatValues
            i=i+1
            print(i)
with open('Vector_dict.txt','wb') as dict_save:
    cPickle.dump(vectorsDict, dict_save)