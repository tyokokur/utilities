import pandas as pd, numpy as np
from Data import Data

''' chi = 1.25, N = 200, b = 1.0, v = 4.19, T = 293 '''

class All:
    def __init__(self, datasets):
        self.all = pd.DataFrame(datasets, columns=['alpha', 'sigma', 'morph', 'done', 'multi', 'name', 'n', 'data'])
        
    def show(self): 
        styler = self.all.iloc[:,:6].style \
            .format(precision=3) \
            .hide(axis='index')
        display(styler)
        
datasets = []
pack_data = lambda name, data: [(data.alpha, data.sigma, data.morph, data.done, data.multi, name, len(data.data), data)]

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

a0s5_hol = Data(0.00, 5e-03, 'str')
a0s5_hol.new((8, 13.8, 15)   , -2.98419, icm=3.2e-06, err=4.0e-04)
a0s5_hol.new((13.8, 13.8, 15), -2.98544, icm=1.1e-05, err=4.5e-04)
a0s5_hol.new((15, 15,15)     , -2.98573, icm=2.1e-04, err=6.7e-04)
a0s5_hol.new((16, 16,15)     , -2.98602, icm=5.5e-05, err=1.8e-04)
a0s5_hol.new((17, 17,15)     , -2.98620, icm=6.8e-05, err=2.0e-04)
a0s5_hol.new((19, 19,15)     , -2.98637, icm=1.2e-05, err=5.6e-04)
a0s5_hol.new((21, 21,15)     , -2.98639, icm=2.4e-04, err=7.5e-04)
a0s5_hol.new((23, 23,15)     , -2.98644, icm=7.1e-05, err=7.3e-04)
a0s5_hol.done = True
a0s5_hol.hole = True
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
# (11, 11) unstable
a0s6_hol.new((12.2, 12.2, 15.2), -3.59170, icm=4.9e-04, err=1.8e-03)
a0s6_hol.new((15.2, 15.2, 15.2), -3.59099, icm=5.4e-04, err=3.5e-03)
a0s6_hol.new((20.2, 20.2, 15.2), -3.58496, icm=2.8e-04, err=2.6e-03)
a0s6_hol.done = True
datasets += pack_data('a0s6_hol', a0s6_hol)

a0s6_hom = Data(0.00, 6e-03, 'hom')
a0s6_hom.new((20.2, 20.2, 15.2), -3.59404, icm=2.2e-07, err=1.2e-07)
a0s6_hom.done = True
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
a05s3_mic.done = True
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
a05s5_mic.done = True # Unsure, but don't want to waste time
datasets += pack_data('a05s5_mic', a05s5_mic)

''' alpha = 0.05, sigma = 6e-03 '''
a05s6_str = Data(0.05, 6e-03, 'str')
a05s6_str.new((19.2, 24.2, 36.2), -3.57621, icm=8.3e-03, err=1.5e-03)
a05s6_str.new((21.2, 24.2, 36.2), -3.57664, icm=6.5e-03, err=1.2e-03)
a05s6_str.new((24.2, 24.2, 36.2), -3.57642, icm=1.0e-02, err=2.4e-03)
a05s6_str.new((26.2, 24.2, 36.2), -3.57625, icm=1.4e-02, err=2.9e-03)
a05s6_str.done=True
datasets += pack_data('a05s6_str', a05s6_str)

a05s6_hol = Data(0.05, 6e-03, 'hol')
a05s6_hol.new((18.2, 18.2, 36.2), -3.57716, icm=1.7e-02, err=1.1e-03)
a05s6_hol.new((20.2, 20.2, 36.2), -3.57724, icm=4.1e-03, err=3.8e-04)
a05s6_hol.new((21.8, 21.8, 36.2), -3.57720, icm=1.1e-02, err=8.4e-04)
a05s6_hol.new((20.2, 24.2, 36.2), -3.57732, icm=8.6e-03, err=7.9e-04)
a05s6_hol.new((20.2, 27.2, 36.2), -3.57732, icm=1.1e-02, err=6.5e-04)
datasets += pack_data('a05s6_hol', a05s6_hol)

a05s6_hom = Data(0.05, 6e-03, 'hom')
a05s6_hom.new((20.2, 20.2, 36.2), -3.57783, icm = 2.6e-06, err=1.1e-06)
a05s6_hom.done = True
datasets += pack_data('a05s6_hom', a05s6_hom)

''' alpha = 0.05, sigma = 7e-03 '''
a05s7_str = Data(0.05, 7e-03, 'str')
a05s7_str.new((24.2, 24.2, 36.2), -4.17944, icm=8.1e-03, err=1.6e-03)
a05s7_str.new((21.2, 24.2, 36.2), -4.18090, icm=2.8e-02, err=3.8e-03)
a05s7_str.done = True
datasets += pack_data('a05s7_str', a05s7_str)

a05s7_hol = Data(0.05, 7e-03, 'hol')
a05s7_hol.new((21.8, 21.8, 36.2), -4.18116, icm=1.7e-02, err=1.2e-03)
a05s7_hol.done = True # unless 6e-03 hol is minF 
datasets += pack_data('a05s7_hol', a05s7_hol)

a05s7_hom = Data(0.05, 7e-03, 'hom')
a05s7_hom.new((20.2, 20.2, 36.2), -4.18226, icm=5.6e-06, err=3.0e-06)
a05s7_hom.done = True
datasets += pack_data('a05s7_hom', a05s7_hom)

########################################################################

''' alpha = 0.10, sigma = 2.5e-03 '''
a1s25_mic = Data(0.10, 2.5e-03, 'mic')
a1s25_mic.new((18.2, 25.2, 36.2), -1.45857, icm=5.1e-03, err=5.7e-04)
a1s25_mic.new((18.2, 27.2, 36.2), -1.45769, icm=2.1e-03, err=2.5e-04)
a1s25_mic.new((22.2, 25.2, 36.2), -1.45723, icm=3.2e-03, err=4.0e-03)
datasets += pack_data('a1s25_mic', a1s25_mic)

a1s25_str = Data(0.10, 2.5e-03, 'str')
a1s25_str.new((14.2, 16.2, 36.2), -1.45840, icm=2.7e-03, err=4.1e-04)
a1s25_str.new((17.2, 16.2, 36.2), -1.45789, icm=8.2e-04, err=8.7e-05)
a1s25_str.new((20.2, 16.2, 36.2), -1.45715, icm=1.2e-03, err=2.1e-04)
datasets += pack_data('a1s25_str', a1s25_str)

a1s25_hol = Data(0.10, 2.5e-03, 'hol')
a1s25_hol.new((27.2, 27.2, 36.2), -1.45357, icm=5.2e-02, err=5.4e-03)
a1s25_hol.new((27.2, 29.2, 36.2), -1.45337, icm=5.7e-02, err=5.4e-03)
a1s25_hol.new((29.2, 29.2, 36.2), -1.45274, icm=6.3e-02, err=5.6e-03)
a1s25_hol.new((32.2, 32.2, 36.2), -1.45276, icm=6.0e-02, err=6.7e-03)
a1s25_hol.done = True # not likely
datasets += pack_data('a1s25_hol', a1s25_hol)

