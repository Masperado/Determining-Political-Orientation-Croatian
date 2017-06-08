import csv
from nltk.tokenize import word_tokenize
from Croatian_stemmer import stem,korjenuj

with open('vector.txt') as vectors:
    with open('vectorstem.txt','w') as vectorsStem:
        for word in vectors:
            key=stem(word.split(" ")[0][:-2])
            values=word.split(" ")[1:]
            toWrite=key +" " + " ".join(values)
            vectorsStem.write(toWrite)

with open('SeminarStem.csv', 'w', newline='') as stemFile:
    with open('Seminar.csv', newline='') as csvfile:
        writer=csv.writer(stemFile, delimiter=',')
        reader=csv.reader(csvfile, delimiter=',')
        for row in reader:
            words=word_tokenize(row[0])
            stemmedWords=[]
            for i in range(0,len(words)):
                result=stem(words[i])
                if (len(result)>1):
                    stemmedWords.append(stem(words[i]))
            score=row[1]
            writer.writerow([" ".join(stemmedWords), score])