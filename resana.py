import pandas as pd

def ResAnaysis(results):
    writer = pd.ExcelWriter('results/results.xlsx')
    mdtext = """\n## Results\n\n[Results in Excel file](results/results.xlsx)\n\nBase ![](results/Base.png)"""
    for res in (r for r in results if r[0] != 'Base'):
        scenario = res[0]
        df = pd.DataFrame(res[1])
        df.to_excel(writer,scenario)

        cdf = pd.DataFrame({'Base':results[0][1]['val_loss'],scenario:res[1]['val_loss']})
        ax = cdf.plot()
        fig = ax.get_figure()
        pngfile = 'results/'+scenario+'.png'
        fig.savefig(pngfile)

        mdtext += '\n'+scenario+' ![]('+pngfile.replace(' ','%20')+')\n'

    writer.save()

    cdf = pd.DataFrame(results[0][1])
    ax = cdf.plot()
    fig = ax.get_figure()
    pngfile = 'results/Base.png'
    fig.savefig(pngfile)

    fi = open('implement.md', 'r')
    fo = open('readme.md', 'w')
    fo.write(fi.read()+mdtext)
    fo.close()
    fi.close()




