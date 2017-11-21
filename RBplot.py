import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from IVplot import getIV

def getRB(f,nf,nl):
    '''f = filepath up to index, nf/nl = index of first/last file'''
    R = []
    B = []
    for i in range(nf,nl):
        xy = getIV(f+str(i)+".txt")
        R.append(stats.linregress(xy[:,0],xy[:,1])[0])
        with open(f+str(i)+".txt", 'r') as fi:
            j = 0
            while j < 3:
                line = fi.readline()
                j += 1
            line = line.split("\t")
            B.append(float(line[1][0:7]))
    R = np.array(R)
    B = np.array(B)
    return (R,B)

def plotRB(f,nf,nl):
    '''f = filepath up to index, n = index of final file'''
    dat = getRB(f,nf,nl)
    plt.plot(dat[1],dat[0],'o')
    plt.xlabel("B (T)")
    plt.ylabel("R (ohm)")
    plt.show()
