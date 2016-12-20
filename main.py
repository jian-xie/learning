from model import getModel
from conf import DATAFREQ, Y, XS, TRAIN_FROM, TRAIN_TO, VAL_FROM,VAL_TO, ROLLWINDOW, BATCH_SIZE, BATCH_INDEX
from data_load import getData,prepareData,normaliz
from train_data import getTrainData
from results import ResAnaysis

if __name__ == '__main__':
    strFrq = {30: 'M', 7: 'W', 1: 'D'}
    df = getData(strFrq[DATAFREQ])
    df = prepareData(df)
    ndf = normaliz(df)
    train_Xs, train_Y = getTrainData(ndf, df[Y],TRAIN_FROM, TRAIN_TO, ROLLWINDOW)
    val_Xs, val_Y = getTrainData(ndf, df[Y], VAL_FROM,VAL_TO, ROLLWINDOW)
    model = getModel()

    res = model.fit(train_Xs, train_Y, batch_size=256, nb_epoch=100, validation_data=(val_Xs, val_Y))

    '''
    results = []
    for step in range(401):
        # data shape = (batch_num, steps, inputs/outputs)
        X_batch = [train_Xs[i][BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :, :] for i in range(len(train_Xs))]
        Y_batch = train_Y[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :]
        tcost, taccuracy = model.train_on_batch(X_batch, Y_batch)
        BATCH_INDEX += BATCH_SIZE
        BATCH_INDEX = 0 if BATCH_INDEX >= train_Xs[0].shape[0] else BATCH_INDEX

        if step % 50 == 0:
            cost, accuracy = model.evaluate(val_Xs, val_Y, batch_size=val_Y.shape[0], verbose=False)
            results.append([tcost, taccuracy,cost, accuracy])
    '''
    ResAnaysis(res.history)

