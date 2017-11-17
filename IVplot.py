import numpy as np
import matplotlib.pyplot as plt

def getdata(f):
    dat = np.genfromtxt(f,skip_header=11)   #Get all data from file
    dat = dat[0:1][:]   #take only I and V
    return dat

def plotIV(dat):
    plt.scatter(dat)
    plt.show()
