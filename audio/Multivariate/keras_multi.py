from pandas import read_csv
from matplotlib import pyplot
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense, Dropout
from keras.layers.recurrent import LSTM

# from keras.utils import plot_model

# load dataset
dataset = read_csv('data/music_data.csv', header=0, index_col=0)
values = dataset.values
# specify columns to plot
groups = [-1, 0]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1


pyplot.show()

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# load dataset
dataset = read_csv('data/music_data.csv', header=0)
values = dataset.values
# integer encode direction
encoder = LabelEncoder()
values[:, 0] = encoder.fit_transform(values[:, 0])
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
print(reframed.head())


# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

# split into train and test sets
values = reframed.values
n_train_hours = 9000
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, 0:2], train[:, 0]
test_X, test_y = test[:, 0:2], test[:, 0]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

visible = Input(shape=(train_X.shape[1], train_X.shape[2]))
hidden1 = LSTM(50, return_sequences=True)(visible)
dropout1 = Dropout(0.5)(hidden1)

hidden2 = LSTM(50, return_sequences=True)(dropout1)
dropout2 = Dropout(0.5)(hidden2)

hidden3 = LSTM(50, return_sequences=True)(dropout2)
dropout3 = Dropout(0.5)(hidden3)
#
#hidden4 = LSTM(256, return_sequences=True)(dropout3)
#dropout4 = Dropout(0.5)(hidden4)
#
#hidden5 = LSTM(256, return_sequences=True)(dropout4)
#dropout5 = Dropout(0.5)(hidden5)
#
#hidden6 = LSTM(256, return_sequences=True)(dropout5)
#dropout6 = Dropout(0.5)(hidden6)
#
#hidden7 = LSTM(256, return_sequences=True)(dropout6)
#dropout7 = Dropout(0.5)(hidden7)
#
#hidden8 = LSTM(256, return_sequences=True)(dropout7)
#dropout8 = Dropout(0.5)(hidden8)
#
#hidden9 = LSTM(256, return_sequences=True)(dropout8)
#dropout9 = Dropout(0.5)(hidden9)
#
#hidden10 = LSTM(256, return_sequences=True)(dropout9)
#dropout10 = Dropout(0.5)(hidden10)

hidden4 = LSTM(50)(dropout3)
output = Dense(1, activation='sigmoid')(hidden4)

model = Model(inputs=visible, outputs=output)
model.compile(loss='mae', optimizer='adam')
# plot_model(model, to_file='model.png')
model.summary()

# fit network
history = model.fit(train_X, train_y, epochs=250, batch_size=72, validation_data=(test_X, test_y), verbose=2,
                    shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)
