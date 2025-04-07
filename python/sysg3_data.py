import pandas as pd, numpy as np
from Data import Data

''' chi = 1.25, N = 200, b = 1.0, v = 4.19, T = 293 '''

class All:
    def __init__(self, datasets):
        self.all = pd.DataFrame(datasets, columns=['alpha', 'sigma', 'morph', 'done', 'name', 'n', 'data'])
        
    def show(self): 
        styler = self.all.iloc[:,:6].style \
            .format(precision=3) \
            .hide(axis='index')
        display(styler)
        
datasets = []
pack_data = lambda name, data: [(data.alpha, data.sigma, data.morph, data.done, name, len(data.data), data)]

########################################################################

''' alpha = 0.00, sigma = 3e-03 '''
a0s3_mic = Data(0.00, 3e-03, 'mic')
a0s3_mic.new((16, 27.6, 15)  , -1.77937, icm=1.9e-04, err=8.3e-04)
a0s3_mic.new((20, 27.6, 15)  , -1.77956, icm=2.6e-03, err=5.9e-04) 
a0s3_mic.new((20, 32, 15)    , -1.77930, icm=7.4e-03, err=1.7e-03) 
a0s3_mic.new((22.2, 22.2, 15), -1.77919, icm=3.4e-04, err=1.8e-03)
a0s3_mic.new((24.2, 24.2, 15), -1.77899, icm=3.0e-04, err=1.6e-03)
a0s3_mic.new((18.2,25.2,15.2), -1.77969, icm=3.3e-03, err=7.9e-04)
a0s3_mic.done = True
datasets += pack_data('a0s3_mic', a0s3_mic)

a0s3_str = Data(0.00, 3e-03, 'str')
a0s3_str.new((20.2, 20.2, 15.2), -1.77861, icm=5.9e-04, err=1.5e-04)
a0s3_str.new((25.2, 25.2, 15.2), -1.77828, icm=5.2e-03, err=1.2e-03)
a0s3_str.new((18.2, 18.2, 15.2), -1.77893, icm=7.0e-04, err=1.5e-04)
a0s3_str.new((22.2, 22.2, 15.2), -1.77817, icm=2.5e-03, err=3.1e-04)
a0s3_str.done = True
datasets += pack_data('a0s3_str', a0s3_str)

''' alpha = 0.00, sigma = 5e-03 '''
a0s5_hom = Data(0.00, 5e-03, 'hom')
a0s5_hom.new((8, 13.8, 15) , -2.98579, icm=5.5e-06, err=4.0e-04)
a0s5_hom.new((13.8,13.8,15), -2.98578, icm=2.2e-06, err=1.3e-04)
a0s5_hom.new((10.6,10.6,15), -2.98580, icm=1.0e-05, err=3.7e-05)
a0s5_hom.done = True
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
a0s5_hol.done = True
datasets += pack_data('a0s5_hol', a0s5_hol)

a0s5_mic = Data(0.00, 5e-03, 'mic')
a0s5_mic.new((16, 27.6, 15), -2.98465, icm=2.7e-05, err=1.9e-03) 
a0s5_mic.new((20, 27.6, 15), -2.98595, icm=5.9e-06, err=7.4e-04) 
a0s5_mic.new((20, 32, 15)  , -2.98541, icm=4.1e-05, err=2.5e-03) 
a0s5_mic.done = True
datasets += pack_data('a0s5_mic', a0s5_mic)

a0s5_str = Data(0.00, 5e-03, 'str')
a0s5_str.new((15, 13.8, 15), -2.98601, icm=7.4e-06, err=1.4e-03) 
a0s5_str.new((15, 15, 15)  , -2.98610, icm=7.0e-03, err=3.0e-03) 
a0s5_str.new((20, 13.8, 15), -2.98733, icm=8.9e-04, err=3.5e-04) 
a0s5_str.new((18, 13.8, 15), -2.98707, icm=2.1e-03, err=6.4e-04) 
a0s5_str.new((22, 13.8, 15), -2.98558, icm=7.8e-03, err=2.8e-03) 
a0s5_str.new((24, 13.8, 15), -2.98569, icm=5.2e-03, err=1.6e-03) 
a0s5_str.done = True
datasets += pack_data('a0s5_str', a0s5_str)

