import numpy as np

class freeE:
    def __init__(self, dims, freeE, icm=0, err=0):
        if np.size(dims) == 3:
            self.lx, self.ly, self.lz = dims[0], dims[1], dims[2]
        else:
            print('\n\nDIMS NOT SIZE 3: (lx, ly, lz)\n\n')
            return
        self.freeE = freeE
        self.icm   = icm
        self.err   = err
        
test = freeE((8,13.8,15), -2.98579, icm=5.5e-06, err=4.0e-04)
test2= freeE((13.8,13.8,15), -2.98578, icm=2.2e-06, err=1.3e-04)