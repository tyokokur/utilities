def ticks(axs = []):
    import matplotlib.pyplot as plt, numpy as np
    
    kw = {'fontname': 'serif'}
    if not np.any(axs): 
        plt.yticks(**kw) 
        plt.xticks(**kw)
    
    dims = np.shape(axs)
    try:
        if dims[1] != None: 
            for i in range(dims[0]): 
                for j in range(dims[1]):
                    for k in axs[i,j]: 
                        plt.sca(k)
                        plt.yticks(**kw)
                        plt.xticks(**kw)
            return
    except:            
        for i in axs: 
            plt.sca(i)
            plt.yticks(**kw)
            plt.xticks(**kw)
        return
        
def plot_pha(read_list, labs=[], b0=1.0, 
             double=True,
             y1_start=0, y1_end=1.00, x1_start=0, x1_end=None, 
             y2_start=None, y2_end=None, x2_start=None, x2_end=None,
             block1 = None, block2 = None): 
    
    from matplotlib import animation, rc
    import numpy as np, pandas as pd, matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    from matplotlib import ticker
   
    # Defaults
    if not labs:     labs     = read_list
    if not x2_start: x2_start = x1_start
    if not x2_end:   x2_end   = x1_end
    if not y2_start: y2_start = y1_start
    if not y2_end:   y2_end   = y1_end
    
    div = [b0]*len(read_list) #b0
    block_Num = len(read_list)
    block_Ni = [[4,7]]*len(read_list) 
    colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
    colors_i = [colors[i] for i in range(len(read_list))]

    if double: fig, axs = plt.subplots(1,2, figsize=(10,5)) 
    else: fig, ax = plt.subplots(1,1, figsize=(7,5)) 

    for k in range(len(read_list)):
      block_Nik = block_Ni[k]
      a = 1
      b = 1
      c = 1
      names = ['rx', 'phA']
      for j in range(len(block_Nik)):
        names += ['phA_T{:d}'.format(a)] +  ['*'*b]+ ['ph{:d}'.format(c+i) for i in range(block_Nik[j])] + ['*'*(b+1)]
        a += 1
        b += 2
        c += block_Nik[j]

      names += ['phB']
      df = pd.read_csv(read_list[k], sep="\s+", skiprows=0, names=names)
      Nx = len(df.index)

      for i in range(len(block_Nik)*2):
        names.remove('*'*(i+1))
        df = df.drop('*'*(i+1),axis=1)

      Nx = len(df.index)
      rows = range(0, Nx)

      rows = range(0, Nx)

      phAr = pd.DataFrame(data=None, index=rows, columns=range(2), dtype=None, copy=False)
      phAr = phAr.fillna(0) # with 0s rather than NaNs
      phAT = pd.DataFrame(data=None, index=rows, columns=range(1+len(block_Nik)), dtype=None, copy=False)
      phAT = phAT.fillna(0) # with 0s rather than NaNs
      ph1r = pd.DataFrame(data=None, index=rows, columns=range(1+sum(block_Nik)), dtype=None, copy=False)
      ph1r = ph1r.fillna(0) # with 0s rather than NaNs

      phB = pd.DataFrame(data=None, index=rows, columns=range(2), dtype=None, copy=False)
      phB = phB.fillna(0) # with 0s rather than NaNs

      ph1r = df.loc[:, ['ph{:d}'.format(i+1) for i in range(sum(block_Nik))]]
      ph1r.insert(0, 'rx', df.iloc[:,0])

      phAT = df.loc[:, ['phA_T{:d}'.format(i+1) for i in range(len(block_Nik))]]
      phAT.insert(0, 'rx', df.iloc[:,0])

      for i in range(Nx):
        phAr.iloc[i, 0] = df.iloc[i,0]
        phAr.iloc[i, 1] = df.iloc[i,1] 
        phB.iloc[i, 0] = df.iloc[i, 0]
        phB.iloc[i, 1] = df.iloc[i, 2 + sum(block_Nik) + len(block_Nik)] 

      rshi = pd.DataFrame(data=None,  index=rows, columns=range(1), dtype=None, copy=False)
      lshi = pd.DataFrame(data=None,  index=rows, columns=range(1), dtype=None, copy=False)

      # Plot total density (zorder 3)
      rshi.iloc[1:,0] = phAr.iloc[1:,0] # Change here if shift wanted; can change udf inputs if needed
      lshi.iloc[1:,0] = phAr.iloc[1:,0]
    
      if double: 
          axs[0].plot(np.multiply(rshi.iloc[1:,0], div[k]), phAr.iloc[1:,1], color = colors[k], zorder = 3, alpha=1.0)
          axs[1].plot(np.multiply(lshi.iloc[1:,0], div[k]), phAr.iloc[1:,1], color = colors[k], zorder = 3, alpha=1.0, label=labs[k])
      else: 
          ax.plot(np.multiply(rshi.iloc[1:,0], div[k]), phAr.iloc[1:,1], color = colors[k], zorder = 3, alpha=1.0, label=labs[k])

      # Plot chain types (zorder 2)
      step = 1
      if double:
          for j in range(len(block_Nik)):
            axs[0].plot(np.multiply(phAT.iloc[1:,0], div[k]), phAT.iloc[1:,j+1], '-',  zorder=2, color=lighten_color(colors_i[k], amount=0.50),label='_Total')

            #Plot block densities (zorder 3)
            for i in range(block_Nik[j]):
              if (i == block1): axs[0].plot(np.multiply(ph1r.iloc[1:,0], div[k]), ph1r.iloc[1:,i+step], '--',  zorder=3, color=lighten_color(colors_i[k], amount=0.60),label='_Block')
              if (i == block2): axs[1].plot(np.multiply(ph1r.iloc[1:,0], div[k]), np.multiply(ph1r.iloc[1:,i+step],1), '--',  zorder=3, color=lighten_color(colors_i[k], amount=0.60),label='_Block')
                
            step += block_Nik[j]
      else: 
          for j in range(len(block_Nik)):
            ax.plot(np.multiply(phAT.iloc[1:,0], div[k]), phAT.iloc[1:,j+1], '-',  zorder=2, color=lighten_color(colors_i[k], amount=0.50),label='_Total')

            #Plot block densities (zorder 3)
            for i in range(block_Nik[j]):
              if (i == block1): ax.plot(np.multiply(ph1r.iloc[1:,0], div[k]), ph1r.iloc[1:,i+step], '--',  zorder=3, color=lighten_color(colors_i[k], amount=0.60),label='_Block')

            step += block_Nik[j]

    conf = [Patch(facecolor=i, edgecolor='k', lw=1.5) for i in colors_i]
    conf += [
              Line2D([0], [0], color='k', ls='-'),
              Line2D([0], [0], color='k', ls='--'),
            ]
    if double: 
        for i in range(2):
          axs[0].set_ylabel(r'$\bf{\langle\phi(z)\rangle}_{xy}$')
          axs[i].set_xlabel("Length (z, nm)")
          axs[i].set_yscale('linear')

        axs[0].set_ylim(y1_start, y1_end)
        axs[1].set_ylim(y2_start, y2_end)
        axs[0].set_xlim(x1_start, x1_end)
        axs[1].set_xlim(x2_start, x2_end)

        leg = axs[1].legend(loc=1)

    else: 
        plt.ylabel(r'$\bf{\langle\phi(z)\rangle}_{xy}$')
        plt.xlabel("Length (z, nm)")
        plt.yscale('linear')
        plt.ylim(y1_start, y1_end)
        plt.xlim(x1_start, x1_end)
        leg = plt.legend(loc=1)
        
    #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)
    if double: ticks(axs)
    else: ticks()
    plt.show()
    return
    
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

