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
        
datasets = []
pack_data = lambda name, data: [(data.alpha, data.sigma, data.morph, name, len(data.data), data)]

''' alpha = 0.00, sigma = 3e-03 '''
a0s3_mic = Data(0.00, 3e-03, 'mic')
a0s3_mic.new((16, 27.6, 15)  , -1.77937, icm=1.9e-04, err=8.3e-04)
a0s3_mic.new((20, 27.6, 15)  , -1.77956, icm=2.6e-03, err=5.9e-04) 
a0s3_mic.new((20, 32, 15)    , -1.77930, icm=7.4e-03, err=1.7e-03) 
a0s3_mic.new((24.2, 24.2, 15), -1.77899, icm=3.0e-04, err=1.6e-03)
a0s3_mic.new((18.2,25.2,15.2), -1.77969, icm=3.3e-03, err=7.9e-04)
datasets += pack_data('a0s3_mic', a0s3_mic)

a0s3_str = Data(0.00, 3e-03, 'str')
a0s3_str.new((20.2, 20.2, 15.2), -1.77861, icm=5.9e-04, err=1.5e-04)
a0s3_str.new((25.2, 25.2, 15.2), -1.77828, icm=5.2e-03, err=1.2e-03)
a0s3_str.new((18.2, 18.2, 15.2), -1.77893, icm=7.0e-04, err=1.5e-04)
a0s3_str.new((22.2, 22.2, 15.2), -1.77817, icm=2.5e-03, err=3.1e-04)
datasets += pack_data('a0s3_str', a0s3_str)

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
a0s5_mic.new((16, 27.6, 15), -2.98465, icm=2.7e-05, err=1.9e-03) 
a0s5_mic.new((20, 27.6, 15), -2.98595, icm=5.9e-06, err=7.4e-04) 
a0s5_mic.new((20, 32, 15)  , -2.98541, icm=4.1e-05, err=2.5e-03) 
datasets += pack_data('a0s5_mic', a0s5_mic)

a0s5_str = Data(0.00, 5e-03, 'str')
a0s5_str.new((15, 13.8, 15), -2.98601, icm=7.4e-06, err=1.4e-03) 
a0s5_str.new((15, 15, 15)  , -2.98610, icm=7.0e-03, err=3.0e-03) 
datasets += pack_data('a0s5_str', a0s5_str)

''' alpha = 0.00, sigma = 7e-03 '''
a0s7_hom = Data(0.00, 7e-03, 'hom')
a0s7_hom.new((15.2, 15.2, 15.2), -4.20224, icm=7e-06, err=4e-05)
a0s7_hom.new((18.2, 18.2, 15.2), -4.20218, icm=2e-04, err=8e-04)
datasets += pack_data('a0s7_hom', a0s7_hom)

a0s7_mic = Data(0.00, 7e-03, 'mic')
a0s7_hol = Data(0.00, 7e-03, 'hol')

''' alpha = 0.05, sigma = 5e-03 '''
a05s5_str = Data(0.05, 5e-03, 'str')
a05s5_str.new((18.2, 18.2, 36.2), -2.97413, icm=2.7e-03, err=3.9e-04)
a05s5_str.new((18.2, 24.2, 36.2), -2.97415, icm=2.8e-03, err=4.0e-04)
datasets += pack_data('a05s5_str', a05s5_str)

a05s5_hol = Data(0.05, 5e-03, 'hol')
a05s5_hol.new((20.2, 20.2, 36.2), -2.97364, icm=1.9e-03, err=2.5e-04)
datasets += pack_data('a05s5_hol', a05s5_hol)

