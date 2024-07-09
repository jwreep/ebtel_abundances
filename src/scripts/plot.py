"""
Plots the temperature, density, and abundance factor from an ebtel++ simulation

"""
import paths
import numpy as np
from matplotlib import pyplot as plt

def plot_figures(time, temperature, density, L, H, t, filename=None, xlim=None, show_legend=False):
    """
    Plot the temperature, density, and abundance factor as a function of time for
    a given set of simulations
    
    Parameters
    ----------
    time : 
        The time-step of a given simulation
    temperature : 
        The coronal-averaged electron temperature [K] 
    density : 
        The coronal-averaged density [cm**-3]
    L : `str`
        The loop length [Mm]
    H : `str`
        The maximum heating rate [erg s**-1 cm**-3]
    t : `str`
        The total duration of a heating pulse [s]
    filename : `str`, default: `None`
        Format for the filename of each figure
    xlim : 
        The limits of the x-axis
    
    Returns
    -------
    None

    """
    if filename is None:
        filename = 'L'+L+'_H'+H+'_t'+t+'.png'

    plt.figure(0)
    plt.plot(time[0][:]/60., temperature[0][:]/1e6, label='Time variable')
    plt.plot(time[1][:]/60., temperature[1][:]/1e6, label='Photospheric', linestyle='dashed')
    plt.plot(time[2][:]/60., temperature[2][:]/1e6, label='Coronal', linestyle='dashed')
    plt.ylabel('Electron Temperature [MK]', fontsize=14)
    plt.xlabel('Time [min]', fontsize=14)
    plt.title(r'Length = '+L+' Mm, Heat = '+H+' erg s$^{-1}$ cm$^{-3}$, time = '+t+' s')
    plt.grid('-')
    if xlim is not None:
        plt.xlim(xlim)
    if show_legend:
        plt.legend(fontsize=18)
    plt.savefig(paths.figures / ('temperature_' + filename), dpi=300)   
    plt.close()

    plt.figure(1)
    plt.plot(time[0][:]/60., density[0][:]/1e8, label='Time variable')
    plt.plot(time[1][:]/60., density[1][:]/1e8, label='Photospheric', linestyle='dashed')
    plt.plot(time[2][:]/60., density[2][:]/1e8, label='Coronal', linestyle='dashed')
    plt.ylabel(r'Density [$10^{8}$ cm$^{-3}$]', fontsize=14)
    plt.xlabel('Time [min]', fontsize=14)
    plt.title(r'Length = '+L+' Mm, Heat = '+H+' erg s$^{-1}$ cm$^{-3}$, time = '+t+' s')
    plt.grid('-')
    if xlim is not None:
        plt.xlim(xlim)
    plt.savefig(paths.figures / ('density_' + filename), dpi=300)
    plt.close()

    # the abundance factor is not output from ebtel++, so we recalculate it here
    initial_af = 4.0
    af = 1.0 + (initial_af - 1.0) * (density[0][0] / density[0][:]);
    max_n = density[0][0]
    for i in range(len(af)):
        if density[0][i] > max_n:
            max_n = density[0][i]
        af[i] = 1.0 + (initial_af - 1.0) * (density[0][0] / max_n);

    plt.figure(2)
    plt.plot(time[0][:]/60., af[:], label='Time variable', )
    plt.plot(time[1][:]/60., np.full(len(time[1][:]), 1.0), label='Photospheric', linestyle='dashed')
    plt.plot(time[2][:]/60., np.full(len(time[2][:]), 4.0), label='Coronal', linestyle='dashed')
    plt.ylabel(r'Abundance Factor', fontsize=14)
    plt.xlabel('Time [min]', fontsize=14)
    plt.title(r'Length = '+L+' Mm, Heat = '+H+' erg s$^{-1}$ cm$^{-3}$, time = '+t+' s')
    plt.ylim(0,5)
    plt.grid('-')
    if xlim is not None:
        plt.xlim(xlim)
    plt.savefig(paths.figures / ('abundance_' + filename), dpi=300)
    plt.close()