import pandas
import matplotlib.pyplot as plt
import numpy as np

def graficar():

    df = pandas.DataFrame(dict(graph=['Dragon', 'MOESI', 'MOSI', 'MESI', 'MSI'],
                                n=[8626, 3640, 3741, 3640, 3741], 
                                m=[517, 517, 517, 517, 517], 
                                l=[0, 0, 0, 1432, 1432],
                                k=[8093, 1793, 1793, 1793, 1793])) 

    ind = np.arange(len(df))
    width = 0.2

    fig, ax = plt.subplots()
    ax.barh(ind + width + width + width + width, df.n, width, color='red', label='Bus Transaction')
    ax.barh(ind + width + width + width, df.m, width, color='orange', label='Memory Request')
    ax.barh(ind + width + width, df.l, width, color='yellow', label='Memory Writeback')
    ax.barh(ind + width, df.k, width, color='purple', label='Cache Transaction')

    ax.set(yticks=ind + width + width, yticklabels=df.graph, ylim=[2*width - 0.5, len(df)])
    ax.legend()
    ax.set_title('Lock Fill Bucket')

    plt.show()
