from IVplot import getIV
from RTplot import getRT
import numpy

def test_getIV():
    f = "../CDT_E/B1/RT2/B1_9 11 10 12_R-T_2_IV_0.txt"  #Test file
    dat = getIV(f)
    assert dat.shape[1] == 2
    assert type(dat) == numpy.ndarray
    assert dat[0][0] == 0.0
    assert dat[0][1] == 0.0000037838727475

def test_getRT():
    f = "../CDT_E/B1/RT2/B1_9 11 10 12_R-T_2_IV_"  #Test file
    dat = getRT(f,886)
    assert len(dat[0]) == len(dat[1]) == 886
    assert dat[0][0] > dat[0][-1]
    assert dat[1][0] > dat[1][-1]
    assert all(dat[0]>0)
    assert all(dat[1]>0)
