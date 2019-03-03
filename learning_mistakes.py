import pandas as pd
import numpy as np
import warnings

from sklearn.preprocessing import Imputer
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import roc_curve
from sklearn.metrics import make_scorer
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

def getSplit(X_imp, y_imp):

    X_train, X_test, y_train, y_test = train_test_split(X_imp, y_imp , test_size=0.30)

    clf = RandomForestClassifier(n_estimators=100, random_state=713)
    clf.fit(X_train, y_train)

    y_test = np.asarray(y_test)
    mistakes = []
    mistakes = np.where(y_test != clf.predict(X_test))
    corrects = np.where(y_test == clf.predict(X_test))

    #get list of indicies in x
    mistake_list = []
    for item in mistakes:
        mistake_list.extend(item)

    correct_list = []
    for item in corrects:
        correct_list.extend(item)

    #print(mistake_list)

    X_list = X_test.index.tolist()

    #get actual mistake indicies in dataset
    mistake_indexes = []
    for i in mistake_list:
        mistake_indexes.append(X_list[i])

    correct_indexes = []
    for i in correct_list:
        correct_indexes.append(X_list[i])

    mistake_indexes.sort()
    correct_indexes.sort()

    return mistake_indexes, correct_indexes



#dataset = pd.read_csv("./Data/DATASET_cckres.csv").drop('Group', axis=1)
dataset = pd.read_csv("./Data/DATASET_gigafida.csv").drop('Group', axis=1)
#dataset['Avg N3'] = dataset.apply(lambda row: (row['N1']+row['N2']+row['N3']) / 3, axis=1)
#dataset['Diff N12'] = dataset.apply(lambda row: (row['N2']-row['N1']), axis=1)
#dataset['Diff N13'] = dataset.apply(lambda row: (row['N3']-row['N1']), axis=1)


#print(dataset.shape)

#impute missing values
tmp = dataset[['Type','CosDist Sim']]
tmp = tmp.apply(pd.to_numeric, errors='coerce')
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(tmp)
tmp = imp.transform(tmp)
dataset_imp = dataset.drop('CosDist Sim', axis=1)
dataset_imp['CosDist Sim'] = tmp[:,1]


X_imp = dataset_imp.drop('Type', axis=1)
y_imp = dataset_imp['Type']




#read dataset
examples = []
with open("./Data/DATASET_gigafida.csv", encoding="utf8") as ins:
    for line in ins:
        examples.append(line)

#get rid of first line in csv
examples.pop(0)

open('example_mistakes_concat.csv', 'w').close()
open('example_corrects_concat.csv', 'w').close()
for i in range(10):

    mistake_indexes, correct_indexes = getSplit(X_imp, y_imp)
    
    with open('example_mistakes_concat.csv', 'a+', encoding="utf8") as f:
        f.write("Group,Mag Group,Mag Avg,CosDist Sum,DotProd Sum,CosDist Sim,N1,N2,N3,Type\n")
        for i in mistake_indexes:
            line = examples[i]
            f.write("%s" % line)
    
    with open('example_corrects_concat.csv', 'a+', encoding="utf8") as f:
        f.write("Group,Mag Group,Mag Avg,CosDist Sum,DotProd Sum,CosDist Sim,N1,N2,N3,Type\n")
        for i in correct_indexes:
            line = examples[i]
            f.write("%s" % line)


'''
#print mistakes
for i in mistake_indexes:
    line = examples[i]
    attributes = line.split(",")
    print(attributes[0])
    
#print corrects
for i in correct_indexes:
    line = examples[i]
    attributes = line.split(",")
    print(attributes[0])
'''
 

'''
with open('example_mistakes.csv', 'w', encoding="utf8") as f:
    f.write("Group,Mag Group,Mag Avg,CosDist Sum,DotProd Sum,CosDist Sim,N1,N2,N3,Type\n")
    for i in mistake_indexes:
        line = examples[i]
        f.write("%s" % line)

with open('example_corrects.csv', 'w', encoding="utf8") as f:
    f.write("Group,Mag Group,Mag Avg,CosDist Sum,DotProd Sum,CosDist Sim,N1,N2,N3,Type\n")
    for i in correct_indexes:
        line = examples[i]
        f.write("%s" % line)


print ("napacnih:", len(mistake_indexes))
print ("pravilnih:", len(correct_indexes))

'''