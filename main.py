from model import getModel
from conf import DATAFREQ, Y, XS, TRAIN_FROM, TRAIN_TO, VAL_FROM,VAL_TO, ROLLWINDOW
from data_load import getData,prepareData,normaliz
from train_data import getTrainData

if __name__ == '__main__':
    strFrq = {30: 'M', 7: 'W', 1: 'D'}
    df = getData(strFrq[DATAFREQ])
    df = prepareData(df)
    ndf = normaliz(df)
    train_Xs, train_Y = getTrainData(ndf, df[Y],TRAIN_FROM, TRAIN_TO, ROLLWINDOW)
    val_Xs, val_Y = getTrainData(ndf, df[Y], VAL_FROM,VAL_TO, ROLLWINDOW)
    model = getModel()
    model.fit(train_Xs, train_Y, batch_size=256,
            nb_epoch=10,
            validation_data=(val_Xs, val_Y))