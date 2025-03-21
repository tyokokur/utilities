import pandas as pd, numpy as np
from Data import Data

''' chi = 1.25, N = 200, b = 1.0, v = 4.19, T = 293 '''

class All:
    def __init__(self, datasets):
        self.all = pd.DataFrame(datasets, columns=['alpha', 'sigma', 'morph', 'name', 'n', 'data'])
        
    def show(self): 
        styler = self.all.iloc[:,:5].style \
            .format(precision=3) \
            .hide(axis='index')
        display(styler)
        
    def find(self, condition, n_cond=1):
        # all Datas that meet condition (e.g., alpha = 0)
        subset = []
        return subset
        
datasets = []
pack_data = lambda name, data: [(data.alpha, data.sigma, data.morph, name, len(data.data), data)]

''' alpha = 0.00, sigma = 5e-03 '''
a0s5_hom = Data(0.00, 5e-03, 'hom')
a0s5_hom.new((8, 13.8, 15) , -2.98579, icm=5.5e-06, err=4.0e-04)
a0s5_hom.new((13.8,13.8,15), -2.98578, icm=2.2e-06, err=1.3e-04)
a0s5_hom.new((10.6,10.6,15), -2.98580, icm=1.0e-05, err=3.7e-05)
datasets += pack_data('a0s5_hom', a0s5_hom)

a0s5_hol = Data(0.00, 5e-03, 'hol')
a0s5_hol.new((8, 13.8, 15)   , -2.98419, icm=3.2e-06, err=4.0e-04)
a0s5_hol.new((13.8, 13.8, 15), -2.98544, icm=1.1e-05, err=4.5e-04)
a0s5_hol.new((15, 15,15)     , -2.98573, icm=2.1e-04, err=6.7e-04)
a0s5_hol.new((16, 16,15)     , -2.98602, icm=5.5e-05, err=1.8e-04)
a0s5_hol.new((17, 17,15)     , -2.98620, icm=6.8e-05, err=2.0e-04)
a0s5_hol.new((19, 19,15)     , -2.98637, icm=1.2e-05, err=5.6e-04)
a0s5_hol.new((21, 21,15)     , -2.98639, icm=2.4e-04, err=7.5e-04)
a0s5_hol.new((23, 23,15)     , -2.98644, icm=7.1e-05, err=7.3e-04)
datasets += pack_data('a0s5_hol', a0s5_hol)

a0s5_mic = Data(0.00, 5e-03, 'mic')
datasets += pack_data('a0s5_mic', a0s5_mic)

a0s5_str = Data(0.00, 5e-03, 'str')
datasets += pack_data('a0s5_str', a0s5_str)

''' alpha = 0.10, sigma = 5e-03 '''
a1s5_hol = Data(0.10, 5e-03, 'hol')
a1s5_hol.new((8, 13.8, 35)   , -2.93661, icm=9.7e-05, err=3.3e-04)
a1s5_hol.new((13.8, 13.8, 35), -2.93731, icm=1.8e-05, err=4.4e-04) 
a1s5_hol.new((15, 15, 35)    , -2.93757, icm=1.6e-04, err=4.0e-04) 
a1s5_hol.new((16, 16, 35)    , -2.93773, icm=3.1e-05, err=3.4e-04)
a1s5_hol.new((17, 17, 35)    , -2.93781, icm=4.7e-05, err=4.1e-04)
a1s5_hol.new((19, 19, 35)    , -2.93795, icm=3.9e-04, err=3.1e-04)
a1s5_hol.new((21.2, 21.2, 35), -2.93847, icm=3.4e-03, err=4.2e-04)
a1s5_hol.new((25.2, 25.2, 35), -2.93854, icm=2.7e-03, err=3.9e-04)
datasets += pack_data('a1s5_hol', a1s5_hol)

a1s5_str = Data(0.10, 5e-03, 'str')
a1s5_str.new((15, 13.8, 35), -2.93758, icm=9.4e-05, err=3.6e-04)
a1s5_str.new((17, 13.8, 35), -2.93775, icm=1.8e-05, err=5.4e-04)
a1s5_str.new((15, 16, 35)  , -2.93762, icm=7.5e-05, err=2.6e-04)
a1s5_str.new((17, 16, 35)  , -2.93788, icm=1.5e-04, err=3.0e-04)
datasets += pack_data('a1s5_str', a1s5_str)

a1s5_hom = Data(0.10, 5e-03, 'hom')
a1s5_hom.new((10, 10, 35), -2.93780, icm=3.9e-04, err=7.6e-05)
a1s5_hom.new((12, 12, 35), -2.93788, icm=9.4e-05, err=2.3e-05)
datasets += pack_data('a1s5_hom', a1s5_hom)

All = All(datasets)