import pandas as pd
import numpy as np
import warnings
import sys

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

def specificity(y_true, y_pred):
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    spec = 1 - fpr
    #spec = 1 -(1-tpr)
    return spec[1]

def printScores(scores):
    print("accuracy:", (sum(scores['test_accuracy'])/len(scores['test_accuracy'])).round(decimals=3))
    #print("precision:", (sum(scores['test_precision'])/len(scores['test_precision'])).round(decimals=3))
    print("sensitivity:", (sum(scores['test_recall'])/len(scores['test_recall'])).round(decimals=3))
    print("specificity:", (sum(scores['test_specificity'])/len(scores['test_specificity'])).round(decimals=3))
    print("auc:", (sum(scores['test_roc_auc'])/len(scores['test_roc_auc'])).round(decimals=3))


if len(sys.argv) < 2:
    print("missing corpus argument")
    sys.exit(1)

corpus = sys.argv[1]

dataset = pd.read_csv("./datasets/DATASET_"+ corpus +".csv").drop('Group', axis=1)
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


X = dataset.drop('Type', axis=1)
y = dataset['Type']


X_imp = dataset_imp.drop('Type', axis=1)
y_imp = dataset_imp['Type']


#X_imp = X_imp.drop('N1', axis=1)
#X_imp = X_imp.drop('N2', axis=1)
#X_imp = X_imp.drop('N3', axis=1)
#X_imp = X_imp.drop('CosDist Sim', axis=1)



#w['Similar Cos Dist'] = w['Similar Cos Dist'].map({'None': None, })

custom_scorer = make_scorer(specificity)
scoring = {'accuracy': 'accuracy',
           'precision': 'precision',
           'recall': 'recall',
           'specificity': custom_scorer,
           'roc_auc': 'roc_auc'}

#C_svc = SVC(kernel='rbf')
#C_svc = SVC(kernel='sigmoid')

warnings.filterwarnings("ignore", category=DeprecationWarning)

C_svc = SVC(kernel='rbf', gamma='auto')
scores_svc = cross_validate(C_svc, X_imp, y_imp, scoring=scoring, cv=10)
print("SVM:")
printScores(scores_svc)
print()


C_rf = RandomForestClassifier(n_estimators=100, random_state=713)
scores_rf = cross_validate(C_rf, X_imp, y_imp, scoring=scoring, cv=10)
print("Random Forest:")
printScores(scores_rf)
print()


#scores_lr = LogisticRegressionCV(cv=10, scoring=scoring, random_state=713).fit(X_imp, y_imp)
C_lr = LogisticRegression()
scores_lr = cross_validate(C_lr, X_imp, y_imp, scoring=scoring, cv=10)
print("Logistic Regression:")
printScores(scores_lr)

#lr feature importance
lr = LogisticRegressionCV(cv=10, scoring='accuracy')
coef = lr.fit(X_imp, y_imp)
print()
print("Logistic Regression Ranking:")
print(coef.coef_.round(decimals=3))
#print(lr.score(X_imp, y_imp))


#forest feature importance
forest = ExtraTreesClassifier(n_estimators=100, random_state=713)
forest.fit(X_imp, y_imp)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
indices = np.argsort(importances)[::-1]
print()
print("Random Forest Ranking:")
for f in range(X.shape[1]):
    print("%d - (%f)" % (indices[f], importances[indices[f]].round(decimals=3)))