''' alpha = 0.10, sigma = 5e-03 '''
a1s5_hol = Data(0.10, 5e-03, 'hol')
a1s5_hol.new((8, 13.8, 35)   , -2.93661, icm=9.7e-05, err=3.3e-04)
a1s5_hol.new((13.8, 13.8, 35), -2.93731, icm=1.8e-05, err=4.4e-04) 
a1s5_hol.new((15, 15, 35)    , -2.93757, icm=1.6e-04, err=4.0e-04) 
a1s5_hol.new((16, 16, 35)    , -2.93773, icm=3.1e-05, err=3.4e-04)
a1s5_hol.new((17, 17, 35)    , -2.93781, icm=4.7e-05, err=4.1e-04)
a1s5_hol.new((19, 19, 35)      , -2.93795, icm=3.9e-04, err=3.1e-04)
a1s5_hol.new((21.2, 21.2, 35)  , -2.93847, icm=3.4e-03, err=4.2e-04)
a1s5_hol.new((25.2, 25.2, 35)  , -2.93854, icm=2.7e-03, err=3.9e-04)
a1s5_hol.new((27.2, 27.2, 36.2), -2.93849, icm=3.4e-03, err=4.2e-04)
a1s5_hol.new((27.2, 29.2, 36.2), -2.93873)
a1s5_hol.new((27.2, 25.2, 36.2), -2.93850)
a1s5_hol.new((29.2, 27.2, 36.2), -2.93849)
a1s5_hol.new((25.2, 27.2, 36.2), -2.93858)
a1s5_hol.new((25.2, 30.2, 36.2), -2.93858, icm=2.9e-03, err=4.0e-04)
a1s5_hol.new((27.2, 32.2, 36.2), -2.93859)
datasets += pack_data('a1s5_hol', a1s5_hol)

a1s5_str = Data(0.10, 5e-03, 'str')
a1s5_str.new((15, 13.8, 35), -2.93758, icm=9.4e-05, err=3.6e-04)
a1s5_str.new((17, 13.8, 35), -2.93775, icm=1.8e-05, err=5.4e-04)
a1s5_str.new((15, 16, 35)  , -2.93762, icm=7.5e-05, err=2.6e-04)
a1s5_str.new((17, 16, 35)  , -2.93788, icm=1.5e-04, err=3.0e-04)
a1s5_str.new((19, 16, 35)  , -2.93755, icm=2.0e-05, err=1.1e-03)
datasets += pack_data('a1s5_str', a1s5_str)

a1s5_hom = Data(0.10, 5e-03, 'hom')
a1s5_hom.new((10, 10, 35), -2.93780, icm=3.9e-04, err=7.6e-05)
a1s5_hom.new((12, 12, 35), -2.93788, icm=9.4e-05, err=2.3e-05)
datasets += pack_data('a1s5_hom', a1s5_hom)

''' alpha = 0.20, sigma = 0.025 '''
a2s25_mul = Data(0.20, 0.025, 'mul')
a2s25_mul.new((5.2, 5.2, 70.2)  , -13.9730, icm=8.4e-03, err=2.4e-03)
a2s25_mul.new((10.2, 10.2, 70.2), -13.9744, icm=1.7e-04, err=1.7e-03)
a2s25_mul.new((15.2, 15.2, 70.2), -13.9755, icm=1.5e-04, err=1.5e-03)
datasets += pack_data('a2s25_mul', a2s25_mul)

a2s25_cyl = Data(0.20, 0.025, 'cyl')
a2s25_cyl.new((10.2, 10.2, 70.2), -14.0011, icm=1.7e-02, err=2.9e-03)
a2s25_cyl.new((13.0, 13.0, 70.2), -14.0022, icm=1.1e-02, err=1.4e-03)
a2s25_cyl.new((15.2, 15.2, 70.2), -13.9979, icm=2.7e-02, err=5.2e-03)
datasets += pack_data('a2s25_cyl', a2s25_cyl)

''' alpha = 0.20, sigma = 0.027 '''
a2s27_hom = Data(0.20, 0.027, 'hom')
a2s27_hom.new((5.2, 5.2, 70.2)  , -15.1030, icm=2.0e-06, err=2.1e-06)
a2s27_hom.new((15.2, 15.2, 70.2), -15.1048, icm=3.5e-06, err=2.2e-06)
a2s27_hom.new((20.2, 20.2, 70.2), -15.1050, icm=5.7e-07, err=2.4e-07)
datasets += pack_data('a2s27_hom', a2s27_hom)

a2s27_cyl = Data(0.20, 0.027, 'cyl')
datasets += pack_data('a2s27_cyl', a2s27_cyl)

a2s27_mul = Data(0.20, 0.027, 'mul')
datasets += pack_data('a2s27_mul', a2s27_mul)

All = All(datasets)