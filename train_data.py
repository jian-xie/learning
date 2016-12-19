from conf import DATAFREQ, Y, XS
from data_load import getData,prepareData,normaliz
import numpy as np

def getTrainData(df, dfY, fromD, toD, rollingwindow):
    ffr = int(fromD / DATAFREQ)
    fto = int(toD / DATAFREQ)
    frw = int(rollingwindow / DATAFREQ)
    train_Xs, train_Y = [],[]
    for cols in XS:
        train_Xs.append(np.array([df[i + ffr:i + ffr + frw].as_matrix(cols) for i in range(fto - ffr - frw)]))
    for i in range(fto - ffr - frw):

        _Y = dfY.iloc[i+ffr+frw][0]
        Y = [0,1,0]
        if _Y > 0:
            Y = [0,0,1]
        elif _Y < 0:
            Y = [1,0,0]
        train_Y.append(Y)
        '''
        if _Y >= dfY[dfY>0].mean()[0]:
            train_Y.append([0,0,0,0,1])
        elif _Y >= dfY[dfY > 0].mean()[0] / 4:
            train_Y.append([0, 0, 0, 1, 0])
        elif _Y >= dfY[dfY < 0].mean()[0] / 4:
            train_Y.append([0, 0, 1, 0, 0])
        elif _Y >= dfY[dfY < 0].mean()[0] :
            train_Y.append([0, 1, 0, 0, 0])
        else:
            train_Y.append([1, 0, 0, 0, 0])
        '''
    #train_Y = np.array([dfY.iloc[i+ffr+frw] for i in range(fto - ffr - frw)])
    return train_Xs, np.array(train_Y)


if __name__ == '__main__':
    strFrq = {30: 'M', 7: 'W', 1: 'D'}
    df = getData(strFrq[DATAFREQ])
    df = prepareData(df)
    ndf = normaliz(df)
    train_X, train_Y = getTrainData(ndf,df[Y], 1*365,20*365,1*365)

    val_X, val_Y = getTrainData(ndf,df[Y], 20*365, 29.5 * 365, 1 * 365)