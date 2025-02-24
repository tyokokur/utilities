import pandas as pd, numpy as np
from Data import Data

''' chi = 1.25, N = 200, b = 1.0, v = 4.19, T = 293 '''

class All:
    def __init__(self, datasets):
        self.all = pd.DataFrame(datasets, columns=['alpha', 'sigma', 'morph', 'name', 'data'])
        
    def show(self): 
        styler = self.all.iloc[:,:4].style.hide(axis='index')
        display(styler)
        
    def find(self, condition, n_cond=1):
        # all Datas that meet condition (e.g., alpha = 0)
        return
        
datasets = []

''' alpha = 0.00, sigma = 5e-03 '''
a0s5_hom = Data(0.00, 5e-03, 'hom')
a0s5_hom.new((8, 13.8, 15) , -2.98579, icm=5.5e-06, err=4.0e-04)
a0s5_hom.new((13.8,13.8,15), -2.98578, icm=2.2e-06, err=1.3e-04)
a0s5_hom.new((10.6,10.6,15), -2.98580, icm=1.0e-05, err=3.7e-05)
datasets += [(a0s5_hom.alpha, a0s5_hom.sigma, a0s5_hom.morph, 'a0s5_hom', a0s5_hom)]

a0s5_hol = Data(0.00, 5e-03, 'hol')
a0s5_hol.new((8, 13.8, 15)   , -2.98419, icm=3.2e-06, err=4.0e-04)
a0s5_hol.new((13.8, 13.8, 15), -2.98544, icm=1.1e-05, err=4.5e-04)
a0s5_hol.new((15, 15,15)     , -2.98573, icm=2.1e-04, err=6.7e-04)
a0s5_hol.new((16, 16,15)     , -2.98602, icm=5.5e-05, err=1.8e-04)
a0s5_hol.new((17, 17,15)     , -2.98620, icm=6.8e-05, err=2.0e-04)
datasets += [(a0s5_hol.alpha, a0s5_hol.sigma, a0s5_hol.morph, 'a0s5_hol', a0s5_hol)]

All = All(datasets)