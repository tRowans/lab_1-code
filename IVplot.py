import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def getIV(f):
    dat = np.genfromtxt(f,skip_header=11)   #Get all data from file
    dat = dat[:,0:2]   #take only I and V
    return dat 

def plotIV(f):
    dat = getIV(f)
    plt.plot(dat[:,0],dat[:,1], 'o')
    plt.xlabel("I")
    plt.ylabel("V")
    plt.show()
