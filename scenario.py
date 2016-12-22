SCENARIOS = [
    {'SCENARIO': 'Base'},

    {'SCENARIO':'- Economic data',
     'XS':[['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt','GTGBP10Y Govt'],
        ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt','SX5E Index'],
        ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt','GTJPY10Y Govt','NKY Index'],
        ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt','GTAUD10Y Govt','AS51 Index'],
        ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt','GTCAD10Y Govt','SPTSX60 Index'],
        ['GT2 Govt', 'GT5 Govt','GT10 Govt', 'SPX Index']]
     },

    {'SCENARIO': '- GBP',
     'XS': [
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'GT10 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': '- EUR',
     'XS': [['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'GT10 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': '- JPY',
     'XS': [['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'GT10 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': '- AUD',
     'XS': [['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDCAD Curncy', 'GTCAD2Y Govt', 'GTCAD5Y Govt', 'GTCAD10Y Govt', 'EHUPCA Index', 'EHGDCA Index',
             'EHPICA Index', 'SPTSX60 Index'],
            ['GT2 Govt', 'GT5 Govt', 'GT10 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     },

    {'SCENARIO': '- CAD',
     'XS': [['USDGBP Curncy', 'GTGBP2Y Govt', 'GTGBP5Y Govt', 'GTGBP10Y Govt', 'EHUPGB Index', 'EHGDGB Index',
             'EHPIGB Index'],
            ['USDEUR Curncy', 'GTEUR2Y Govt', 'GTEUR5Y Govt', 'GTEUR10Y Govt', 'EHUPEU Index', 'EHGDEU Index',
             'EHPIEU Index', 'SX5E Index'],
            ['USDJPY Curncy', 'GTJPY2Y Govt', 'GTJPY5Y Govt', 'GTJPY10Y Govt', 'EHUPJP Index', 'EHGDJP Index',
             'EHPIJP Index', 'NKY Index'],
            ['USDAUD Curncy', 'GTAUD2Y Govt', 'GTAUD5Y Govt', 'GTAUD10Y Govt', 'EHUPAU Index', 'EHGDAU Index',
             'EHPIAU Index', 'AS51 Index'],
            ['GT2 Govt', 'GT5 Govt', 'GT10 Govt', 'EHUPUS Index', 'EHGDUS Index', 'EHPIUS Index', 'SPX Index',
             'CONSUEXR Index', 'NFP TYOY Index', 'CONSPXMD Index']]
     }
]
