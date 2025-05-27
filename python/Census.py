import numpy as np, pandas as pd
import matplotlib.pyplot as plt, matplotlib as mpl

class Census:
    """
    docstring for Census class
    """
    def __init__(self, filepath, header=1, datarange=(17,None)): 
        from pathlib import Path
        p = Path(filepath)
        df = pd.read_csv(p, header=header)
        
        # Discard IP addresses
        df = df.drop([0])

        # No previews
        df = df[df['Response Type']!='Survey Preview'].reset_index(drop=True)

        # Discard unnecessary data
        df = df.iloc[:, datarange[0]:datarange[1]]

        # Complete
        if datarange[1] == None: 
            lastcol = df.shape[1]+datarange[0]
        else: 
            lastcol = datarange[1]
        print('Initialization completed.')
        print('\tData recorded from column {} to {}'.format(chr(num_to_exel_col(datarange[0])), chr(num_to_exel_col(lastcol))))
        print('{} responses.\n{} questions asked.'.format(*df.shape))
        self.data_df = df
        
        
def num_to_exel_col(n):
    # Source: https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
    d, m = divmod(n,26) # 26 is the number of ASCII letters
    return '' if n < 0 else num_to_exel_col(d-1)+chr(m+65)

    
