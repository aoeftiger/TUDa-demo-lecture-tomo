#!/usr/bin/env python
import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.random.seed(0)

import matplotlib
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

import seaborn as sns
sns.set_context('talk', font_scale=1.2, rc={'lines.linewidth': 3})
sns.set_style('ticks',
              {'grid.linestyle': 'none', 'axes.edgecolor': '0',
               'axes.linewidth': 1.2, 'legend.frameon': True,
               'xtick.direction': 'out', 'ytick.direction': 'out',
               'xtick.top': True, 'ytick.right': True,
              })

# custom plot functions
def plot_mp(z, dp, rfb):
    dpmax = rfb.dp_max(rfb.z_ufp_separatrix)
    zz = np.linspace(rfb.z_left, rfb.z_right, num=1000)
    Z, DP = np.meshgrid(zz, np.linspace(-dpmax*1.1, dpmax*1.1, num=100))
    H = rfb.hamiltonian(Z, DP)
    plt.contour(Z, DP, H, 20, cmap=plt.get_cmap('coolwarm_r'))
    # plt.scatter(z, dp, alpha=0.6)
    my_cmap = plt.get_cmap('hot_r')
    try:
        my_cmap = my_cmap.copy()
    except AttributeError:
        pass
    my_cmap.set_under('w',1)
    plt.hist2d(z, dp, bins=40, cmap=my_cmap)
    plt.plot(zz, rfb.separatrix(zz), c='purple', lw=2)
    plt.plot(zz, -rfb.separatrix(zz), c='purple', lw=2)
    plt.xlim(rfb.z_left, rfb.z_right)
    plt.ylim(-dpmax*1.1, dpmax*1.1)
    plt.colorbar().set_label('# particles', fontsize=20)
    plt.xlabel(r'$z$', fontsize=20)
    plt.ylabel(r'$\delta$', fontsize=20)
#    plt.title('particle generation', fontsize=20)
    return zz, Z, DP
