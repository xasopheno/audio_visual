# Kernel SVM

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# importing the dataset
dataframe = pd.read_csv('./Training/csv/output.csv', header=None)
dataset = dataframe.values
X = dataset[:, 0:9]
y = dataset[:, 10]
print (X[1255])
print (y[1255])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

# Fitting the Classifier to the Training Set
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

# classifier = svm.SVC(decision_function_shape='ovo')
# classifier = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)
# classifier = KNeighborsClassifier(n_neighbors=20, metric="minkowski", p=2)
classifier = RandomForestClassifier(n_estimators=3,
                                    criterion='entropy',
                                    max_features='auto',
                                    # n_jobs=-1,
                                    oob_score=True)
# classifier = AdaBoostClassifier(n_estimators=100)
# classifier = GaussianNB()
# classifier = LogisticRegression(random_state = 0)

print('Fitting Classifier')
classifier.fit(X_train, y_train)

print('Predicting the Test set Results')
y_pred = classifier.predict(X_test)

print('Making the confusion matrix')
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
np.savetxt('./Training/csv/confusion_matrix.out', cm, delimiter=',', fmt='%.0f')

print('Performing cross validation')
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X=X_test, y=y_test, cv=3)
print('mean accuracy:', accuracies.mean())
print('accuracy standard deviation: ', accuracies.std())

# print('Performing grid search')
# from sklearn.model_selection import GridSearchCV
# parameters = [
#     {'n_estimators':[32],
#      'criterion':['entropy'],
#      'max_features':['auto'],
#      },
#     ]
#
# grid_search = GridSearchCV(estimator=classifier,
#                            param_grid=parameters,
#                            scoring='accuracy',
#                            cv=10,
#                            n_jobs=-1
#                            )
#
# grid_search = grid_search.fit(X_train, y_train)
# best_accuracy = grid_search.best_score_
# best_parameters = grid_search.best_params_
# print ('best accuracy: ', best_accuracy)
# print ('best_parameters: ', best_parameters)

print ('Pickling')
with open('./Training/csv/knn_classifier.pickle', 'wb') as f:
    pickle.dump(classifier, f)


# print (classifier.predict(X[10000]))

# from sklearn.model_selection import GridSearchCV
# parameters

# Plotting decision regions
# x_min, x_max = X_train[:, [0,1,2,3,4]].min() - .5, X_train[:, [0,1,2,3,4]].max() + .5
# print (x_min, x_max)
# y_min, y_max = y_train[0].min() - .5, y_train[0].max() + .5
# print (y_min, y_max)
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
#                      np.arange(y_min, y_max, 0.1))
#
# tt = 'KNN (k=20) \n'
#
# Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# #
# plt.contourf(xx, yy, Z, 36, alpha=0.3, cmap='viridis')
# plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, alpha=1)
# plt.suptitle(tt)
# plt.set_cmap('viridis')
#
# plt.show()
