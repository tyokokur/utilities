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
        df = df.iloc[:,17:]

        # Print data summary
        print('Data read into df1.\n{} responses.\n{} questions asked.'.format(*df1.shape))
        
    
