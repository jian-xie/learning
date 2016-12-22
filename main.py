
from conf import Conf
from scenario import SCENARIOS
from model import getModel
from data_load import getData, prepareData, normaliz
from train_data import getTrainData
from results import ResAnaysis

if __name__ == '__main__':
    global C
    C = Conf()
    for conf in SCENARIOS:
        C.overwrite(conf['conf'])

        df = getData(C.STRFRQ[C.DATAFREQ])
        #df = prepareData(df)
        ndf = normaliz(df)
        dfY_diff = df[C.Y].diff()
        train_Xs, train_Y = getTrainData(C,ndf, dfY_diff)
        val_Xs, val_Y = getTrainData(C,ndf, dfY_diff)
        model = getModel(C)

        res = model.fit(train_Xs, train_Y, batch_size=C.BATCH_SIZE, nb_epoch=40, validation_data=(val_Xs, val_Y))


    ResAnaysis(res.history)

