from ase.io.vasp import read_vasp
from pathlib import Path
import numpy as np
p=Path('structures/initial/ase_generated/gC3N4_N4/Fe@gC3N4_N4.vasp')
with p.open() as h:
    a=read_vasp(h)
d=a.get_all_distances(mic=True)
d += np.eye(len(a))*1e6
i,j=np.unravel_index(np.argmin(d), d.shape)
print('atoms',len(a),'min',d[i,j],'pair',i,j,a[i].symbol,a[j].symbol)
print('positions',a[i].position,a[j].position)
print('cell',a.cell)