''' alpha = 0.00, sigma = 6e-03 '''
a0s6_str = Data(0.00, 6e-03, 'str')
a0s6_str.new((12.2, 20.2, 15.2), -3.58677, icm=6.1e-05, err=4.2e-03)
a0s6_str.new((15.2, 20.2, 15.2), -3.59025, icm=3.4e-04, err=2.8e-03)
a0s6_str.new((18.2, 20.2, 15.2), -3.58290, icm=3.6e-04, err=2.9e-03)
a0s6_str.done = True
datasets += pack_data('a0s6_str', a0s6_str)

a0s6_hol = Data(0.00, 6e-03, 'hol')
a0s6_hol.new((12.2, 12.2, 15.2), -3.59170, icm=4.9e-04, err=1.8e-03)
a0s6_hol.new((15.2, 15.2, 15.2), -3.59099, icm=5.4e-04, err=3.5e-03)
a0s6_hol.new((20.2, 20.2, 15.2), -3.58496, icm=2.8e-04, err=2.6e-03)
# a0s6_hol.new(( 9.2,  9.2, 15.2), ) # TODO, Josh
datasets += pack_data('a0s6_hol', a0s6_hol)

a0s6_hom = Data(0.00, 6e-03, 'hom')
# TODO, TJY start from 1D
datasets += pack_data('a0s6_hom', a0s6_hom)

''' alpha = 0.00, sigma = 7e-03 '''
a0s7_hom = Data(0.00, 7e-03, 'hom')
a0s7_hom.new((15.2, 15.2, 15.2), -4.20224, icm=7e-06, err=4e-05)
a0s7_hom.new((18.2, 18.2, 15.2), -4.20218, icm=2e-04, err=8e-04)
a0s7_hom.done = True
datasets += pack_data('a0s7_hom', a0s7_hom)

a0s7_hol = Data(0.00, 7e-03, 'hol')
a0s7_hol.new((20.2, 20.2, 15.2), -4.20077, icm=1.0e-02, err=2.7e-03)
a0s7_hol.new((21.2, 21.2, 15.2), -4.20075, icm=1.1e-03, err=1.9e-03)
a0s7_hol.new((24.2, 24.2, 15.2), -4.20090, icm=1.9e-02, err=3.2e-03)
a0s7_hol.done = True
datasets += pack_data('a0s7_hol', a0s7_hol)

########################################################################

''' alpha = 0.05, sigma = 3e-03 '''
a05s3_mic = Data(0.05, 3e-03, 'mic')
a05s3_mic.new((18.2, 25.2, 36.2), -1.77283, icm=6.1e-04, err=1.1e-04)
a05s3_mic.new((16.2, 27.2, 36.2), -1.77262, icm=7.2e-03, err=1.0e-03)
a05s3_mic.new((20.2, 36.2, 36.2), -1.77111, icm=4.6e-02, err=3.5e-03)
datasets += pack_data('a05s3_mic', a05s3_mic)

a05s3_hol = Data(0.05, 3e-03, 'hol')
a05s3_hol.new((21.8, 21.8, 36.2), -1.76958, icm=2.9e-02, err=3.0e-03)
a05s3_hol.new((18.2, 18.2, 36.2), -1.77005, icm=1.1e-02, err=1.5e-03)
a05s3_hol.new((15.2, 15.2, 36.2), -1.76994, icm=1.5e-02, err=3.0e-03)
a05s3_hol.done = True
datasets += pack_data('a05s3_hol', a05s3_hol)

a05s3_str = Data(0.05, 3e-03, 'str')
a05s3_str.new((20.2, 24.2, 36.2), -1.77178, icm=1.2e-03, err=2.4e-04)
a05s3_str.new((18.2, 24.2, 36.2), -1.77213, icm=3.0e-03, err=5.6e-04)
a05s3_str.new((21.8, 24.2, 36.2), -1.77142, icm=2.3e-03, err=4.3e-04)
a05s3_str.new((16.2, 24.2, 36.2), -1.77232, icm=3.0e-03, err=5.2e-04)
a05s3_str.new((13.0, 24.2, 36.2), -1.77202, icm=2.9e-03, err=4.4e-04)
a05s3_str.done = True
datasets += pack_data('a05s3_str', a05s3_str)

