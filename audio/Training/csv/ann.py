import numpy
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from keras.callbacks import TensorBoard
from datetime import datetime
from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

now = datetime.now()
logdir = "logs/.../" + now.strftime("%Y%m%d-%H%M%S") + "/"

tensorboard = TensorBoard(log_dir=logdir, histogram_freq=0,
                          write_graph=True, write_images=False)

# importing the dataset
dataframe = pd.read_csv('./Training/csv/output.csv', header=None)
dataset = dataframe.values
X = dataset[1:, 0:10]
y = dataset[1:, 10]
# onehotencoder = OneHotEncoder(categorical_features = [1])
# X = onehotencoder.fit_transform(X).toarray()
# X = X[:, 0:]
# print X[10]
# X = X[1:, 0:10]
# print X.shape

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

print (X[10])
print (X.shape)
print (dummy_y[20])
print (dummy_y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size = 0.2, random_state = 0)

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras import optimizers
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
import keras.backend as K

# Initialising the ANN
def model():
    classifier = Sequential()

    # Adding the input layer and the first hidden layer
    # classifier.add(Dropout(0.2, input_shape=(10,)))
    classifier.add(Dense(input_dim=(10), output_dim = 10, init = 'uniform', activation = 'relu'))
    # classifier.add(BatchNormalization())
    # classifier.add(Dropout(0.2))
    # classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))
    # classifier.add(Dropout(0.2))

    classifier.add(Dense(512, init = 'uniform', activation = 'tanh'))
    classifier.add(Dense(512, init = 'uniform', activation = 'tanh'))
    classifier.add(Dense(512, init = 'uniform', activation = 'tanh'))
    # classifier.add(Dense(24, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(24, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(1024, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(1024, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'relu'))
    # classifier.add(Dense(output_dim = 16, init = 'uniform', activation = 'relu'))
    # classifier.add(Dropout(0.2))

    classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'softmax'))

    sdg = optimizers.SGD(
        lr=0.001,
        momentum=0.01,
        decay=0,
        nesterov=True
    )

    adam = optimizers.Adam(
        lr=0.0007,
        # beta_1=0.9,
        # beta_2=0.999,
        # epsilon=1e-08,
        # schedule_decay=0.004
    )
    # sgd = optimizers.SGD(lr=0.00001)

    classifier.compile(optimizer='adam',
                       loss = 'categorical_crossentropy',
                       metrics = ['accuracy'],
                       )

    return classifier



checkpointer = ModelCheckpoint(filepath='/tmp/weights.hdf5', verbose=1, save_best_only=True)
# earlystop = EarlyStopping(monitor='val_acc', min_delta=0.0001, patience=5, \
#                           verbose=1, mode='auto')
classifier = model()

classifier.fit(X_train, y_train,
               batch_size = 1024,
               nb_epoch = 2000,
               callbacks=
               [tensorboard,
                checkpointer,
                # earlystop,
                ]
               )

# estimator = KerasClassifier(
#     build_fn=model,
#     epochs=50,
#     batch_size=2048,
#     verbose=1,
#     callbacks=[tensorboard]
# )
# # fix random seed for reproducibility
# seed = 7
# numpy.random.seed(seed)
# kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
#
# results = cross_val_score(estimator, X, dummy_y, cv=kfold)
# print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

#
# model = Sequential()
# model.add(Embedding(10, output_dim=256))
# model.add(Dropout(0.5))
# model.add(Dense(32, activation='sigmoid'))
#
# model.compile(loss='categorical_crossentropy',
#               optimizer='rmsprop',
#               metrics=['accuracy'])
#
# model.fit(X_train, y_train, batch_size=16, epochs=10)
# # score = model.evaluate(x_test, y_test, batch_size=16)
#


# Fitting the ANN to the Training set
# score = KerasClassifier.evaluate(X_test, y_test, batch_size=16)
# print (score)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
# y_pred = classifier.predict(X_test)
# y_pred = (y_pred > 0.5)
#
# # Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)
