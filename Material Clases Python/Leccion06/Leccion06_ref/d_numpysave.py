
"""

http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html#numpy.save


http://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html#numpy.load

"""
import numpy as np
from tempfile import TemporaryFile
outfile = TemporaryFile()


x = np.arange(10)
np.save(outfile, x)
del(x)

outfile.seek(0)  # Only needed here to simulate closing & reopening file
x = np.load(outfile)

print(x)

datos = np.loadtxt("n0012.dat", usecols=(1, 2), skiprows=3,
                   delimiter=' ')

import matplotlib.pyplot as plt
plt.plot(datos[:,0], datos[:,1])



np.savetxt("naca0012_mio.txt", datos, fmt="%.10f",
           delimiter="**")

plt.show()