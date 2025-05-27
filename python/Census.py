import numpy as np, pandas as pd
import matplotlib.pyplot as plt, matplotlib as mpl

class Census:
    """
    docstring for Census class
    """
    def __init__(self, filepath, header=1, datarange=(17,None), from_file=True):
        if from_file:
            df = _init_from_file(self, filepath=filepath, header=header, datarange=datarange)

        # Discard unnecessary data
        df = df.iloc[:, datarange[0]:datarange[1]]
        
        # Record
        self.data_df = df
        self.q_list  = df.columns.to_list()
        
        # Complete
        if datarange[1] == None: 
            lastcol = df.shape[1]+datarange[0]-1
        else: 
            lastcol = datarange[1]
        
        print('Initialization completed.')
        print('Data recorded')
        print('\tfrom column {}: \n\t\t"{}"'.format(num_to_exel_col(datarange[0]), self.q_list[0]))
        print('\tto column {}: \n\t\t"{}"'.format(num_to_exel_col(lastcol), self.q_list[-1]))
        print('{} responses.\n{} questions asked.'.format(*df.shape))
        
    def section(self, datarange):
        print('no')
        
    def _init_from_file(self, filepath, header=1, datarange=(17,None)): 
        from pathlib import Path
        p = Path(filepath)
        df = pd.read_csv(p, header=header)
        df = df.drop([0]) # Discard IP addresses
        df = df[df['Response Type']!='Survey Preview'].reset_index(drop=True) # No previews
        return df
        
        
def num_to_exel_col(n):
    # Source: https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
    d, m = divmod(n,26) # 26 is the number of ASCII letters
    return '' if n < 0 else num_to_exel_col(d-1)+chr(m+65)

    
