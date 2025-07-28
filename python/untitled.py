import numpy as np, pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl, plotly.graph_objects as go
from Pha3D import Pha3D

class Process3D:

    def _get_data(self, fname, dims, fp, n_coarse=3, zmax=25, reflect_over='sw', isomin=0.10,
    pha3d = Pha3D(f2_fnames[1], dims=f2_boxes[1], fprefix=fp)
    data = pha3d.get_vol(isomin=isomin, fprefix=fp,  n_coarse=1, zmax=25.0, reflect_over='sw', write_html=False)