''' alpha = 0.10, sigma = 5e-03 '''
a1s5_pn  = Data(0.10, 5e-03, 'mic')
a1s5_pn.new((19.0, 19.0, 40.2), -2.93679, icm=7.7e-03, err=1.3e-03)
a1s5_pn.new((19.0, 21.2, 40.2), -2.93703, icm=6.0e-03, err=1.0e-03)
a1s5_pn.new((19.0, 24.2, 40.2), -2.93698, icm=1.4e-02, err=1.7e-03)
datasets += pack_data('a1s5_pn', a1s5_pn)

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
a1s5_hol.new((27.2, 29.2, 40.2), -2.93858, icm=1.0e-03, err=1.4e-04)
a1s5_hol.new((27.2, 25.2, 36.2), -2.93850)
a1s5_hol.new((29.2, 27.2, 36.2), -2.93849)
a1s5_hol.new((25.2, 27.2, 36.2), -2.93858)
a1s5_hol.new((25.2, 30.2, 36.2), -2.93858, icm=2.9e-03, err=4.0e-04)
a1s5_hol.new((27.2, 32.2, 36.2), -2.93859, icm=3.2e-03, err=4.4e-04)
a1s5_hol.done = True
datasets += pack_data('a1s5_hol', a1s5_hol)

a1s5_str = Data(0.10, 5e-03, 'str')
# a1s5_str.new((15, 13.8, 35), -2.93758, icm=9.4e-05, err=3.6e-04)
# a1s5_str.new((17, 13.8, 35), -2.93775, icm=1.8e-05, err=5.4e-04)
# a1s5_str.new((15, 16, 35)  , -2.93762, icm=7.5e-05, err=2.6e-04)
a1s5_str.new((15.2, 20.2, 40.2), -2.93819, icm=2.3e-03, err=3.1e-04)
a1s5_str.new((17.6, 20.2, 40.2), -2.93844, icm=4.4e-03, err=5.6e-04)
a1s5_str.new((18.2, 20.2, 40.2), -2.93850, icm=2.4e-03, err=3.1e-04)
a1s5_str.new((19.0, 20.2, 40.2), -2.93851, icm=5.7e-05, err=2.7e-04)
a1s5_str.new((20.2, 20.2, 40.2), -2.93849, icm=8.5e-05, err=4.1e-04)
a1s5_str.done = True
datasets += pack_data('a1s5_str', a1s5_str)

a1s5_hom = Data(0.10, 5e-03, 'hom')
a1s5_hom.new((10, 10, 35), -2.93780, icm=3.9e-04, err=7.6e-05)
a1s5_hom.new((12, 12, 35), -2.93788, icm=9.4e-05, err=2.3e-05)
a1s5_hom.done = True
datasets += pack_data('a1s5_hom', a1s5_hom)

''' alpha = 0.10, sigma = 7.5e-03 '''
a1s75_hol = Data(0.10, 7.5e-03, 'hol')
a1s75_hol.new((24.2, 24.2, 48.2), -4.42384, icm=4.5e-02, err=2.0e-03)
a1s75_hol.new((24.2, 26.2, 48.2), -4.42388, icm=5.4e-02, err=2.9e-03)
a1s75_hol.new((26.2, 26.2, 48.2), -4.42399, icm=5.3e-02, err=2.7e-03)
a1s75_hol.new((27.2, 27.2, 48.2), -4.42413, icm=1.3e-03, err=8.1e-04)
a1s75_hol.new((27.2, 30.2, 48.2), -4.42374, icm=2.0e-03, err=8.4e-04)
a1s75_hol.new((30.2, 27.2, 48.2), -4.42429, icm=2.3e-02, err=1.1e-03)
# a1s75_hol.new((30.2, 32.2, 36.2), -4.42392, icm=6.4e-02, err=2.6e-03)
datasets += pack_data('a1s75_hol', a1s75_hol)

a1s75_hom = Data(0.10, 7.5e-03, 'hom')
a1s75_hom.new((20.2, 20.2, 48.2), -4.42466, icm=3.2e-07, err=1.2e-07)
a1s75_hom.done = True
datasets += pack_data('a1s75_hom', a1s75_hom)

''' alpha = 0.10, sigma = 1e-02 '''
a1s2_str = Data(0.10, 1e-02, 'str')
a1s2_str.new((16.2, 10.2, 36.2), -5.90844, icm=1.5e-02, err=3.0e-03)
a1s2_str.new((20.2, 14.2, 36.2), -5.90885, icm=1.7e-02, err=2.3e-03)
a1s2_str.new((22.2, 20.2, 36.2), -5.90897, icm=1.7e-02, err=2.1e-03)
a1s2_str.new((24.2, 18.2, 36.2), -5.90899, icm=1.6e-02, err=2.1e-03)
a1s2_str.new((26.2, 20.2, 36.2), -5.90831, icm=2.6e-02, err=3.3e-03)
a1s2_str.done = True
datasets += pack_data('a1s2_str', a1s2_str)

a1s2_hol = Data(0.10, 1e-02, 'hol')
# Unstable
a1s2_hol.done = True 
datasets += pack_data('a1s2_hol', a1s2_hol)

a1s2_hom = Data(0.10, 1e-02, 'hom')
a1s2_hom.new((20.2, 20.2, 36.2), -5.90938, icm=4.9e-06, err=2.9e-06)
a1s2_hom.done = True
datasets += pack_data('a1s2_hom', a1s2_hom)

########################################################################

''' alpha = 0.15, sigma = 0.005 '''
a15s05_mic = Data(0.15, 0.005, 'mic')
a15s05_mic.new((10.2, 10.2, 54.2), -2.88236, icm=2.9e-02, err=3.3e-03)
a15s05_mic.new((13.2, 13.2, 54.2), -2.88507, icm=1.3e-02, err=1.1e-03) # probably hole
datasets += pack_data('a15s05_mic', a15s05_mic)

a15s05_str = Data(0.15, 0.005, 'str')
a15s05_str.new((17.2, 16.2, 54.2), -2.88591, icm=6.9e-03, err=9.3e-04)
a15s05_str.new((20.2, 16.2, 54.2), -2.88574, icm=1.1e-02, err=1.5e-03)
datasets += pack_data('a15s05_str', a15s05_str)

a15s05_str2 = Data(0.15, 0.005, 'str') # melted
a15s05_str2.new((20.2, 15.2, 54.2), -2.88482, icm=2.0e-02, err=3.7e-03)
datasets += pack_data('a15s05_str2', a15s05_str2)

a15s05_hol = Data(0.15, 0.005, 'hol')
a15s05_hol.new((27.2, 29.2, 54.2), -2.88653, icm=1.4e-02, err=1.7e-03)
datasets += pack_data('a15s05_hol', a15s05_hol)

''' alpha = 0.15, sigma = 0.010 '''
a15s1_mic = Data(0.15, 0.010, 'mic')
a15s1_mic.new((10.2, 10.2, 54.2), -5.78462, icm=2.5e-02, err=2.6e-03)
a15s1_mic.new((13.2, 13.2, 54.2), -5.78550, icm=9.8e-03, err=1.1e-03)
datasets += pack_data('a15s1_mic', a15s1_mic)

