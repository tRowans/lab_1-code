from IVplot import getdata
import numpy

def test_getdata():
    assert getdata().shape[1] == 2
    assert type(getdata()) == numpy.ndarray
