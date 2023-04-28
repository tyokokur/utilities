import pandas as pd

GIT = 'https://github.com/tyokokur/tmpdat/raw/main/nfh/'

test = pd.read_csv(GIT+'NFH_train.txt')

print(test)