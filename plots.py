from parameters import *
import numpy as np

def plot_with_spikes(ax, monitor, n, 
                     subsampling=1,
                     shift=0, color='k'):
    ax.plot(monitor.t[::subsampling]/ms,
            monitor.v[n][::subsampling]/mV+shift,
            '-', color=color)

    # find spikes and plot them
    ispikes = np.flatnonzero((monitor.v[n][:-1]/mV>-55) & (monitor.v[n][1:]/mV==-70))
    for s in monitor.t[ispikes]:
        ax.plot([s/ms,s/ms], [Vt/mV+shift, shift], ':', color=color)
