from keras.models import Sequential
from keras.layers import Merge, LSTM, Dense, Dropout, TimeDistributed
from keras.optimizers import Adam
import numpy as np

def getModel(C):

    timesteps = int(C.ROLLWINDOW/C.DATAFREQ)
    nb_classes = 1

    encoders = []

    for x in C.XS:
        encoder = Sequential()
        Data_dim = len(x)
        encoder.add(LSTM(output_dim=C.XOUT_DIM, return_sequences=True, stateful=True, batch_input_shape=(C.BATCH_SIZE, timesteps, Data_dim)))
        encoder.add(Dropout(0.5))
        #encoder.add(LSTM(output_dim=C.XOUT_DIM, return_sequences=True, stateful=True))
        #encoder.add(Dropout(0.5))
        encoder.add(LSTM(output_dim=C.XOUT_DIM, return_sequences=True, stateful=True))
        #encoder.add(TimeDistributed(Dense(output_dim=C.XOUT_DIM, activation='tanh')))
        encoder.add(Dropout(0.5))
        encoder.add(LSTM(output_dim=C.XOUT_DIM, stateful=True))
        encoders.append(encoder)

    decoder = Sequential()
    decoder.add(Merge(encoders, mode='concat'))
    decoder.add(Dropout(0.5))
    #decoder.add(LSTM(output_dim=64))
    #decoder.add(Dropout(0.5))
    #decoder.add(LSTM(128, stateful=True))
    #decoder.add(TimeDistributed(Dense(64)))
    #decoder.add(Dropout(0.5))
    #decoder.add(TimeDistributed(Dense(output_dim=64, activation='tanh')))
    decoder.add(Dense(96, activation='tanh'))
    decoder.add(Dropout(0.5))
    decoder.add(Dense(nb_classes))


    #sgd = SGD(lr=0.1, decay=1e-6, momentum=0.2, nesterov=True)
    adam = Adam(0.006)
    decoder.compile(loss='mse', optimizer='adam')
    #decoder.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])

    return decoder