a15s1_str= Data(0.15, 0.010, 'str') #melted
a15s1_str.new((17.2, 16.2, 54.2), -5.78283, icm=8.8e-02, err=5.0e-03) # single
# a15s1_str.new((20.2, 15.2, 54.2), -5.78487, icm=2.0e-02, err=2.6e-03) # double 
a15s1_str.new((20.2, 16.2, 54.2), -5.78568, icm=7.7e-03, err=1.0e-03) # single
# a15s1_str.new((22.2, 15.2, 54.2), -5.78551, icm=1.4e-02, err=1.3e-03) # double
datasets += pack_data('a15s1_str', a15s1_str)

a15s1_hom = Data(0.15, 0.010, 'hom')
a15s1_hom.new((15.2, 15.2, 54.2), -5.78574, icm=6.6e-03, err=6.5e-04)
a15s1_hom.new((22.2, 16.2, 54.2), -5.78573, icm=4.7e-03, err=7.6e-04)
a15s1_hom.done = True
datasets += pack_data('a15s1_hom', a15s1_hom)

########################################################################

''' alpha = 0.20, sigma = 0.005 '''
a2s05_hol = Data(0.20, 0.005, 'mic')
a2s05_hol.new((16.2, 16.2, 48.2), -2.89601, icm=6.1e-02, err=5.0e-03)
a2s05_hol.new((20.2, 20.2, 54.2), -2.81578, icm=3.9e-02, err=5.4e-03)
a2s05_hol.new((24.2, 24.2, 54.2), -2.81520, icm=6.1e-02, err=7.0e-03)
a2s05_hol.new((12.2, 12.2, 48.2), -2.81948, icm=3.0e-02, err=4.3e-03)
a2s05_hol.new((10.2, 10.2, 54.2), -2.82020, icm=2.0e-02, err=1.9e-03)
a2s05_hol.new(( 8.2,  8.2, 54.2), -2.81967, icm=1.4e-02, err=2.5e-03)
a2s05_hol.done = True
datasets += pack_data('a2s05_hol', a2s05_hol)

''' alpha = 0.20, sigma = 0.015 '''
a2s15_cyl = Data(0.20, 0.015, 'cyl')
a2s15_cyl.new((12.2, 12.2, 64.2), -8.43694, icm=3.0e-02, err=2.8e-03)
a2s15_cyl.new((10.2, 10.2, 64.2), -8.43882, icm=3.3e-02, err=2.3e-03)
a2s15_cyl.new(( 8.2,  8.2, 64.2), -8.43926, icm=7.5e-03, err=1.3e-03)
a2s15_cyl.new(( 8.2,  7.4, 64.2), -8.43930, icm=7.6e-03, err=1.0e-03)
a2s15_cyl.new(( 7.4,  7.4, 64.2), -8.43919, icm=1.1e-02, err=1.6e-03)
a2s15_cyl.done = True
datasets += pack_data('a2s15_cyl', a2s15_cyl)

a2s15_str = Data(0.20, 0.015, 'str')
a2s15_str.new((10.2, 15.2, 64.2), -8.43398, icm=8.8e-03, err=1.7e-03)
a2s15_str.new((12.2, 15.2, 64.2), -8.43538, icm=9.2e-03, err=1.7e-03)
a2s15_str.new((13.0, 15.2, 64.2), -8.43620, icm=5.8e-03, err=1.2e-03)
a2s15_str.new((15.2, 15.2, 64.2), -8.43689, icm=6.8e-03, err=1.2e-03)
a2s15_str.new((18.2, 15.2, 64.2), -8.43770, icm=4.4e-03, err=6.9e-04)
a2s15_str.new((20.2, 15.2, 64.2), -8.43806, icm=3.7e-03, err=5.3e-04)
a2s15_str.new((24.2, 20.2, 64.2), -8.43879, icm=4.7e-03, err=6.5e-04)
a2s15_str.new((27.2, 20.2, 64.2), -8.43902, icm=4.3e-03, err=8.4e-04)
a2s15_str.new((30.2, 20.2, 64.2), -8.43929, icm=4.6e-03, err=8.6e-04)
a2s15_str.new((32.2, 20.2, 64.2), -8.43935, icm=3.6e-03, err=7.5e-04)
a2s15_str.multi = True
a2s15_str.done = True # Called for the sake of memory
datasets += pack_data('a2s15_str', a2s15_str)

a2s15_mic = Data(0.20, 0.015, 'mic')
a2s15_mic.new((20.2, 20.2, 64.2), -8.43841, icm=3.5e-02, err=3.9e-03)
a2s15_mic.new((18.2, 18.2, 64.2), -8.43899, icm=2.1e-02, err=3.1e-03)
a2s15_mic.new((16.2, 16.2, 64.2), -8.43912, icm=1.8e-02, err=2.7e-03)
a2s15_mic.new((24.2, 24.2, 64.2), -8.43855, icm=1.7e-02, err=3.1e-03)
a2s15_mic.new((16.2, 18.2, 64.2), -8.43956, icm=1.2e-02, err=1.7e-03)
a2s15_mic.new((16.2, 14.6, 64.2), -8.43935, icm=1.5e-02, err=2.2e-03)
a2s15_mic.done = True
datasets += pack_data('a2s15_mic', a2s15_mic)

''' alpha = 0.20, sigma = 0.0175 '''
a2s175_mic = Data(0.20, 0.0175, 'mic')
a2s175_mic.new((16.2, 20.2, 64.2), -9.83770, icm=8.6e-03, err=1.3e-03)
a2s175_mic.new((18.2, 20.2, 64.2), -9.83777, icm=8.5e-03, err=1.4e-03)
a2s175_mic.new((20.2, 20.2, 64.2), -9.83739, icm=1.1e-03, err=9.6e-04)
a2s175_mic.done=True
datasets += pack_data('a2s175_mic', a2s175_mic)

a2s175_str = Data(0.20, 0.0175, 'str')
a2s175_str.new((21.8, 20.2, 64.2), -9.83838, icm=4.5e-03, err=7.8e-04)
a2s175_str.new((24.2, 20.2, 64.2), -9.83841, icm=5.6e-03, err=9.7e-04)
a2s175_str.new((27.2, 20.2, 64.2), -9.83851, icm=4.9e-03, err=7.8e-04)
a2s175_str.new((30.2, 20.2, 64.2), -9.83858, icm=5.1e-03, err=7.5e-04)
a2s175_str.new((32.2, 20.2, 64.2), -9.83863, icm=3.5e-03, err=5.6e-04)
a2s175_str.done=True #can go further
datasets += pack_data('a2s175_str', a2s175_str)

a2s175_hom = Data(0.20, 0.0175, 'hom')
a2s175_hom.new((20.2, 20.2, 64.2), -9.83859, icm=6.5e-06, err=2.0e-06)
a2s175_hom.done=True
datasets += pack_data('a2s175_hom', a2s175_hom)