def H_find(filename, alg, b0=1.0, thresh=1e-04):
    ## Alg options: thresh, maxpt, norm
    import pandas as pd, numpy as np

    df = pd.read_csv(filename, sep="\s+", skiprows=0)
    Nx = len(df.index)
    rows = range(0, Nx)

    phA = pd.DataFrame(data=None, index=rows, columns=range(2), dtype=None, copy=False)
    phA = phA.fillna(0) # with 0s rather than NaNs

    for i in range(Nx):
        phA.iloc[i, 0] = df.iloc[i,0] * b0
        phA.iloc[i, 1] = df.iloc[i,1] 

    if alg == 'thresh': 
        diff = 100
        for i in range(Nx):
            if np.isnan(phA.iloc[i, 1]): return 0
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
    
    if alg == 'maxpt': 
        dx = (phA.iloc[1,0] - phA.iloc[0, 0]) #Assuming equally spaced
        maxpt = np.argmax(phA.iloc[:,1])

        sum = 0
        for i in range(maxpt, np.max(phA.index)):
            sum += phA.iloc[i, 1]
        sum *= dx 
        rGibbs =  sum / phA.iloc[maxpt, 1] + phA.iloc[maxpt, 0]
        
        return rGibbs
    
    if alg == 'norm':
        dx = (phA.iloc[1,0] - phA.iloc[0, 0]) #Assuming equally spaced

        sum = 0
        sum2 = 0
        for i in range(0, np.max(phA.index)):
            sum += phA.iloc[i, 1]
            sum2 += phA.iloc[i, 1] * phA.iloc[i, 0]
        sum *= dx 
        sum2 *= dx
        rGibbs =  2 * sum2 / sum 
        
        return rGibbs

    print('Alg not recognized')
    return

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

def plot_anim(fname, simname='SIM.dat', lx=100, xstart=0, xend=0, dx=17/150, b0=1.0, html_render='jshtml'):
    from matplotlib import animation, rc
    import numpy as np, pandas as pd, matplotlib.pyplot as plt
    from IPython.display import HTML, display

    if lx == 100 or lx == 300 or lx == 275 or lx == 350: nx = int(np.floor(lx / dx))
    else: nx = int(np.ceil(lx/dx))
    if xend == 0: xend = lx # Default behavior

    ## Unknown bug: 
    # Maybe caused by (lx-dx)/b0; only works when b0 = 1.0
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
    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot(1,2,1)
    ax2 = plt.subplot(2,4,3)
    ax3 = plt.subplot(2,4,4)
    ax4 = plt.subplot(2,2,4)
    plt.subplots_adjust(hspace=0.40)
    plt.subplots_adjust(wspace=0.35)

    # set up the subplots as needed
    ax1.set_xlim(( xstart, xend))            
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
        display(HTML(anim.to_jshtml()))
    else: 
        print("nframes, phn mismatch > 2")    
    
    return 