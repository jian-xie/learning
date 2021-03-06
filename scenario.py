SCENARIOS = [
    {'SCENARIO': 'Base'},

    {'SCENARIO': 'Y_in_X_1','Y_IN_X':1},

    {'SCENARIO': 'Y_in_X_6','Y_IN_X':6},

    {'SCENARIO':'exclude_Eco_data',
     'XS':[['GT10 Govt'],
        ['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt','GTGBP10Y Govt'],
        ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt','SX5E Index'],
        ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt','GTJPY10Y Govt','NKY Index'],
        ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt','GTAUD10Y Govt','AS51 Index'],
        ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt','GTCAD10Y Govt','SPTSX60 Index'],
        ['GT2 Govt', 'GT5 Govt', 'SPX Index']]
     },

    {'SCENARIO': 'exclude_GBP',
     'XS': [['GT10 Govt'],
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': 'exclude_EUR',
     'XS': [['GT10 Govt'],
         ['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': 'exclude_JPY',
     'XS': [['GT10 Govt'],
         ['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     }
]