''' alpha = 0.20, sigma = 0.020 '''
a2s2_mic = Data(0.20, 0.020, 'mic')
a2s2_mic.new((14.6, 16.2, 64.2), -11.2306, icm=1.1e-02, err=2.3e-03)
a2s2_mic.new((16.2, 18.2, 64.2), -11.2299, icm=2.0e-02, err=3.8e-03)
a2s2_mic.new((18.2, 20.2, 64.2), -11.2303, icm=1.5e-02, err=2.9e-03)
a2s2_mic.new((13.0, 14.6, 64.2), -11.2312, icm=8.9e-03, err=1.3e-03)
a2s2_mic.new((12.0, 13.0, 64.2), -11.2310, icm=9.2e-03, err=1.5e-03)
a2s2_mic.new(( 8.2,  7.4, 64.2), -11.2311, icm=1.6e-02, err=2.7e-03)
a2s2_mic.done=True
a2s2_mic.new(( 7.4,  8.2, 64.2), -11.2311, icm=1.6e-02, err=2.7e-03)
a2s2_mic.new((13.0, 12.0, 64.2), -11.2310, icm=9.2e-03, err=1.5e-03)
a2s2_mic.new((14.6, 13.0, 64.2), -11.2312, icm=8.9e-03, err=1.3e-03)
a2s2_mic.new((20.2, 18.2, 64.2), -11.2303, icm=1.5e-02, err=2.9e-03)
a2s2_mic.new((18.2, 16.2, 64.2), -11.2299, icm=2.0e-02, err=3.8e-03)
a2s2_mic.new((16.2, 14.6, 64.2), -11.2306, icm=1.1e-02, err=2.3e-03)
datasets += pack_data('a2s2_mic', a2s2_mic)

# a2s2_cyl = Data(0.20, 0.020, 'cyl')
# a2s2_cyl.new(( 8.2,  7.4, 64.2), -11.2311, icm=1.6e-02, err=2.7e-03)
# datasets += pack_data('a2s2_cyl', a2s2_cyl)

a2s2_str = Data(0.20, 0.020, 'str')
a2s2_str.new((18.2, 20.2, 64.2), -11.2313, icm=7.0e-03, err=1.6e-03)
a2s2_str.new((20.2, 20.2, 64.2), -11.2314, icm=6.5e-03, err=1.4e-03)
a2s2_str.new((24.2, 20.2, 64.2), -11.2317, icm=7.2e-03, err=1.5e-03)
a2s2_str.new((27.2, 20.2, 64.2), -11.2319, icm=2.1e-04, err=7.5e-04)
a2s2_str.new((30.2, 20.2, 64.2), -11.2318, icm=4.7e-05, err=8.8e-04)
a2s2_str.done=True
datasets += pack_data('a2s2_str', a2s2_str)

a2s2_hom = Data(0.20, 0.020, 'hom')
a2s2_hom.new((20.2, 20.2, 64.2), -11.2321, icm=4.0e-06, err=1.5e-06)
a2s2_hom.done = True
datasets += pack_data('a2s2_hom', a2s2_hom)

''' alpha = 0.20, sigma = 0.022 '''
a2s22_cyl = Data(0.20, 0.022, 'cyl')
a2s22_cyl.new((10.2, 10.2, 64.2), -12.3420, icm=1.5e-02, err=1.1e-03)
a2s22_cyl.new((12.2, 12.2, 64.2), -12.3394, icm=3.2e-02, err=4.3e-03)
a2s22_cyl.new(( 8.2,  8.2, 64.2), -12.3420, icm=1.3e-02, err=1.4e-03)
a2s22_cyl.new((10.2, 12.2, 64.2), -12.3420, icm=1.3e-02, err=1.8e-03)
a2s22_cyl.done = True
datasets += pack_data('a2s22_cyl', a2s22_cyl)

a2s22_str = Data(0.20, 0.022, 'str')
a2s22_str.new((12.2, 15.2, 64.2), -12.3426, icm=5.9e-03, err=8.3e-04)
a2s22_str.new((13.0, 15.2, 64.2), -12.3427, icm=6.9e-03, err=1.1e-03)
a2s22_str.new((13.8, 20.2, 64.2), -12.3429, icm=8.7e-05, err=4.5e-04)
a2s22_str.new((14.6, 20.2, 64.2), -12.3428, icm=8.5e-05, err=4.8e-04)
a2s22_str.done = True
datasets += pack_data('a2s22_str', a2s22_str)

a2s22_hom = Data(0.20, 0.022, 'hom')
a2s22_hom.new((20.2, 20.2, 64.2), -12.3433, icm=7.3e-06, err=2.7e-06)
a2s22_hom.done = True
datasets += pack_data('a2s22_hom', a2s22_hom)

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
a2s25_str.new((11.0, 20.2, 60.2), -14.0029, icm=2.8e-03, err=6.4e-04)
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
a25s27_mic = Data(0.25, 0.027, 'mic')
a25s27_mic.new((15.2, 21.2, 64.2), -14.6021, icm=4.6e-03, err=6.7e-04)
a25s27_mic.new((15.2, 17.6, 64.2), -14.6022, icm=8.6e-03, err=7.6e-04)
a25s27_mic.done = True
datasets += pack_data('a25s27_mic', a25s27_mic)

a25s27_cyl = Data(0.25, 0.027, 'cyl')
a25s27_cyl.new((13.0, 13.0, 70.2), -14.6057, icm=5.2e-03, err=9.5e-04)
a25s27_cyl.new((15.2, 15.2, 70.2), -14.6053, icm=1.1e-02, err=1.7e-03)
a25s27_cyl.done = True
datasets += pack_data('a25s27_cyl', a25s27_cyl)

a25s27_str = Data(0.25, 0.027, 'str')
a25s27_str.new((13.0, 15.2, 64.2), -14.6018, icm=1.2e-03, err=2.3e-04)
a25s27_str.new((15.2, 15.2, 64.2), -14.6018, icm=2.5e-03, err=5.2e-04)
a25s27_str.new((18.2, 15.2, 64.2), -14.6017, icm=3.0e-03, err=7.0e-04)
a25s27_str.new((11.0, 15.2, 64.2), -14.6017, icm=3.5e-03, err=5.5e-04)
a25s27_str.done = True
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
a25s3_mic = Data(0.25, 0.030, 'mic')
a25s3_mic.new((15.2, 17.6, 72.2), -16.1858, icm=8.0e-03, err=5.2e-04)
a25s3_mic.new((15.2, 15.2, 72.2), -16.1858, icm=1.2e-02, err=8.1e-04)
a25s3_mic.new((13.0, 15.2, 72.2), -16.1856, icm=1.4e-02, err=1.2e-03)
a25s3_mic.new((17.6, 17.6, 72.2), -16.1857, icm=3.2e-03, err=3.4e-04)
a25s3_mic.new((20.2, 17.6, 72.2), -16.1856, icm=5.7e-03, err=7.1e-04)
a25s3_mic.done = True
datasets += pack_data('a25s3_mic', a25s3_mic)

a25s3_cyl = Data(0.25, 0.030, 'cyl')
a25s3_cyl.new(( 9.2,  9.2, 72.2), -16.1843, icm=1.8e-02, err=2.1e-03)
a25s3_cyl.new((11.0, 11.0, 72.2), -16.1874, icm=1.7e-02, err=2.1e-03)
a25s3_cyl.new((13.0, 13.0, 72.2), -16.1888, icm=5.5e-03, err=1.0e-03)
a25s3_cyl.new((15.2, 15.2, 72.2), -16.1887, icm=6.9e-03, err=1.5e-03)
a25s3_cyl.done=True
datasets += pack_data('a25s3_cyl', a25s3_cyl)

