import pandas as pd

def ResAnaysis(results):

    res = pd.DataFrame(results)

    res.to_csv("results.csv")
    ax = res.plot()
    fig = ax.get_figure()
    fig.savefig('results.png')