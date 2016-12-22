from keras.models import Sequential
from keras.layers import Merge, LSTM, Dense, Dropout, TimeDistributed
from keras.optimizers import SGD
import numpy as np
from conf import ROLLWINDOW, DATAFREQ, XS, XOUT_DIM, BATCH_SIZE

def getModel():

    timesteps = int(ROLLWINDOW/DATAFREQ)
    nb_classes = 3

    encoders = []

    for x in XS:
        encoder = Sequential()
        data_dim = len(x)
        encoder.add(LSTM(XOUT_DIM, return_sequences=True, stateful=True, batch_input_shape=(BATCH_SIZE, timesteps, data_dim)))
        encoders.append(encoder)

    decoder = Sequential()
    decoder.add(Merge(encoders, mode='concat'))
    decoder.add(LSTM(128, stateful=True, return_sequences=True))
    decoder.add(LSTM(128, stateful=True))
    #decoder.add(TimeDistributed(Dense(64)))
    #decoder.add(Dropout(0.5))
    decoder.add(Dense(128, activation='tanh'))
    decoder.add(Dense(nb_classes, activation='softmax'))


    #sgd = SGD(lr=0.1, decay=1e-6, momentum=0.2, nesterov=True)
    decoder.compile(loss='categorical_crossentropy', optimizer='sgd',
                    metrics=['accuracy'])

    return decoder