a25s3_str = Data(0.25, 0.030, 'str')
a25s3_str.new((11.0, 15.2, 72.2), -16.1852, icm=3.0e-03, err=5.2e-04)
a25s3_str.new((13.0, 15.2, 72.2), -16.1855, icm=1.6e-03, err=2.3e-04)
a25s3_str.new((15.2, 20.2, 72.2), -16.1857, icm=7.6e-05, err=4.4e-04)
a25s3_str.new((17.6, 15.2, 72.2), -16.1855, icm=5.9e-03, err=9.1e-04)
a25s3_str.new((20.2, 15.2, 72.2), -16.1855, icm=6.1e-03, err=1.3e-03)
a25s3_str.done = True
datasets += pack_data('a25s3_str', a25s3_str)

a25s3_mul = Data(0.25, 0.030, 'str')
a25s3_mul.new((13.0, 15.2, 72.2), -16.1845, icm=7.4e-03, err=1.5e-03)
a25s3_mul.new((15.2, 20.2, 72.2), -16.1854, icm=3.3e-03, err=6.0e-04)
a25s3_mul.new((17.6, 15.2, 72.2), -16.1847, icm=1.1e-02, err=2.5e-03)
a25s3_mul.multi = True
a25s3_mul.done = True
datasets += pack_data('a25s3_mul', a25s3_mul)

a25s3_hommul = Data(0.25, 0.030, 'hom')
# Unstable
a25s3_hommul.done=True
datasets += pack_data('a25s3_hommul', a25s3_hommul)

a25s3_hom = Data(0.25, 0.030, 'hom')
a25s3_hom.new((15.2, 15.2, 64.2), -16.1854, icm=5.3e-06, err=1.5e-06)
a25s3_hom.done=True
datasets += pack_data('a25s3_hom', a25s3_hom)

''' alpha = 0.25, sigma = 0.0325 '''
a25s325_mic = Data(0.25, 0.0325, 'mic')
a25s325_mic.new((13.0, 13.0, 81.2), -17.4969, icm=1.7e-02, err=1.1e-03)
a25s325_mic.new((13.0, 15.2, 81.2), -17.4973, icm=2.0e-02, err=1.1e-03)
a25s325_mic.new((15.2, 15.2, 81.2), -17.4971, icm=1.1e-02, err=5.7e-04)
a25s325_mic.new((17.0, 15.2, 81.2), -17.4970, icm=5.2e-03, err=4.7e-04)
a25s325_mic.done=True
datasets += pack_data('a25s325_mic', a25s325_mic)

a25s325_cyl = Data(0.25, 0.0325, 'cyl')
a25s325_cyl.new(( 9.2,  9.2, 81.2), -17.4963, icm=8.3e-03, err=1.1e-03)
a25s325_cyl.new((11.0, 11.0, 81.2), -17.4983, icm=6.9e-03, err=7.2e-04)
a25s325_cyl.new((13.0, 13.0, 81.2), -17.4995, icm=9.9e-03, err=9.7e-04)
a25s325_cyl.new((15.2, 15.2, 81.2), -17.4995, icm=5.9e-03, err=1.1e-03)
datasets += pack_data('a25s325_cyl', a25s325_cyl)

a25s325_pn  = Data(0.25, 0.0325, 'str')
a25s325_pn.new((12.2, 15.2, 81.2), -17.4997, icm=6.6e-03, err=6.3e-04)
a25s325_pn.new((12.2, 18.2, 81.2), -17.4998, icm=6.3e-03, err=5.2e-04)
a25s325_pn.new((14.6, 18.2, 81.2), -17.4995, icm=7.7e-03, err=1.2e-03)
datasets += pack_data('a25s325_pn', a25s325_pn)

a25s325_strT = Data(0.25, 0.0325, 'str') # Two stripes
a25s325_strT.new((11.0, 20.2, 81.2), -17.4967, icm=3.0e-03, err=4.7e-04)
a25s325_strT.new((13.0, 20.2, 81.2), -17.4975, icm=2.5e-03, err=4.7e-04)
a25s325_strT.new((15.2, 20.2, 81.2), -17.4972, icm=4.0e-03, err=8.0e-04)
a25s325_strT.done=True
datasets += pack_data('a25s325_strT', a25s325_strT)

a25s325_strO = Data(0.25, 0.0325, 'str') # One stripe
a25s325_strO.new((11.0, 20.2, 81.2), -17.4970, icm=1.4e-03, err=2.0e-04)
a25s325_strO.new((13.0, 20.2, 81.2), -17.4971, icm=5.7e-03, err=1.1e-03)
a25s325_strO.new((15.2, 20.2, 81.2), -17.4961, icm=6.9e-03, err=1.3e-03)
a25s325_strO.done=True
datasets += pack_data('a25s325_strO', a25s325_strO)

a25s325_hom = Data(0.25, 0.0325, 'hom')
a25s325_hom.new((15.2, 15.2, 81.2), -17.4968, icm=2.0e-06, err=5.0e-07)
a25s325_hom.done = True
datasets += pack_data('a25s325_hom', a25s325_hom)

########################################################################

''' alpha = 0.30, sigma = 0.005 '''
a3s5_hol = Data(0.30, 0.005, 'cyl')
a3s5_hol.new((10.2, 10.2, 64.2), -2.68125, icm=4.7e-02, err=5.2e-03)
a3s5_hol.new((16.2, 16.2, 64.2), -2.68749, icm=6.0e-02, err=7.5e-03)
a3s5_hol.new((16.2, 18.2, 64.2), -2.68997, icm=4.3e-02, err=3.4e-03)
a3s5_hol.new((16.2, 16.2, 64.2), -2.68968, icm=4.0e-02, err=3.3e-03)
datasets += pack_data('a3s5_hol', a3s5_hol)

''' alpha = 0.30, sigma = 0.020 '''
a3s2_cyl = Data(0.30, 0.020, 'cyl')
a3s2_cyl.new(( 9.2,  9.2, 64.2), -10.5044, icm=1.6e-02, err=2.4e-03)
a3s2_cyl.new((11.0, 11.0, 64.2), -10.5091, icm=5.9e-03, err=1.1e-03)
a3s2_cyl.new((12.2, 12.2, 64.2), -10.5084, icm=1.1e-02, err=1.8e-03)
a3s2_cyl.new((15.2, 15.2, 64.2), -10.5025, icm=4.4e-02, err=2.4e-03)
a3s2_cyl.done = True
datasets += pack_data('a3s2_cyl', a3s2_cyl)

