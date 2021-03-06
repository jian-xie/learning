class Conf:
    SCENARIO = 'Base'
    STRFRQ = {30: 'M', 7: 'W', 1: 'D'}
    DATAFREQ = 7#days
    TRAIN_FROM = 0 * 365
    TRAIN_TO = 22.66 * 365
    VAL_FROM = 17.66 * 365
    VAL_TO = 30 * 365
    ROLLWINDOW = 5 * 365

    LAG = 0

    XOUT_DIM = 32
    BATCH_SIZE = 64
    BATCH_INDEX = 0


    Y = ['GT10 Govt']
    #XS = [['GT10 Govt'], ['GT10 Govt']]
    Y_IN_X = 0

    XS = [['GT10 Govt'],
    ['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt','GTGBP10Y Govt', 'EHUPGB Index',  'EHGDGB Index', 'EHPIGB Index'],
    ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index', 'EHPIEU Index','SX5E Index'],
    ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt','GTJPY10Y Govt', 'EHUPJP Index',  'EHGDJP Index', 'EHPIJP Index','NKY Index'],
    ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt','GTAUD10Y Govt', 'EHUPAU Index',  'EHGDAU Index', 'EHPIAU Index','AS51 Index'],
    ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt','GTCAD10Y Govt', 'EHUPCA Index',  'EHGDCA Index', 'EHPICA Index','SPTSX60 Index'],
    ['GT2 Govt', 'GT5 Govt', 'EHUPUS Index',  'EHGDUS Index', 'EHPIUS Index','SPX Index',
     'CONSUEXR Index','NFP TYOY Index', 'CONSPXMD Index']
          ]


    DATAFMT={
        'pct_change':['USDGBP Curncy', 'USDEUR Curncy', 'USDCNH Curncy', 'USDJPY Curncy',
           'USDAUD Curncy', 'USDCAD Curncy', 'SPX Index', 'SX5E Index',
           'SHCOMP Index', 'NKY Index', 'AS51 Index', 'SPTSX60 Index', 'CONSUEXR Index'],

        'diff':['GT2 Govt',
            'GT5 Govt', 'GT10 Govt', 'GTGBP2Y Govt', 'GTGBP5Y Govt',
            'GTGBP10Y Govt', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt',
            'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'GTAUD2Y Govt',
            'GTAUD5Y Govt', 'GTAUD10Y Govt', 'GTCAD2Y Govt', 'GTCAD5Y Govt',
            'GTCAD10Y Govt', 'EHUPUS Index', 'EHUPGB Index', 'EHUPEU Index',
            'EHUPCN Index', 'EHUPJP Index', 'EHUPAU Index', 'EHUPCA Index',
            'EHGDUS Index', 'EHGDGB Index', 'EHGDEU Index', 'EHGDCN Index',
            'EHGDJP Index', 'EHGDAU Index', 'EHGDCA Index', 'EHPIUS Index',
            'EHPIGB Index', 'EHPIEU Index', 'EHPICN Index', 'EHPIJP Index',
            'EHPIAU Index', 'EHPICA Index', 'NFP TYOY Index',
            'CONSPXMD Index'],
        'value':[]

    }

    def overwrite(self,sn):
        for key in sn:
            setattr(self,key,sn[key])