''' alpha = 0.05, sigma = 5e-03 '''
a05s5_str = Data(0.05, 5e-03, 'str')
a05s5_str.new((18.2, 18.2, 36.2), -2.97413, icm=2.7e-03, err=3.9e-04)
a05s5_str.new((18.2, 24.2, 36.2), -2.97415, icm=2.8e-03, err=4.0e-04)
a05s5_str.new((16.2, 24.2, 36.2), -2.97378, icm=2.9e-03, err=5.9e-04)
a05s5_str.new((20.2, 24.2, 36.2), -2.97422, icm=5.4e-03, err=1.0e-03)
a05s5_str.new((24.2, 24.2, 36.2), -2.97385, icm=1.2e-02, err=2.1e-03)
a05s5_str.done = True
datasets += pack_data('a05s5_str', a05s5_str)

a05s5_hol = Data(0.05, 5e-03, 'hol')
a05s5_hol.new((20.2, 20.2, 36.2), -2.97364, icm=1.9e-03, err=2.5e-04)
a05s5_hol.new((18.2, 18.2, 36.2), -2.97350, icm=4.8e-03, err=5.4e-04)
a05s5_hol.new((21.8, 21.8, 36.2), -2.97365, icm=1.0e-02, err=5.1e-04)
a05s5_hol.new((24.2, 24.2, 36.2), -2.97360, icm=5.5e-03, err=5.6e-04)
a05s5_hol.done = True
datasets += pack_data('a05s5_hol', a05s5_hol)

a05s5_mic = Data(0.05, 5e-03, 'mic')
a05s5_mic.new((16.2, 27.2, 36.2), -2.97229, icm=8.2e-03, err=8.9e-04)
a05s5_mic.new((20.2, 36.2, 36.2), -2.97223, icm=2.8e-02, err=3.7e-03)
a05s5_mic.new((21.8, 21.8, 36.2), -2.97379, icm=1.2e-02, err=2.9e-03)
a05s5_mic.new((25.2, 25.2, 36.2), -2.97282, icm=2.6e-02, err=4.0e-03)
datasets += pack_data('a05s5_mic', a05s5_mic)

########################################################################

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
a1s5_hol.done = True
datasets += pack_data('a1s5_hol', a1s5_hol)

a1s5_str = Data(0.10, 5e-03, 'str')
a1s5_str.new((15, 13.8, 35), -2.93758, icm=9.4e-05, err=3.6e-04)
a1s5_str.new((17, 13.8, 35), -2.93775, icm=1.8e-05, err=5.4e-04)
a1s5_str.new((15, 16, 35)  , -2.93762, icm=7.5e-05, err=2.6e-04)
a1s5_str.new((17, 16, 35)  , -2.93788, icm=1.5e-04, err=3.0e-04)
a1s5_str.new((19, 16, 35)  , -2.93755, icm=2.0e-05, err=1.1e-03)
a1s5_str.done = True
datasets += pack_data('a1s5_str', a1s5_str)

a1s5_hom = Data(0.10, 5e-03, 'hom')
a1s5_hom.new((10, 10, 35), -2.93780, icm=3.9e-04, err=7.6e-05)
a1s5_hom.new((12, 12, 35), -2.93788, icm=9.4e-05, err=2.3e-05)
a1s5_hom.done = True
datasets += pack_data('a1s5_hom', a1s5_hom)

########################################################################

''' alpha = 0.20, sigma = 0.005 '''
a2s05_mic = Data(0.20, 0.005, 'mic')
a2s05_mic.new((16.2, 16.2, 48.2), -2.81601, icm=6.1e-02, err=5.0e-03)
a2s05_mic.new((20.2, 20.2, 54.2), -2.81578, icm=3.9e-02, err=5.4e-03)
a2s05_mic.new((24.2, 24.2, 54.2), -2.81520, icm=6.1e-02, err=7.0e-03)
a2s05_mic.new((12.2, 12.2, 48.2), -2.81948, icm=3.0e-02, err=4.3e-03)
a2s05_mic.new((10.2, 10.2, 54.2), -2.82020, icm=2.0e-02, err=1.9e-03)
a2s05_mic.new(( 8.2,  8.2, 54.2), -2.81967, icm=1.4e-02, err=2.5e-03)
datasets += pack_data('a2s05_mic', a2s05_mic)