a3s2_mic = Data(0.30, 0.020, 'mic')
a3s2_mic.new((15.2, 17.6, 64.2), -10.4873, icm=3.6e-02, err=7.4e-03)
a3s2_mic.new((16.2, 17.6, 64.2), -10.4922, icm=3.4e-02, err=6.8e-03)
a3s2_mic.new((15.2, 16.2, 64.2), -10.4936, icm=6.0e-04, err=3.0e-03)
a3s2_mic.new((14.0, 16.2, 64.2), -10.4922, icm=2.1e-02, err=4.6e-03)
a3s2_mic.new((16.2, 18.2, 64.2), -10.4923, icm=2.5e-02, err=5.0e-03)
a3s2_mic.new((15.2, 15.2, 64.2), -10.4961, icm=1.6e-02, err=3.8e-03)
a3s2_mic.new((14.6, 15.2, 72.2), -10.4988, icm=1.3e-02, err=2.5e-03)
a3s2_mic.new((14.6, 14.6, 72.2), -10.4992, icm=1.7e-02, err=2.4e-03)
a3s2_mic.new((14.6, 13.0, 72.2), -10.4996, icm=1.4e-02, err=1.6e-03)
a3s2_mic.new((13.0, 13.0, 72.2), -10.4989, icm=8.2e-03, err=1.8e-03)
a3s2_mic.done = True #?
a3s2_mic.multi = True
a3s2_mic.new((13.0, 14.6, 72.2), -10.4996, icm=1.4e-02, err=1.6e-03)
a3s2_mic.new((15.2, 14.6, 64.2), -10.4971, icm=1.9e-02, err=3.6e-03)
a3s2_mic.new((18.2, 16.2, 64.2), -10.4923, icm=2.5e-02, err=5.0e-03)
a3s2_mic.new((16.2, 14.0, 64.2), -10.4922, icm=2.1e-02, err=4.6e-03)
a3s2_mic.new((16.2, 15.2, 64.2), -10.4936, icm=6.0e-04, err=3.0e-03)
a3s2_mic.new((17.6, 16.2, 64.2), -10.4873, icm=3.6e-02, err=7.4e-03)
a3s2_mic.new((17.6, 15.2, 64.2), -10.4873, icm=3.6e-02, err=7.4e-03)
datasets += pack_data('a3s2_mic', a3s2_mic)

a3s2_str = Data(0.30, 0.020, 'str')
a3s2_str.new((13.0, 15.2, 64.2), -10.4828, icm=3.1e-02, err=7.1e-03)
a3s2_str.new((15.2, 15.2, 64.2), -10.4884, icm=5.4e-04, err=2.9e-03)
a3s2_str.new((18.2, 15.2, 64.2), -10.4855, icm=2.0e-02, err=4.7e-03)
a3s2_str.multi = True
a3s2_str.done = True
datasets += pack_data('a3s2_str', a3s2_str)

a3s2_mul = Data(0.30, 0.020, 'hom')
a3s2_mul.new((15.2, 15.2, 64.2), -10.4794, icm=1.2e-03, err=5.3e-04)
a3s2_mul.multi = True
a3s2_mul.done = True
datasets += pack_data('a3s2_mul', a3s2_mul)

''' alpha = 0.30, sigma = 0.025 '''
a3s25_cyl = Data(0.30, 0.025, 'cyl')
a3s25_cyl.new((12.2, 12.2, 72.2), -13.0655, icm=9.3e-03, err=1.2e-03)
a3s25_cyl.new((11.0, 11.0, 72.2), -13.0657, icm=9.3e-03, err=1.3e-03)
a3s25_cyl.done = True
datasets += pack_data('a3s25_cyl', a3s25_cyl)

a3s25_mic = Data(0.30, 0.025, 'mic')
a3s25_mic.new((15.2, 17.6, 72.2), -13.0522, icm=4.6e-02, err=5.1e-03)
a3s25_mic.new((17.6, 17.6, 70.2), -13.0516, icm=9.9e-02, err=9.3e-03)
a3s25_mic.new((15.2, 19.4, 70.2), -13.0539, icm=3.0e-02, err=3.9e-03)
a3s25_mic.new((17.6, 19.4, 70.2), -13.0521, icm=6.2e-02, err=6.7e-03)
a3s25_mic.new((13.0, 15.2, 72.2), -13.0547, icm=3.1e-02, err=3.5e-03)
a3s25_mic.new((15.2, 15.2, 72.2), -13.0548, icm=3.2e-02, err=3.9e-03)
a3s25_mic.multi = True
a3s25_mic.done = True
datasets += pack_data('a3s25_mic', a3s25_mic)

a3s25_str = Data(0.30, 0.025, 'str')
a3s25_str.new((13.0, 15.2, 64.2), -13.0500, icm=3.1e-02, err=5.4e-03)
a3s25_str.new((15.2, 15.2, 64.2), -13.0538, icm=2.9e-02, err=4.7e-03)
a3s25_str.new((18.2, 15.2, 64.2), -13.0529, icm=2.1e-02, err=4.2e-03)
a3s25_str.multi = True
a3s25_str.done = True
datasets += pack_data('a3s25_str', a3s25_str)

a3s25_mul = Data(0.30, 0.025, 'mul')
# Unstable
a3s25_mul.done = True
datasets += pack_data('a3s25_mul', a3s25_mul)

a3s25_hom = Data(0.30, 0.025, 'hom')
a3s25_hom.new((15.2, 15.2, 64.2), -13.0394, icm=2.2e-06, err=8.1e-07)
a3s25_hom.done = True
datasets += pack_data('a3s25_hom', a3s25_hom)

''' alpha = 0.30, sigma = 0.030 '''
a3s3_cyl = Data(0.30, 0.030, 'cyl')
a3s3_cyl.new(( 8.2,  8.2, 70.2), -15.5888, icm=5.8e-03, err=1.1e-03)
a3s3_cyl.new((10.2, 10.2, 70.2), -15.5935, icm=1.2e-02, err=3.1e-03)
a3s3_cyl.new((12.2, 12.2, 70.2), -15.5953, icm=5.6e-03, err=7.6e-04)
a3s3_cyl.new((15.2, 15.2, 70.2), -15.5907, icm=1.5e-02, err=3.7e-03)
a3s3_cyl.done = True
datasets += pack_data('a3s3_cyl', a3s3_cyl)

a3s3_str = Data(0.30, 0.030, 'str')
a3s3_str.new(( 9.2, 15.2, 70.2), -15.5830, icm=1.3e-02, err=1.6e-03)
a3s3_str.new((12.2, 15.2, 70.2), -15.5886, icm=3.3e-04, err=2.0e-03)
a3s3_str.new((15.2, 15.2, 70.2), -15.5861, icm=3.3e-02, err=4.3e-03)
a3s3_str.new((18.2, 15.2, 70.2), -15.5840, icm=1.9e-02, err=3.5e-03)
a3s3_str.done = True
datasets += pack_data('a3s3_str', a3s3_str)

# a3s3_mic = Data(0.30, 0.030, 'mic')
# a3s3_mic.new((11.0, 13.0, 70.2), -15.5867, icm=3.0e-02, err=3.9e-03)
# a3s3_mic.new((13.0, 15.2, 70.2), -15.5877, icm=4.0e-02, err=3.7e-03)
# a3s3_mic.new((15.2, 16.2, 70.2), -15.5897, icm=3.9e-02, err=3.8e-03)
# a3s3_mic.new((18.2, 16.2, 70.2), -15.5867, icm=6.7e-02, err=8.1e-03)
# a3s3_mic.multi=True
# datasets += pack_data('a3s3_mic', a3s3_mic)

a3s3_mul = Data(0.30, 0.030, 'hom')
a3s3_mul.new((15.2, 15.2, 70.2), -15.5739, icm=1.3e-03, err=5.6e-04)
a3s3_mul.multi = True
a3s3_mul.done = True
datasets += pack_data('a3s3_mul', a3s3_mul)

a3s3_hom = Data(0.30, 0.030, 'hom')
#Unstable
a3s3_hom.done = True
datasets += pack_data('a3s3_hom', a3s3_hom)

