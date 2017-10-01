# Kernel SVM

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import sklearn
from itertools import product


# importing the dataset
dataset = pd.read_csv('./Training/csv/output.csv')
X = dataset.iloc[:,[0,4]].values
y = dataset.iloc[:, 5].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting the Classifier to the Training Set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=20, metric="minkowski", p=2)
classifier.fit(X_train, y_train)

# Predicting the Test set Results
y_pred = classifier.predict(X_test)

# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
np.savetxt('./Training/csv/confusion_matrix.out', cm, delimiter=',', fmt='%.0f')

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv = 10)
print('mean accuracy:', accuracies.mean())
print('accuracy standard deviation: ', accuracies.std())

with open('./Training/csv/knn_classifier.pickle', 'wb') as f:
    pickle.dump(classifier, f, pickle.HIGHEST_PROTOCOL)

# from sklearn.model_selection import GridSearchCV
# parameters

# Plotting decision regions
x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

tt = 'KNN (k=20) \n'

Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, 1000, alpha=0.3, cmap='viridis')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, alpha=1)
plt.suptitle(tt)
plt.set_cmap('viridis')

plt.show()