''' alpha = 0.20, sigma = 0.015 '''
a2s15_str = Data(0.20, 0.015, 'str')
a2s15_str.new((10.2, 15.2, 64.2), -8.43398, icm=8.8e-03, err=1.7e-03)
a2s15_str.new((10.2, 10.2, 64.2), -8.43538, icm=9.2e-03, err=1.7e-03)
datasets += pack_data('a2s15_str', a2s15_str)

a2s15_cyl = Data(0.20, 0.015, 'cyl')
a2s15_cyl.new((12.2, 12.2, 64.2), -8.43694, icm=3.0e-02, err=2.8e-03)
a2s15_cyl.new((10.2, 10.2, 64.2), -8.43882, icm=3.3e-02, err=2.3e-03)
a2s15_cyl.new(( 8.2,  8.2, 64.2), -8.43926, icm=7.5e-03, err=1.3e-03)
datasets += pack_data('a2s15_cyl', a2s15_cyl)

''' alpha = 0.20, sigma = 0.022 '''
a2s22_cyl = Data(0.20, 0.022, 'cyl')
a2s22_cyl.new((10.2, 10.2, 64.2), -12.3420, icm=1.5e-02, err=1.1e-03)
a2s22_cyl.new((12.2, 12.2, 64.2), -12.3394, icm=3.2e-02, err=4.3e-03)
datasets += pack_data('a2s22_cyl', a2s22_cyl)

a2s22_str = Data(0.20, 0.022, 'str')
a2s22_str.new((13.0, 15.2, 64.2), -12.3424, icm=9.7e-03, err=1.5e-03)
a2s22_str.new((12.2, 15.2, 64.2), -12.3426, icm=5.9e-03, err=8.3e-04)
a2s22_str.new((13.0, 15.2, 64.2), -12.3427, icm=4.1e-03, err=1.5e-03)
datasets += pack_data('a2s22_str', a2s22_str)

''' alpha = 0.20, sigma = 0.025 '''
a2s25_mul = Data(0.20, 0.025, 'mul')
a2s25_mul.new((5.2, 5.2, 70.2)  , -13.9730, icm=8.4e-03, err=2.4e-03)
a2s25_mul.new((10.2, 10.2, 70.2), -13.9744, icm=1.7e-04, err=1.7e-03)
a2s25_mul.new((15.2, 15.2, 70.2), -13.9755, icm=1.5e-04, err=1.5e-03)
a2s25_mul.done = True
datasets += pack_data('a2s25_mul', a2s25_mul)

a2s25_cyl = Data(0.20, 0.025, 'cyl')
a2s25_cyl.new((10.2, 10.2, 70.2), -14.0011, icm=1.7e-02, err=2.9e-03)
a2s25_cyl.new((13.0, 13.0, 70.2), -14.0022, icm=1.1e-02, err=1.4e-03)
# a2s25_cyl.new((15.2, 15.2, 70.2), -13.9979, icm=2.7e-02, err=5.2e-03)
a2s25_cyl.new((14.6, 13.0, 60.2), -14.0024, icm=1.1e-02, err=1.3e-03)
a2s25_cyl.new((16.2, 27.2, 60.2), -14.0021, icm=2.1e-02, err=3.2e-03)
a2s25_cyl.new((15.2, 20.2, 60.2), -14.0021, icm=1.6e-02, err=2.4e-03)
a2s25_cyl.new((17.2, 20.2, 60.2), -14.0023, icm=1.2e-02, err=1.7e-03)
a2s25_cyl.new((15.2, 18.2, 60.2), -14.0024, icm=1.5e-02, err=2.1e-03)
a2s25_cyl.new((17.2, 18.2, 60.2), -14.0026, icm=1.1e-02, err=1.4e-03)
a2s25_cyl.new((15.2, 16.2, 60.2), -14.0028, icm=8.5e-03, err=1.2e-03)
a2s25_cyl.done = True
datasets += pack_data('a2s25_cyl', a2s25_cyl)

