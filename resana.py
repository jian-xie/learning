import pandas as pd

def ResAnaysis(results):
    writer = pd.ExcelWriter('results/results.xlsx')
    mdtext = """\n## Results\n\n[Results in Excel file](results/results.xlsx)\n"""
    for scenario in results:
        df = pd.DataFrame(results[scenario])
        df.to_excel(writer,scenario)

        cdf = pd.DataFrame({'Base':results['Base']['val_acc'],scenario:results[scenario]['val_acc']})
        ax = cdf.plot()
        fig = ax.get_figure()
        pngfile = 'results/'+scenario+'.png'
        fig.savefig(pngfile)

        mdtext += '\n![alt]('+pngfile.replace(' ','%20')+')\n'

    writer.save()

    fi = open('implement.md', 'r')
    fo = open('readme.md', 'w')
    fo.write(fi.read()+mdtext)
    fo.close()
    fi.close()




