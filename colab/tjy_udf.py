def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

def H_find(filename, b0, thresh):
    import pandas as pd, numpy as np

    df = pd.read_csv(filename, sep="\s+", skiprows=0)
    Nx = len(df.index)
    rows = range(0, Nx)

    phA = pd.DataFrame(data=None, index=rows, columns=range(2), dtype=None, copy=False)
    phA = phA.fillna(0) # with 0s rather than NaNs

    for i in range(Nx):
        phA.iloc[i, 0] = df.iloc[i,0] * b0
        phA.iloc[i, 1] = df.iloc[i,1] 

    diff = 100
    for i in range(Nx):
        new_diff = np.abs(phA.iloc[i, 1] - thresh)
        if new_diff < diff: 
            diff = new_diff
            x1 = phA.iloc[i, 0]
            y1 = phA.iloc[i, 1]
            if y1 > thresh :
                x2 = phA.iloc[i+1, 0]
                y2 = phA.iloc[i+1, 1]
            else: 
                x2 = phA.iloc[i-1, 0]
                y2 = phA.iloc[i-1, 1]

    m = (y2-y1)/(x2-x1)
    b = y2 - m * x2
    x = (thresh - b) / m
    y = m*x + b
  
    return x

def git_sync(GIT_REPO, REPO_SUB, GIT_CREDS):
  ## Paste GIT_REPO/REPO_sub (e.g. tmpdat/sysg) into Google Colab pwd
  from IPython import get_ipython
  ipython = get_ipython()

  #### Github clone data into Gdrive_folder
  GIT_PATH = "https://" + GIT_CREDS['GIT_TOKEN'] + "@github.com/" + GIT_CREDS['GIT_USERNAME'] + "/" + GIT_REPO + ".git"
  print("GIT_PATH: ", "https://" + "github.com/" + GIT_CREDS['GIT_USERNAME'] + "/" + GIT_REPO + ".git")

  ipython.system('git clone --quiet "{GIT_PATH}" ./temp')  # clone github repository to temp folder
  ipython.system('mv ./temp/"{REPO_SUB}"/*  ./')           # copy only subdirectory files to Colab pwd
  ipython.system('rm -rf ./temp')                          # remove all the files/folders in temp folder
  ipython.system('date')
  return

def Kap_D(Cs):
  ## mM (1e-03 * Molar) to nm (1e-09 * Meter)
  from numpy import sqrt
  Cs *=  6.022e23*1e3
  pi = 3.1415926535
  e = 1.6e-19
  ep0 = 8.8541878128e-12 # x length scale
  epr = 80
  kb = 1.38064852e-23
  beta = 1/(kb*293)

  lb = e**2 * beta / (4*pi * ep0 * epr)
  kappa = sqrt(4*pi * lb * (1*Cs + 1*Cs))
  return kappa