a2s25_str = Data(0.20, 0.025, 'str')
a2s25_str.new((15.2, 10.2, 70.2), -13.9952, icm=5.0e-02, err=6.2e-03)
a2s25_str.new((15.2, 15.2, 60.2), -14.0001, icm=3.1e-02, err=4.9e-03)
a2s25_str.new((18.2, 15.2, 60.2), -14.0002, icm=2.8e-02, err=4.7e-03)
a2s25_str.new((13.0, 15.2, 60.2), -14.0019, icm=1.5e-02, err=2.3e-03)
a2s25_str.new((11.0, 15.2, 60.2), -14.0028, icm=6.5e-03, err=1.4e-03)
a2s25_str.new(( 9.2, 15.2, 60.2), -14.0027, icm=1.1e-03, err=2.4e-04)
a2s25_str.new((10.2, 15.2, 60.2), -14.0028, icm=5.2e-04, err=1.3e-04)
a2s25_str.done = True
datasets += pack_data('a2s25_str', a2s25_str)

a2s25_hom = Data(0.20, 0.025, 'hom')
a2s25_hom.new((20.2, 20.2, 60.2), -14.0033, icm=4.8e-06, err=1.8e-06)
a2s25_hom.done = True
datasets += pack_data('a2s25_hom', a2s25_hom)

''' alpha = 0.20, sigma = 0.027 '''
a2s27_hom = Data(0.20, 0.027, 'hom')
a2s27_hom.new((5.2, 5.2, 70.2)  , -15.1030, icm=2.0e-06, err=2.1e-06)
a2s27_hom.new((15.2, 15.2, 70.2), -15.1048, icm=3.5e-06, err=2.2e-06)
a2s27_hom.new((20.2, 20.2, 70.2), -15.1050, icm=5.7e-07, err=2.4e-07)
a2s27_hom.done = True
datasets += pack_data('a2s27_hom', a2s27_hom)

a2s27_str = Data(0.20, 0.027, 'str')
a2s27_str.new((13.0, 15.2, 70.2), -15.1044, icm=1.1e-02, err=1.8e-03)
a2s27_str.new((15.2, 15.2, 70.2), -15.1046, icm=5.6e-03, err=8.9e-04)
a2s27_str.new((18.2, 15.2, 70.2), -15.1047, icm=5.1e-03, err=1.4e-03)
a2s27_str.new((20.2, 15.2, 70.2), -15.1029, icm=2.4e-02, err=3.4e-03)
a2s27_str.done = True
datasets += pack_data('a2s27_str', a2s27_str)

a2s27_cyl = Data(0.20, 0.027, 'cyl')
a2s27_cyl.new((15.2, 15.2, 70.2), -15.1039, icm=1.6e-02, err=1.8e-03)
a2s27_cyl.new((13.0, 13.0, 70.2), -15.1042, icm=7.9e-03, err=1.3e-03)
a2s27_cyl.new((18.2, 18.2, 70.2), -15.1042, icm=8.3e-03, err=1.5e-03)
a2s27_cyl.new((11.0, 11.0, 70.2), -15.1041, icm=7.4e-03, err=9.4e-04)
a2s27_cyl.new((15.2, 21.2, 70.2), -15.1046, icm=9.4e-03, err=1.2e-03)
a2s27_cyl.new((15.2, 17.6, 70.2), -15.1042, icm=8.8e-03, err=1.2e-03)
a2s27_cyl.new((17.6, 21.2, 70.2), -15.1046, icm=1.0e-02, err=1.3e-03)
a2s27_cyl.new((15.2, 24.2, 70.2), -15.1049, icm=7.5e-03, err=9.5e-04)
a2s27_cyl.new((17.6, 24.2, 70.2), -15.1047, icm=7.7e-03, err=1.1e-03)
a2s27_cyl.done = True
datasets += pack_data('a2s27_cyl', a2s27_cyl)

