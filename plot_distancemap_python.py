import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv('Rij.dat', delimiter=r"\s+", header= None, engine = "python")

plt.imshow(data, aspect='equal', interpolation='None')
plt.xlabel('Fragment number', fontsize=16)
plt.ylabel('Fragment number', fontsize=16)
plt.xticks(range(data.shape[1]), range(1, data.shape[1] + 1))
plt.yticks(range(data.shape[0]), range(1, data.shape[0] + 1))

plt.clim(0,35)
cbar = plt.colorbar()
cbar.set_label('Distance (Angstrom)', fontsize=14)
#plt.title("Average pair-wise distance between centers-of-mass of residues", fontsize=12)

plt.savefig('deltadistancemap-pPP15.png')
plt.show()


