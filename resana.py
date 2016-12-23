import pandas as pd

def ResAnaysis(results):
    writer = pd.ExcelWriter('results/results.xlsx')
    mdtext = """\n## Results\n\n[Results in Excel file](results/results.xlsx)\n"""
    for res in results:
        scenario = res[0]
        df = pd.DataFrame(res[1])
        df.to_excel(writer,scenario)

        cdf = pd.DataFrame({'Base':results[0][1]['val_acc'],scenario:res[1]['val_acc']})
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