''' alpha = 0.30, sigma = 0.0325'''
a3s325_cyl = Data(0.30, 0.0325, 'cyl')
a3s325_cyl.new(( 8.2,  8.2, 70.2), -16.8433, icm=5.3e-03, err=6.7e-04)
a3s325_cyl.new((10.2, 10.2, 70.2), -16.8454, icm=2.9e-02, err=4.9e-03)
a3s325_cyl.new((12.2, 12.2, 70.2), -16.8491, icm=4.7e-03, err=6.0e-04)
a3s325_cyl.new((15.2, 15.2, 70.2), -16.8372, icm=3.0e-02, err=5.5e-03)
a3s325_cyl.done = True
datasets += pack_data('a3s325_cyl', a3s325_cyl)

a3s325_str = Data(0.30, 0.0325, 'str')
a3s325_str.new(( 9.2, 15.2, 70.2), -16.8442, icm=1.3e-02, err=2.9e-03)
a3s325_str.new((12.2, 15.2, 80.2), -16.8486, icm=9.4e-03, err=1.5e-03)
a3s325_str.new((15.2, 15.2, 70.2), -16.8432, icm=2.0e-02, err=3.0e-03)
a3s325_str.new((18.2, 15.2, 70.2), -16.8409, icm=1.5e-02, err=4.0e-03)
a3s325_str.done = True
datasets += pack_data('a3s325_str', a3s325_str)

a3s325_vor = Data(0.30, 0.0325, 'hom')
a3s325_vor.new((10.2, 10.2, 70.2), -16.8312, icm=8e-03, err=1e-03)
a3s325_vor.multi = True
a3s325_vor.done = True # Probably
datasets += pack_data('a3s325_vor', a3s325_vor)

a3s325_mul = Data(0.30, 0.0325, 'hom')
a3s325_mul.new((15.2, 15.2, 70.2), -16.8268, icm=4.5e-03, err=1.6e-03)
a3s325_mul.multi = True
a3s325_mul.done = True
datasets += pack_data('a3s325_mul', a3s325_mul)

''' alpha = 0.30, sigma = 0.035'''
a3s35_cyl = Data(0.30, 0.035, 'cyl')
a3s35_cyl.new(( 8.2,  8.2, 75.2), -18.0890, icm=4.2e-03, err=7.1e-04)
a3s35_cyl.new((10.2, 10.2, 75.2), -18.0928, icm=1.4e-02, err=2.7e-03)
a3s35_cyl.new((12.2, 12.2, 75.2), -18.0943, icm=7.7e-03, err=1.0e-03)
a3s35_cyl.new((15.2, 15.2, 75.2), -18.0907, icm=9.8e-03, err=2.0e-03)
a3s35_cyl.done = True
datasets += pack_data('a3s35_cyl', a3s35_cyl)

a3s35_pn  = Data(0.30, 0.035, 'str')
a3s35_pn.new((12.2, 20.2, 75.2), -18.0938, icm=1.0e-02, err=1.6e-03)
a3s35_pn.new((14.6, 20.2, 75.2), -18.0920, icm=1.1e-02, err=1.6e-03)
a3s35_pn.new((13.0, 20.2, 75.2), -18.0939, icm=7.0e-03, err=8.7e-04)
a3s35_pn.new((12.2, 18.2, 75.2), -18.0948, icm=7.4e-03, err=1.1e-03)
a3s35_pn.done=True
datasets += pack_data('a3s35_pn', a3s35_pn)

a3s35_str = Data(0.30, 0.035, 'str')
a3s35_str.new(( 9.2, 15.2, 75.2), -18.0849, icm=1.0e-02, err=2.5e-03)
a3s35_str.new((12.2, 15.2, 75.2), -18.0946, icm=5.5e-03, err=7.3e-04)
a3s35_str.new((15.2, 15.2, 75.2), -18.0887, icm=2.3e-02, err=3.0e-03)
a3s35_str.new((18.2, 15.2, 75.2), -18.0859, icm=1.7e-02, err=3.6e-03)
a3s35_str.done = True
datasets += pack_data('a3s35_str', a3s35_str)

a3s35_vor = Data(0.30, 0.035, 'hom')
a3s35_vor.new((15.2, 15.2, 75.2), -18.0779, icm=4.0e-02, err=4.0e-03)
a3s35_vor.multi = True
a3s35_vor.done = True # Probably
datasets += pack_data('a3s35_vor', a3s35_vor)

a3s35_hom = Data(0.30, 0.035, 'hom')
a3s35_hom.new((10.2, 10.2, 75.2), -18.0782, icm=7.4e-02, err=2.1e-05)
a3s35_hom.done = True
datasets += pack_data('a3s35_hom', a3s35_hom)

''' alpha = 0.30, sigma = 0.040 '''
a3s4_cyl = Data(0.30, 0.040, 'cyl')
a3s4_cyl.new(( 8.2,  8.2, 86.6), -20.5531, icm=5.6e-03, err=6.9e-04)
a3s4_cyl.new((10.2, 10.2, 86.6), -20.5581, icm=1.6e-03, err=1.6e-04)
a3s4_cyl.new((12.2, 12.2, 86.6), -20.5583, icm=3.3e-03, err=3.8e-04)
a3s4_cyl.new((14.6, 14.6, 86.6), -20.5559, icm=5.6e-03, err=8.0e-04)
a3s4_cyl.done=True
datasets += pack_data('a3s4_cyl', a3s4_cyl)

a3s4_pn  = Data(0.30, 0.040, 'str')
a3s4_pn.new((10.2, 20.2, 86.6), -20.5585, icm=7.6e-03, err=9.6e-04)
a3s4_pn.new((12.2, 18.2, 86.6), -20.5584, icm=7.6e-03, err=8.6e-04)
a3s4_pn.new((12.2, 20.2, 86.6), -20.5581, icm=1.0e-02, err=9.0e-04)
a3s4_pn.new((14.6, 20.2, 86.6), -20.5561, icm=1.1e-02, err=1.5e-03)
a3s4_pn.done=True #can min further
datasets += pack_data('a3s4_pn', a3s4_pn)

a3s4_str = Data(0.30, 0.040, 'str')
a3s4_str.new(( 4.2, 15.2, 80.2), -20.5547, icm=7.1e-04, err=8.7e-05)
a3s4_str.new(( 5.0, 20.2, 80.2), -20.5579, icm=6.1e-04, err=8.8e-05)
a3s4_str.new(( 5.6, 20.2, 80.2), -20.5582, icm=1.0e-03, err=1.0e-04)
a3s4_str.new(( 6.2, 15.2, 80.2), -20.5571, icm=4.8e-03, err=5.6e-04)
a3s4_str.new(( 7.4, 15.2, 80.2), -20.5543, icm=1.3e-02, err=1.5e-03)
a3s4_str.new(( 9.2, 15.2, 80.2), -20.5499, icm=1.2e-02, err=1.6e-03)
a3s4_str.done = True
a3s4_str.new(( 5.6, 20.2, 80.2), -20.5584, icm=1.0e-03, err=1.0e-04) # Temp, get 2 str to get minF
datasets += pack_data('a3s4_str', a3s4_str)

