import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from IVplot import getIV

def getRT(f,n):
    '''f = filepath up to index, n = index of final file'''
    R = []
    Rf = []     #File quoted resistances
    T = []
    for i in range(n):    #Up to highest file ID
        xy = getIV(f+str(i)+".txt") #Array of IV values for a single temp
        R.append(stats.linregress(xy[:,0],xy[:,1])[0]) #Linear regression of IV for R
        with open(f+str(i)+".txt", 'r') as fi:
            j = 0
            while j < 10:    #Move through file to lines with T
                line = fi.readline()
                if j == 4:
                    Rf.append(float(line))  #Get file quoted R
                if j == 6:
                    line = line.split("\t")
                    T.append(float(line[0])) #Get start T value
                if j == 9:
                    line = line.split("\t")
                    T[i] += float(line[0])   #Get end T value
                j += 1
    R = np.array(R)
    Rf = np.array(Rf)
    T = np.array(T)
    T = T/2 #Get average T
    return (R,T,Rf)

def plotRT(f,n):
    '''f = filepath up to index, n = index of final file'''
    dat = getRT(f,n)
    plt.plot(dat[1],dat[0],'o')
    plt.xlabel("T (K)")
    plt.ylabel("R (ohm)")
    plt.show()

def plotRfT(f,n):
    dat = getRT(f,n)
    plt.plot(dat[1],dat[2],'o')
    plt.xlabel("T (K)")
    plt.ylabel("R (ohm)")
    plt.show()
