import pickle
import pandas as pd
from conf import DATAFMT, DATAFREQ

from sklearn import preprocessing

STARTDATE='1986-12-01'
ENDDATE='2016-12-31'

def loadExcel():
    dfs = []
    for i in [0,1]:
        cnt = 0
        while True:
            df1 = pd.read_excel('data.xlsx', i, header = 0, index_col=0, parse_cols=[cnt*3,cnt*3+1]).dropna()
            if len(df1) > 0:
                df1.columns=[df1.index.name]
                dates = pd.date_range(pd.to_datetime(STARTDATE), pd.to_datetime(ENDDATE), freq='D')

                df1 = df1.reindex(dates, method='nearest')
                dfs.append(df1)
                cnt += 1
            else:
                break
    mdf = pd.concat(dfs, axis=1)
    return mdf

def getData(Frq):
    try:
        df = pickle.load( open( "df.p", "rb"))
    except:
        df = loadExcel()
        pickle.dump(df, open("df.p", "wb"))

    dates = pd.date_range(pd.to_datetime(STARTDATE), pd.to_datetime(ENDDATE), freq=Frq)
    df = df.reindex(dates, method='ffill')
    return df

def prepareData(df):
    #shift data outright value to change or percentage change

    pdf1 = df[DATAFMT['pct_change']].pct_change()
    pdf2 = df[DATAFMT['diff']].diff()
    pdf3 = df[DATAFMT['value']]

    mdf = pd.concat([pdf1,pdf2,pdf3], axis=1)[1:]
    return mdf

def normaliz(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    df_normalized = df.apply(lambda x: min_max_scaler.fit_transform(x))
    return df_normalized

if __name__ == '__main__':
    strFrq = {30:'M',7:'W',1:'D'}
    df = getData(strFrq[DATAFREQ])
    df = prepareData(df)
    df = normaliz(df)
    print(df)