import pandas
import matplotlib.pyplot as plt
import numpy as np

def graficar():

    df = pandas.DataFrame(dict(graph=['Dragon', 'MOESI', 'MOSI', 'MESI', 'MSI'],
                                n=[32000, 32000, 32000, 31999, 31999], 
                                m=[1, 1, 1, 1, 1], 
                                l=[0, 0, 0, 15999, 15999])) 

    ind = np.arange(len(df))
    width = 0.3

    fig, ax = plt.subplots()
    ax.barh(ind + width + width + width, df.n, width, color='red', label='Bus Transaction')
    ax.barh(ind + width + width, df.m, width, color='orange', label='Memory Request')
    ax.barh(ind + width, df.l, width, color='yellow', label='Memory Writeback')

    ax.set(yticks=ind + width + width, yticklabels=df.graph, ylim=[2*width - 0.5, len(df)])
    ax.legend()
    ax.set_title('MSI vs MOSI code')

    plt.show()
