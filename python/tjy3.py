import pandas as pd, numpy as np, matplotlib.pyplot as plt
import tjy_udf as tjy
class Pha3D:
    """
        Class for reading and plotting 3D (xyz) density distributions 
        self.PHAXYZ[PHA, X, Y, Z] contains all information in 3D arrays with shape (self.nx, self.ny, self.nz)
        self.plot_proj() for plotting 2D projection of density distributions (e.g., x-y projection at specified z)
    """
    def __init__(self, fname, dims, discs=(0.25,0.25,0.10), blocks=[1], silent=True):
        """
        fname: filename containing density distribution; dims: (Lx, Ly, Lz) in nm units; discs: (dx, dy, dz) in nm units;
        blocks: [# of blocks in polymer]; silent: bool, for printing end of init (after _readPha)
        """
        import math
        (self.lx, self.ly, self.lz), (self.dx, self.dy, self.dz) = dims, discs
        self.nxnynz = (self.nx, self.ny, self.nz) = (round(self.lx / self.dx), round(self.ly /self.dy), round(self.lz / self.dz))
        
        self.lx, self.ly, self.lz = self.nx*self.dx, self.ny*self.dy, self.nz*self.dz # update
        self.size   = np.prod(self.nxnynz)
        self.blocks = blocks
        self._readPha(fname, silent=silent)
        
    def _readPha(self, fname, silent=True):
        from urllib.error import HTTPError
        
        a=b=c = 1
        names = ['rx', 'ry', 'rz', 'phA']
        for j in range(len(self.blocks)):
            names += ['phA_T{:d}'.format(a)] +  ['*'*b]+ ['ph{:d}'.format(c+i) for i in range(self.blocks[j])] + ['*'*(b+1)]
            a += 1
            b += 2
            c += self.blocks[j]
        names += ['phB']
        try: df = pd.read_csv(fname, sep="\s+", skiprows=0, names=names)
        except HTTPError: 
            print('{} not found'.format(fname))
            return
    
        X, Y, Z, PHA, PHB = df.rx, df.ry, df.rz, df.phA, df.phB
        # TODO: Insert code for ph_i here

        if (self.size != len(PHA)): print('\nERROR: NxNyNz ({:d}) != PHA ({:d})\n'.format(self.size, len(PHA)))
        self.PHAXYZ = np.array(PHA).reshape(*self.nxnynz), np.array(X).reshape(*self.nxnynz), np.array(Y).reshape(*self.nxnynz), np.array(Z).reshape(*self.nxnynz)

        if not silent: print('_readPha done, max = {}'.format(PHA.max()))
        return 
        
    def plot_proj(self, which='both', yslice=0, zslice=0, zmax=None, show_slice='both', levels=np.array([]), 
                  reflect_box=True, show_box=True, ins_frame=True, cmap=None, fig=None, wspace=1.75,
                  show_cbar=True,cbar_ticks=[], xy_xticks=[], xy_yticks=[]):
        '''
        which: {'both', 'xy', 'xz'}; yslice & zslice: float, in units of nm; zmax: float, in units of nm; show_slice: {'y', 'z', 'both'}, mark slice of projection on other heatmap; 
        reflect_box: bool, for visualizing half-space (around Lx, Ly) results;  ins_frame: bool, for extending periodic data for clean visualizing; 
        cmap: plt.cm.{}; fig: feed some other figure in
        '''
        PHA_3D, X_3D, Y_3D, Z_3D = self.PHAXYZ[0], self.PHAXYZ[1], self.PHAXYZ[2], self.PHAXYZ[3]
        import numpy as np, matplotlib.pyplot as plt
        from mpl_toolkits import axes_grid1
        if not zmax  : zmax = self.lz-self.dz
        if not levels.any(): levels = np.arange(0, 1.01, 0.01)
        if not cmap  : cmap = plt.cm.jet
        if not fig   : fig  = plt.figure(figsize=(plt.rcParams['figure.figsize'][0]*wspace, plt.rcParams['figure.figsize'][1]))
        bools = {'reflect_box':reflect_box, 'show_box':show_box, 'ins_frame':ins_frame}
        kws   = {'levels':levels, 'cmap':cmap} 

        if zmax > self.lz-self.dz: 
            print('\n\nERROR: zmax TOO LARGE: {:.2f} > {:.2f}\n\n'.format(zmax, self.lz-self.dz))
        if PHA_3D.max() > np.max(levels): 
            print('\n\nERROR: LEVELS INSUFFICIENT: {:.5f} > {:.5f}\n\n'.format(PHA_3D.max(), np.max(levels)))
            return
        
        # Initialize figure
        if which=='both': 
            jSLICE, kSLICE = int(yslice / self.dy), int(zslice / self.dz)
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            tjy.ticks([ax1, ax2])
        elif which=='xy': 
            kSLICE = int(zslice / self.dz)
            ax2 = fig.add_subplot(111)
            tjy.ticks()
        elif which=='xz': 
            jSLICE = int(yslice / self.dy)
            ax1 = fig.add_subplot(111)
            tjy.ticks()
        else:
            print("\n\nERROR: INVALID which OPTION ('both', 'xy', 'yz')\n\n")
            return
 
        if self.nx > 1 and self.ny > 1:
            if which=='xz' or which=='both': FIL = self._plotxz(ax1, jSLICE, zmax, kws, **bools)
            if which=='xy' or which=='both': FIL = self._plotxy(ax2, kSLICE, kws, **bools, xy_yticks=xy_yticks, xy_xticks=xy_xticks)
        else:
            print("\n\nERROR: Nx or Ny equal to one: Nx = {:d}, Ny = {:d}\n\n".format(self.nx, self.ny))
            return

        if show_cbar:
            from matplotlib.ticker import FuncFormatter
            # Shared height colorbar: https://stackoverflow.com/questions/18195758/set-matplotlib-colorbar-size-to-match-graph
            im, aspect, pad_fraction = FIL[0], 20, 2
            divider = axes_grid1.make_axes_locatable(im.axes)
            width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
            pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
            current_ax = plt.gca()
            cax = divider.append_axes("right", size=width, pad=pad)
            plt.sca(current_ax)
            if len(cbar_ticks)!=0: cbar = im.axes.figure.colorbar(im, cax=cax, ticks=cbar_ticks)
            else:# cbar = im.axes.figure.colorbar(im, cax=cax)
                fmt = lambda x, pos: '{:.2f}'.format(x)
                cbar = im.axes.figure.colorbar(im, cax=cax, format=FuncFormatter(fmt))
            # cbar.ax.set_ylabel(r'$\phi_p$')
            tjy.ticks([cbar.ax])
        
        return fig
    
    def _plotxz(self, ax, jSLICE, zmax, kws, reflect_box=True, show_box=True, ins_frame=True):
        plt.sca(ax)
        PHA_3D, X_3D, Y_3D, Z_3D = self.PHAXYZ[0], self.PHAXYZ[1], self.PHAXYZ[2], self.PHAXYZ[3]
        XX, ZZ, PHA_Y = X_3D[:,jSLICE,:]+self.dx, Z_3D[:,jSLICE,:], PHA_3D[:,jSLICE,:]# '+'s for centering on Lx instead of Lx-dx
        filter_Z = ZZ < zmax+self.dz
        new_nz = filter_Z[0,:].sum()
        XX, ZZ, PHA_Y = XX[filter_Z].reshape(self.nx, new_nz), ZZ[filter_Z].reshape(self.nx, new_nz), PHA_Y[filter_Z].reshape(self.nx, new_nz)

        FIL = [plt.contourf(XX, ZZ, PHA_Y, **kws)]
        if reflect_box: 
            # plt.plot([self.lx]*2, [0,zmax], ':k')
            FIL.append(plt.contourf(XX[::-1]+(self.nx-1)*self.dx, ZZ, PHA_Y, **kws))

        if ins_frame:
            FRAX, FRAZ, FRAP = self._insFrame(0, self.lx, self.dx, 0, zmax, self.dz, PHA_Y, option='w')
            FIL.append(plt.contourf(FRAX, FRAZ, FRAP, **kws))
            if reflect_box: 
                FRAX, FRAZ, FRAP = self._insFrame(self.lx, 2*self.lx, self.dx, 0, zmax, self.dz, PHA_Y, option='e')
                FIL.append(plt.contourf(FRAX, FRAZ, FRAP, **kws))

        plt.title(r'$y={:.2f}$'.format(jSLICE*self.dy)+r'$~\mathrm{nm}$', fontsize=22)
        plt.gca().set(xlabel='$x\ [\mathrm{nm}]$', ylabel='$z\ [\mathrm{nm}]$', aspect='equal')
        if reflect_box: plt.gca().set(xlim=(0,2*self.lx), ylim=(0,zmax))
        else:           plt.gca().set(xlim=(0,self.lx),   ylim=(0,zmax))
        return FIL

    def _plotxy(self, ax, kSLICE, kws, reflect_box=True, show_box=True, ins_frame=True, xy_xticks=[], xy_yticks=[]):
        plt.sca(ax)
        PHA_3D, X_3D, Y_3D, Z_3D = self.PHAXYZ[0], self.PHAXYZ[1], self.PHAXYZ[2], self.PHAXYZ[3]
        XX, YY, PHA_Z = X_3D[:,:,kSLICE]+self.dx, Y_3D[:,:,kSLICE]+self.dy, PHA_3D[:,:,kSLICE] # '+'s for centering on Lx, Ly instead of Lx-dx, Ly-dy

        FIL = [plt.contourf(XX, YY, PHA_Z, **kws)] # Main
        if reflect_box: 
            FIL.append(plt.contourf(XX, np.flip(YY,1)+(self.ny-1)*self.dy, PHA_Z, **kws)) # NW corner
            FIL.append(plt.contourf(np.flip(XX,0)+(self.nx-1)*self.dx, YY, PHA_Z, **kws)) # SE corner
            FIL.append(plt.contourf(np.flip(XX,0)+(self.nx-1)*self.dx, np.flip(YY,1)+(self.ny-1)*self.dy, PHA_Z, **kws)) # NE corner
            # plt.plot([self.lx]*2, [0,2*self.ly], ':k') # Left-right
            # plt.plot([0, 2*self.lx], [self.ly]*2, ':k') # Top-bot

        if ins_frame: 
            FRAX, FRAY, FRAP = self._insFrame(0, self.lx, self.dx, 0, self.ly, self.dy, PHA_Z)
            FIL.append(plt.contourf(FRAX, FRAY, FRAP, **kws))
            if reflect_box:
                FRAX, FRAY, FRAP = self._insFrame(0, self.lx, self.dx, self.ly, 2*self.ly, self.dy, PHA_Z, option='nw')
                FIL.append(plt.contourf(FRAX, FRAY, FRAP, **kws))
                FRAX, FRAY, FRAP = self._insFrame(self.lx,2*self.lx, self.dx, self.ly,2*self.ly, self.dy, PHA_Z, option='ne')
                FIL.append(plt.contourf(FRAX, FRAY, FRAP, **kws))
                FRAX, FRAY, FRAP = self._insFrame(self.lx,2*self.lx, self.dx, 0, self.ly, self.dy, PHA_Z, option='se')
                FIL.append(plt.contourf(FRAX, FRAY, FRAP, **kws))

        plt.title(r'$z={:.2f}$'.format(kSLICE*self.dz)+r'$~\mathrm{nm}$', fontsize=22)
        plt.gca().set(xlabel='$x\ [\mathrm{nm}]$', ylabel='$y\ [\mathrm{nm}]$', aspect='equal')
        if reflect_box: plt.gca().set(xlim=(0,2*self.lx), ylim=(0,2*self.ly))
        else:           plt.gca().set(xlim=(0,self.lx), ylim=(0,self.ly))           
        if len(xy_yticks) != 0: plt.gca().set_yticks(xy_yticks)
        if len(xy_xticks) != 0: plt.gca().set_xticks(xy_xticks)
        return FIL
    
    def _insFrame(self, xstart, xend, xstep, ystart, yend, ystep, PHA, option='sw'):
        """
        Insert frame of width dx,dy for periodic density distributions
        Option: {'sw', 'nw', 'se', 'ne', 'w', 'e'}
        """
        import numpy as np
        FRAX, FRAY = np.meshgrid(np.arange(xstart,xend+xstep,xstep), np.arange(ystart,yend+ystep,ystep), indexing='ij')
        FRAP = np.zeros(FRAX.shape) 

        FRAP[0, 0] = PHA[0,0] # New corner = old corner
        if option == 'w' or option == 'e': 
            FRAP[1:,:] = PHA # Copy
            FRAP[0,:] = PHA[1,:] # Periodic, share 0th val
        else: 
            FRAP[1:,1:] = PHA     # Copy
            FRAP[0,1:] = PHA[1,:] # Periodic, share 0th val
            FRAP[1:,0] = PHA[:,1] # Periodic, share 0th val
        
        if   option=='sw' or option=='w': pass
        elif option=='nw':
            FRAY = np.flip(FRAY,1)
        elif option=='se' or option=='e':
            FRAX = np.flip(FRAX,0)
        elif option=='ne':
            FRAY = np.flip(FRAY,1)
            FRAX = np.flip(FRAX,0)
            
        return FRAX, FRAY, FRAP
    
    def mask_wa(self, fname_in, fname_out, amps=(0.5,0.5,0.7), pers=(2*np.pi/1, 2*np.pi/1, 2*np.pi/1), shifts=(0,0,0), ph_inplace=True):
        a=b=c = 1
        names = []
        for j in range(len(self.blocks)):
            names += ['*'*b]+ ['w{:d}'.format(c+i) for i in range(self.blocks[j])] + ['*'*(b+1)]
            b += 2
            c += self.blocks[j]
        names += ['wB', 'eta', 'pot']
        try: df = pd.read_csv(fname_in, sep="\s+", skiprows=0, names=names)
        except HTTPError: 
            print('{} not found'.format(fname_in))
            return
        
        wa = np.array(df.w1).reshape(np.shape(self.PHAXYZ[0]))
        mask = np.ones(np.size(self.PHAXYZ[0])).reshape(np.shape(self.PHAXYZ[0]))
        
        xamp,yamp,zamp = amps
        xper,yper,zper = pers
        xshift,yshift,zshift = shifts
        
        tX, tY, tZ = self.PHAXYZ[1], self.PHAXYZ[2], self.PHAXYZ[3]
        for zind in range(len(tZ[0,0,:])):
            for xind in range(len(tX[:,0,0])): 
                for yind in range(len(tY[0,:,0])):
                    xyzi = xind, yind, zind
                    x, y, z = tX[xyzi], tY[xyzi], tZ[xyzi]
                    mask[xyzi] = (xamp*np.cos([x*xper+xshift]) + yamp*np.cos([y*yper+yshift]) + zamp*np.cos([z*zper+zshift])+(xamp+yamp+zamp))/2/(xamp+yamp+zamp)
                    if ph_inplace: npha3d.PHAXYZ[0][xyzi] *= mask[xyzi]
                    wa[xyzi] *= mask[xyzi]
        df.w1 = wa.flatten()
        df.to_csv(fname_out,header=False,index=False,sep=" ",float_format="%10.5e")
        return
