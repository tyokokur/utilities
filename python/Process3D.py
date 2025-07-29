import numpy as np, pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl, plotly.graph_objects as go
from Pha3D import Pha3D

class Process3D:
    ''' 
    kwargs : { fname, dims, fprefix, ( default: isomin, n_coarse, zmax, reflect_over ) }
    '''
    def __init__(self, **kwargs):
        pha3d = Pha3D(**kwargs)
        self.data = pha3d.get_vol(**kwargs)
        print('Data processed into self.data')
            
    def Set_camera(self, opt='d', d = 3.0, a = 25, zcenter = 0.0):
        '''
        'd'efault, 'x'z, 'y'z
        Distance from center
        Angle, if applicable
        Camera focal point
        '''
        
        match opt:
            case 'd': eye=dict(x=-d/np.sqrt(3), y=-d/np.sqrt(3), z=d/np.sqrt(3)) #default
            case 'x': eye=dict(x=0, y=-d*np.cos(np.pi/180*a), z=d*np.sin(np.pi/180*a)) # xz at given angle
            case 'y': eye=dict(x=d*np.cos(np.pi/180*a), y=0, z=d*np.sin(np.pi/180*a)) # yz at given angle
            case  _ : eye=dict(x=-d/np.sqrt(3), y=-d/np.sqrt(3), z=d/np.sqrt(3)) #default
            # eye=dict(x=d, y=0.0, z=0.0) # yz
            # eye=dict(x=0.0, y=-d, z=0.0) # xz
        
        self.camera = dict(
            up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z= zcenter),
            eye = eye
        )
        print('Camera set to self.camera')

    def Figure(self, 
               xrange=[-5, 5], xticks=[], 
               yrange=[-5, 5], yticks=[],
               zrange=[0, 15], zticks=[],
               write_html=True, fprefix = None
               ):
        xn, yn, zn = len(xticks), len(yticks), len(zticks)

        try: camera = self.camera
        except NameError: 
            print('Camera not set, doing default')
            self.Set_camera()

        scene = dict()

        if xn > 0:
            scene.update( 
                xaxis = dict(nticks=xn, range=xrange, title='',
                             ticks='outside',tickangle=0,tickwidth=1,ticklen=5,
                             ticktext= ['', '',''], tickvals= xticks, 
                             spikethickness=0,
                             zeroline=False, showgrid=False, backgroundcolor='white',
                             )
            )
        else: 
            scene.update(
                xaxis = dict(showticklabels=False, title='', zeroline=False, showgrid=False, backgroundcolor='white',), 
            )

            
        if yn > 0:
            scene.update( 
                yaxis = dict(nticks=yn, range=yrange, title='',
                             ticks='outside',tickangle=0,tickwidth=1,ticklen=5,
                             ticktext= ['', '',''], tickvals= yticks, 
                             spikethickness=0,
                             zeroline=False, showgrid=False, backgroundcolor='white',
                             )
            )
        else: 
             scene.update(
                 yaxis = dict(showticklabels=False, title='', zeroline=False, showgrid=False, backgroundcolor='white',), 
             )

        if zn > 0:
            scene.update(
                zaxis = dict(nticks=zn, range=zrange, title='',
                             ticks='outside',tickangle=0,tickwidth=1,ticklen=5,
                             ticktext= ['', '', ''], zticks, 
                             spikethickness=0,
                             zeroline=False, showgrid=False,backgroundcolor='white',
                             ) 
            )
        else: 
            scene.update(
                zaxis = dict(showticklabels=False, title='', zeroline=False, showgrid=False, backgroundcolor='white',), 
            )

        
        layout = go.Layout(
            autosize=False,
            font= dict(size=24, family='serif', color='black'),
            hovermode=False,
            scene = scene,
            scene_camera=self.camera,
            width=1200,
            height=800,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        fig = go.Figure(self.data, layout)
        fig.update_traces(showscale=False)

        if write_html:
            fname = fprefix+'pha_vol.html'
            f = open(fname, "w")
            f.close()
            with open(fname, 'a') as f:
                f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
            f.close()
            print('Wrote to {}'.format(fname))
                
            import webbrowser
            webbrowser.open(fname)
            print('Opening...')
        
        return fig