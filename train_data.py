from data_load import getData,prepareData,normaliz
import numpy as np

def getTrainData(C,df, dfY, type='train'):
    if type == 'train':
        fromD, toD = C.TRAIN_FROM, C.TRAIN_TO
    else:
        fromD, toD = C.VAL_FROM, C.VAL_TO
    ffr = int(fromD / C.DATAFREQ)
    fto = int(toD / C.DATAFREQ)
    if fto >= len(dfY):
        fto = len(dfY)-1
    frw = int(C.ROLLWINDOW / C.DATAFREQ)
    train_Xs, train_Y = [],[]
    for cols in C.XS:
        train_Xs.append([df[i + ffr:i + ffr + frw].as_matrix(cols) for i in range(fto - ffr - frw)])
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
    # add duplicated sample to fill a batch size
    nfill = (C.BATCH_SIZE - len(train_Y) % C.BATCH_SIZE) % C.BATCH_SIZE
    for n in range(nfill):
        for i in range(len(train_Xs)):
            train_Xs[i].append(train_Xs[i][-nfill])
        train_Y.append(train_Y[-nfill])
    print(type+' sample size fill: '+str(nfill))

    return [np.array(train_Xs[i]) for i in range(len(train_Xs))], np.array(train_Y)



if __name__ == '__main__':

    df = getData(C.STRFRQ[C.DATAFREQ])
    df = prepareData(df)
    ndf = normaliz(df)
    train_X, train_Y = getTrainData(ndf,df[C.Y], 1*365,20*365,1*365)

    val_X, val_Y = getTrainData(ndf,df[C.Y], 20*365, 29.5 * 365, 1 * 365)