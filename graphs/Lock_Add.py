import pandas
import matplotlib.pyplot as plt
import numpy as np

def graficar():

    df = pandas.DataFrame(dict(graph=['Dragon', 'MOESI', 'MOSI', 'MESI', 'MSI'],
                                n=[5521, 2334, 2367, 2331, 2367], 
                                m=[1521, 1521, 1521, 1521, 1521], 
                                l=[0, 0, 0, 311, 311],
                                k=[3985, 604, 604, 604, 604])) 

    ind = np.arange(len(df))
    width = 0.2

    fig, ax = plt.subplots()
    ax.barh(ind + width + width + width + width, df.n, width, color='red', label='Bus Transaction')
    ax.barh(ind + width + width + width, df.m, width, color='orange', label='Memory Request')
    ax.barh(ind + width + width, df.l, width, color='yellow', label='Memory Writeback')
    ax.barh(ind + width, df.k, width, color='purple', label='Cache Transaction')

    ax.set(yticks=ind + width + width, yticklabels=df.graph, ylim=[2*width - 0.5, len(df)])
    ax.legend()
    ax.set_title('Lock Add')

    plt.show()