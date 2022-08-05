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

def git_sync(GIT_REPO, REPO_SUB):
  ## Paste GIT_REPO/REPO_sub (e.g. tmpdat/sysg) into Google Colab pwd
  import config
  print(config.GIT_TOKEN)
  print(config.GIT_USERNAME)

  from IPython import get_ipython
  ipython = get_ipython()

  #### Github clone data into Gdrive_folder
  GIT_PATH = "https://" + config.GIT_TOKEN + "@github.com/" + config.GIT_USERNAME + "/" + GIT_REPO + ".git"
  print("GIT_PATH: ", "https://" + "github.com/" + config.GIT_USERNAME + "/" + GIT_REPO + ".git")
  exec(ipython.transform_cell('!git clone --quiet "{GIT_PATH}" ./temp'))      # clone github repository to temp folder
  exec(ipython.transform_cell('!mv ./temp/"{REPO_SUB}"/*  ./'))
  exec(ipython.transform_cell('!rm -rf ./temp'))                      # remove all the files/folders in temp folder
  return