a3s4_mul = Data(0.30, 0.040, 'str')
a3s4_mul.new(( 8.6, 20.2, 86.6), -20.5543, icm=4.1e-03, err=1.1e-03)
a3s4_mul.new(( 9.2, 20.2, 86.6), -20.5550, icm=4.2e-03, err=8.1e-04)
a3s4_mul.new((10.2, 15.2, 86.6), -20.5549, icm=5.5e-03, err=1.2e-03)
a3s4_mul.new((11.0, 15.2, 86.6), -20.5539, icm=7.0e-03, err=2.3e-03)
a3s4_mul.new((12.2, 15.2, 80.2), -20.5522, icm=2.3e-02, err=5.1e-03)
a3s4_mul.new((15.2, 15.2, 86.6), -20.5503, icm=7.0e-03, err=1.3e-03)
a3s4_mul.multi = True
a3s4_mul.done=True
datasets += pack_data('a3s4_mul', a3s4_mul)

a3s4_hol = Data(0.30, 0.040, 'hol')
a3s4_hol.new((10.2, 10.2, 80.2), -20.5368, icm=1e-02, err=2e-03)
a3s4_hol.new((12.2, 12.2, 80.2), -20.5377, icm=2e-02, err=3e-03)
a3s4_hol.new((15.2, 15.2, 80.2), -20.5390, icm=2e-02, err=3e-03)
a3s4_hol.new((18.2, 18.2, 80.2), -20.5393, icm=4e-02, err=4e-03)
a3s4_hol.multi = True
a3s4_hol.done = True # Not worth continuing, F too far
datasets += pack_data('a3s4_hol', a3s4_hol)

a3s4_hom = Data(0.30, 0.040, 'hom')
a3s4_hom.new((15.2, 15.2, 75.2), -20.5384, icm=3.4e-03, err=1.3e-03)
a3s4_hom.multi = True
a3s4_hom.done = True
datasets += pack_data('a3s4_hom', a3s4_hom)

''' alpha = 0.30, sigma = 0.045 '''
a3s45_pn  = Data(0.30, 0.045, 'str')
a3s45_pn.new((10.2, 18.2, 90.2), -22.9834, icm=7.3e-03, err=9.9e-04)
a3s45_pn.new((10.2, 20.2, 90.2), -22.9833, icm=1.9e-02, err=1.2e-03)
a3s45_pn.new((10.2, 24.2, 90.2), -22.9829, icm=2.8e-02, err=2.2e-03)
a3s45_pn.new((12.2, 20.2, 90.2), -22.9830, icm=1.3e-02, err=7.7e-04)
a3s45_pn.done=True #can min further
datasets += pack_data('a3s45_pn', a3s45_pn)

a3s45_str = Data(0.30, 0.045, 'str')
a3s45_str.new(( 3.8, 20.2, 86.6), -22.9765, icm=9.4e-04, err=1.2e-04)
a3s45_str.new(( 4.2, 20.2, 86.6), -22.9794, icm=1.0e-04, err=1.1e-05)
a3s45_str.new(( 5.0, 20.2, 86.6), -22.9822, icm=1.9e-03, err=2.3e-04)
a3s45_str.new(( 6.2, 20.2, 90.2), -22.9819, icm=1.7e-03, err=1.6e-04)
a3s45_str.done = True
datasets += pack_data('a3s45_str', a3s45_str)

a3s45_mul = Data(0.30, 0.045, 'str')
a3s45_mul.new(( 8.2, 20.2, 86.6), -22.9780, icm=2.0e-03, err=4.9e-04)
a3s45_mul.new(( 9.2, 20.2, 86.6), -22.9788, icm=7.3e-03, err=1.1e-03)
a3s45_mul.new((10.2, 20.2, 86.6), -22.9784, icm=2.2e-04, err=1.1e-03)
a3s45_mul.new((11.0, 20.2, 86.6), -22.9780, icm=1.8e-04, err=1.3e-03)
a3s45_mul.multi=True
a3s45_mul.done=True
datasets += pack_data('a3s45_mul', a3s45_mul)

a3s45_hol = Data(0.30, 0.045, 'hol')
a3s45_hol.new((15.2, 15.2, 86.6), -22.9649, icm=5.3e-02, err=4.3e-03)
a3s45_hol.new((15.2, 18.2, 86.6), -22.9668, icm=4.5e-02, err=3.8e-03)
a3s45_hol.new((18.2, 18.2, 90.2), -22.9692, icm=2.4e-02, err=2.7e-03)
a3s45_hol.new((18.2, 20.2, 90.2), -22.9684, icm=2.1e-02, err=2.8e-03)
a3s45_hol.multi=True
a3s45_hol.done=True
datasets += pack_data('a3s45_hol', a3s45_hol)

a3s45_hom = Data(0.30, 0.045, 'hom')
a3s45_hom.new((20.2, 20.2, 90.2), -22.9719, icm=9.7e-07, err=2.8e-07)
a3s45_hom.done=True
datasets += pack_data('a3s45_hom', a3s45_hom)

''' alpha = 0.30, sigma = 0.050 '''
a3s5_pn = Data(0.30, 0.050, 'pn')
a3s5_pn.new((10.2, 18.2, 96.2), -25.3636, icm=9.2e-03, err=7.5e-04)
a3s5_pn.new((10.2, 20.2, 96.2), -25.3645, icm=1.4e-02, err=1.1e-03)
a3s5_pn.new((12.2, 20.2, 96.2), -25.3638, icm=2.3e-02, err=2.2e-03)
datasets += pack_data('a3s5_pn', a3s5_pn)

a3s5_str = Data(0.30, 0.050, 'str')
a3s5_str.new(( 9.2, 20.2, 96.2), -25.3634, icm=5.6e-03, err=7.3e-04)
a3s5_str.new((11.0, 20.2, 96.2), -25.3638, icm=2.4e-02, err=3.0e-03)
a3s5_str.new((13.0, 20.2, 96.2), -25.3635, icm=1.0e-02, err=1.3e-03)
datasets += pack_data('a3s5_str', a3s5_str)

a3s5_mul = Data(0.30, 0.050, 'mul')
a3s5_mul.new(( 8.2, 20.2, 96.2), -25.3569, icm=1.1e-02, err=2.0e-03)
a3s5_mul.new((10.2, 20.2, 96.2), -25.3566, icm=1.7e-02, err=2.3e-03)
a3s5_mul.new((12.2, 20.2, 96.2), -25.3570, icm=1.7e-02, err=2.5e-03)
datasets += pack_data('a3s5_mul', a3s5_mul)

a3s5_hom = Data(0.30, 0.050, 'hom')
a3s5_hom.new((20.2, 20.2, 96.2), -25.3553, icm=6.8e-04, err=2.0e-04)
a3s5_hom.done=True
datasets += pack_data('a3s5_hom', a3s5_hom)
########################################################################

''' alpha = 0.325, sigma = 0.020 '''
a325s2_mul = Data(0.325, 0.020, 'hom')
a325s2_mul.new((15.2, 15.2, 70.2), -10.2824, icm=3.2e-03, err=1.2e-03)
a325s2_mul.multi = True
a325s2_mul.done = True
datasets += pack_data('a325s2_mul', a325s2_mul)

a325s2_str = Data(0.325, 0.020, 'str')
a325s2_str.new((15.2, 15.2, 70.2), -10.2983, icm=7.8e-02, err=9.2e-03)
a325s2_str.new((18.2, 15.2, 70.2), -10.2994, icm=2.9e-02, err=6.8e-03)
datasets += pack_data('a325s2_str', a325s2_str)

########################################################################

''' alpha = 0.35, sigma = 0.020 '''
# a35s2_str



All = All(datasets)


