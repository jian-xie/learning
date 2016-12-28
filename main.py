
from conf import Conf
from scenario import SCENARIOS
from model import getModel
from data_load import getData, prepareData, normaliz
from train_data import getTrainData
from resana import ResAnaysis

if __name__ == '__main__':
    global C
    C = Conf()
    res = []
    df = getData(C.STRFRQ[C.DATAFREQ])
    # df = prepareData(df)
    ndf =df# normaliz(df)
    dfY=df[C.Y]
    for sn in SCENARIOS:
        #encoder.add(Dropout(0.5))
        #encoder.add(LSTM(output_dim=C.XOUT_DIM, return_sequences=True, stateful=True))
        C.overwrite(sn)
        print(" - "+C.SCENARIO)

        train_Xs, train_Y = getTrainData(C,ndf, dfY)
        val_Xs, val_Y = getTrainData(C,ndf, dfY,'test')
        model = getModel(C)

        #cost = model.train_on_batch([train_Xs[i][0:C.BATCH_SIZE] for i in range(len(train_Xs))], train_Y[0:C.BATCH_SIZE])
        #print(cost)

        re = model.fit(train_Xs, train_Y, batch_size=C.BATCH_SIZE, nb_epoch=40, validation_data=(val_Xs, val_Y))
        res.append([C.SCENARIO,re.history])

    ResAnaysis(res)