a2s27_mul = Data(0.20, 0.027, 'mul')
a2s27_mul.new((10.2, 10.2, 70.2), -15.0886, icm=2.0e-02, err=9.8e-03)
a2s27_mul.new((15.2, 15.2, 70.2), -15.0898, icm=1.8e-03, err=8.8e-03)
a2s27_mul.done = True
datasets += pack_data('a2s27_mul', a2s27_mul)

########################################################################

''' alpha = 0.25, sigma = 0.027 '''
a25s27_cyl = Data(0.25, 0.027, 'cyl')
a25s27_cyl.new((15.2, 21.2, 81.2), -14.6053, icm=1.6e-02, err=3.6e-03)
a25s27_cyl.new((15.2, 17.6, 64.2), -14.6022, icm=8.6e-03, err=7.6e-04)
datasets += pack_data('a25s27_cyl', a25s27_cyl)

a25s27_str = Data(0.25, 0.027, 'str')
a25s27_str.new((13.0, 15.2, 81.2), -14.6017, icm=1.2e-03, err=1.9e-04)
a25s27_str.new((15.2, 15.2, 64.2), -14.6016, icm=2.5e-03, err=5.7e-04)
a25s27_str.new((18.2, 15.2, 64.2), -14.6016, icm=3.0e-03, err=1.1e-03)
a25s27_str.new((11.0, 15.2, 64.2), -14.6014, icm=4.4e-03, err=6.8e-04)
datasets += pack_data('a25s27_str', a25s27_str)

a25s27_hom = Data(0.25, 0.027, 'hom')
a25s27_hom.new((15.2, 15.2, 81.2), -14.6015, icm=1.4e-04, err=4.0e-05)
a25s27_hom.done = True
datasets += pack_data('a25s27_hom', a25s27_hom)

a25s27_mul = Data(0.25, 0.027, 'mul')
# Unstable
a25s27_mul.done = True
datasets += pack_data('a25s27_mul', a25s27_mul)

''' alpha = 0.25, sigma = 0.030 '''
a25s3_hom = Data(0.25, 0.030, 'hom')
a25s3_hom.new((15.2, 15.2, 64.2), -16.1894, icm=1.9e-02, err=6.6e-03)
a25s3_hom.done=True
datasets += pack_data('a25s3_hom', a25s3_hom)

a25s3_mul = Data(0.25, 0.030, 'mul')
# Unstable
a25s3_mul.done=True
datasets += pack_data('a25s3_mul', a25s3_mul)

########################################################################

''' alpha = 0.30, sigma = 0.020 '''
a3s2_str = Data(0.30, 0.020, 'str')
a3s2_str.new((13.0, 15.2, 64.2), -10.4828, icm=3.1e-02, err=7.1e-03)
a3s2_str.new((15.2, 15.2, 64.2), -10.4878, icm=2.1e-02, err=5.4e-03)
a3s2_str.new((18.2, 15.2, 64.2), -10.4855, icm=2.0e-02, err=4.7e-03)
a3s2_str.done = True
datasets += pack_data('a3s2_str', a3s2_str)

a3s2_mul = Data(0.30, 0.020, 'mul')
a3s2_mul.new((15.2, 15.2, 64.2), -10.4794, icm=1.2e-03, err=5.3e-04)
a3s2_mul.done = True
datasets += pack_data('a3s2_mul', a3s2_mul)

''' alpha = 0.30, sigma = 0.025 '''
a3s25_hom = Data(0.30, 0.025, 'hom')
a3s25_hom.new((15.2, 15.2, 64.2), -13.0394, icm=2.2e-06, err=8.1e-07)
a3s25_hom.done = True
datasets += pack_data('a3s25_hom', a3s25_hom)

a3s25_str = Data(0.30, 0.025, 'str')
a3s25_str.new((13.0, 15.2, 64.2), -13.0500, icm=3.1e-02, err=5.4e-03)
a3s25_str.new((15.2, 15.2, 64.2), -13.0538, icm=2.9e-02, err=4.7e-03)
datasets += pack_data('a3s25_str', a3s25_str)

a3s25_mul = Data(0.30, 0.025, 'mul')
# Unstable
datasets += pack_data('a3s25_mul', a3s25_mul)

All = All(datasets)