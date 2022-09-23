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

def plot_anim(fname, simname='SIM.dat', lx=100, dx=17/150, b0=1.0, html_render='jshtml'):
    from matplotlib import animation, rc
    import numpy as np, pandas as pd, matplotlib.pyplot as plt

    if lx == 100 or lx == 300 or lx == 275 or lx == 350: nx = int(np.floor(lx / dx))
    else: nx = int(np.ceil(lx/dx))

    ## Unknown bug: 
    # for lx = 100, nx = np.floor, z = np.arange(...(lx-dx)/b0)
    # for lx = 125, 150, nx = np.ceil,  z = np.arange(...(lx)/b0)

    ## Iteration sim:
    df = pd.read_csv(fname, sep="\s+", skiprows=0, header=None)
    print("it len ", np.size(df,0))

    ph = pd.read_csv(simname, sep="\s+", skiprows=0, header=None).to_numpy()
    nframes = np.min([int(len(df)), int(len(ph)/nx)])
    print("nframes calc ", nframes)
    phn = np.reshape(ph, (int(len(ph)/nx), nx))
    print("phn len ", np.size(phn, 0))

    # create a figure and axes
    fig = plt.figure(figsize=(15, 9))
    ax1 = plt.subplot(1,2,1)
    ax2 = plt.subplot(2,4,3)
    ax3 = plt.subplot(2,4,4)
    ax4 = plt.subplot(2,2,4)
    plt.subplots_adjust(hspace=0.40)
    plt.subplots_adjust(wspace=0.35)

    # set up the subplots as needed
    ax1.set_xlim(( 0, lx))            
    ax1.set_ylim((0, 1.0))
    ax1.set_xlabel('z/b')
    ax1.set_ylabel(r'$\langle\phi_p(z)\rangle_{xy}$')
                
    ax3.set_ylim((1e-6, 1))
    ax3.set_xlim((0, 100))
    ax3.set_xlabel('it')
    ax3.set_title('inCompMax')
    ax3.set_yscale('log')
    ax3.plot([0,5e5], np.ones(2)*2e-6, ':r')
                
    ax2.set_ylim((1e-10, 1))
    ax2.set_xlim((0, 100))
    ax2.set_xlabel('it')
    ax2.set_title('freeDiff')
    ax2.set_yscale('log')
    ax2.plot([0,5e5], np.ones(2)*1e-9, ':r')

    ax4.set_ylim((5e-4, 1))
    ax4.set_xlim((0, 100))
    ax4.set_xlabel('it')
    ax4.set_title('andErr')
    ax4.set_yscale('log')
    ax4.plot([0,5e5], np.ones(2)*1e-3, ':r')

    # create objects that will change in the animation. These are
    # initially empty, and will be given new values for each frame
    # in the animation.
    txt_title = ax1.set_title('')
    line1, = ax1.plot([], [], 'k')     # ax.plot returns a list of 2D line objects
    line2, = ax2.plot([], [], 'r')
    line3, = ax3.plot([], [], 'b')
    line4, = ax4.plot([], [], 'g')

    ## Comment to preview subplots
    plt.close()

    # animation function. This is called sequentially
    def drawframe(n):
        ## b0 global from function input 
        nskip = nframes/100
        n = round(n * nskip)
        if n > nframes - 1: n = nframes-1
        if lx == 100 or lx ==300 or lx==275 or lx == 350: z = np.arange(0, (lx-dx)/b0, dx)
        else: z = np.arange(0, (lx)/b0, dx)
        pha = phn[n,:]

        x  = df.iloc[:n,0]
        y1 = df.iloc[:n,2]
        y2 = df.iloc[:n,3]
        y3 = df.iloc[:n,4]
        line1.set_data(z, pha)
        line2.set_data(x, y1)
        line3.set_data(x, y2)
        line4.set_data(x, y3)

        ax1.set_ylim(0, max(pha)*1.2)
        if not x.empty: 
            txt_title.set_text('it = {0:4d}'.format(x[n-1]))
            ax2.set_xlim(0, max(x)*1.1)
            ax3.set_xlim(0, max(x)*1.1)
            ax4.set_xlim(0, max(x)*1.1)
        if not y1.empty: ax3.set_ylim(1e-6,  max(y2)*1.5)
        if not y2.empty: ax2.set_ylim(1e-10, max(y1)*1.5)
        if not y3.empty: ax4.set_ylim(5e-4,  max(y3)*1.5)
        return (line1,line2) 

    if np.abs(nframes-np.size(phn, 0))<=2:
        anim = animation.FuncAnimation(fig, drawframe, frames=100, interval=100, blit=True)
        rc('animation', html=html_render)
        anim
    else: 
        print("nframes, phn mismatch > 2")    
    
    return 