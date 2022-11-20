import matplotlib.pyplot as plt
import numpy as np

# imports graphs
import MSI_vs_MESI as MSI_vs_MESI
import MSI_vs_MOSI as MSI_vs_MOSI
import MOESI_vs_Dragon as MOESI_vs_Dragon
import Lock_Add as Lock_Add
import Lock_Fill_Bucket as Lock_Fill_Bucket
import Wild_Fill_Bucket as Wild_Fill_Bucket

def graficarDatos (code):

    # casos para BP:
    if (code == 'MSI_vs_MESI'):
        MSI_vs_MESI.graficar()

    elif (code == 'MSI_vs_MOSI'):
        MSI_vs_MOSI.graficar()

    elif (code == 'MOESI_vs_Dragon'):
        MOESI_vs_Dragon.graficar()

    elif (code == 'Lock_Add'):
        Lock_Add.graficar()

    elif (code == 'Lock_Fill_Bucket'):
        Lock_Fill_Bucket.graficar()

    elif (code == 'Wild_Fill_Bucket'):
        Wild_Fill_Bucket.graficar()

    else:
        print ('No se encontró la gráfica con estas características')
        return 0