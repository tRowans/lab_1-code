import numpy as np
import matplotlib.pyplot as plt

def getdata():
    f = "../CDT_E/B1/IV/B1_9 11 10 12_I-V_244K_1.txt"
    dat = np.genfromtxt(f,skip_header=11)   #Get all data from file
    dat = dat[:,0:2]   #take only I and V
    return dat

def plotIV(dat):
    plt.scatter(dat[0,:],dat[1,:])
    plt.show()

plotIV(getdata())
