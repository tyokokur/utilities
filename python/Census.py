import numpy as np, pandas as pd
import matplotlib.pyplot as plt, matplotlib as mpl

class Census:
    """
    docstring for Census class
    """
    def __init__(self, filepath='', header=1, datarange=(17,None), from_file=True, 
                 orig_df=pd.DataFrame({'empty':[0]}), orig_datarange=(None,None)):
        if from_file:
            df = self._init_from_file(filepath=filepath, header=header, datarange=datarange)
            self.orig_datarange = datarange
            datarange = (0, 0)
        else:
            df = orig_df.iloc[:, datarange[0]:datarange[1]]
            self.orig_datarange = orig_datarange
        
        # Update 
        self.data_df  = df
        self.q_list   = df.columns.to_list()
        
        # Complete
        lastcol = df.shape[1]+self.orig_datarange[0]+datarange[0]-1
        print('Initialization completed.')
        print('Data recorded')
        print('\tfrom column {}: \n\t\t"{}"'.format(num_to_exel_col(datarange[0]), self.q_list[0]))
        print('\tto column {}: \n\t\t"{}"'.format(num_to_exel_col(lastcol), self.q_list[-1]))
        print('{} responses.\n{} questions asked.'.format(*df.shape))
        
    def section(self, datarange=(None,None), orig_df=pd.DataFrame({'empty':[0]})):
        return Census(from_file=False, datarange=datarange, orig_df=orig_df, orig_datarange=self.orig_datarange)
        
    def _init_from_file(self, filepath, header=1, datarange=(17,None)): 
        from pathlib import Path
        p = Path(filepath)
        df = pd.read_csv(p, header=header)
        df = df.drop([0]) # Discard IP addresses
        df = df[df['Response Type']!='Survey Preview'].reset_index(drop=True) # No previews
        df = df.iloc[:, datarange[0]:datarange[1]] # Discard unnecessary data
        return df
        
        
def num_to_exel_col(n):
    # Source: https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
    d, m = divmod(n,26) # 26 is the number of ASCII letters
    return '' if n < 0 else num_to_exel_col(d-1)+chr(m+65)

    
