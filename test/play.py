from data_load import getData
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = getData('M')
pdf = df.iloc[:,0:3]


plt.figure(); pdf.plot(); plt.legend(loc='best')

print('hi')