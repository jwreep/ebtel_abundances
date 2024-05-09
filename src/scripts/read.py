"""
Reads the data from the ebtel++ output files

"""
import numpy as np

def read_ebtel_file(filename='ebtel++_results_file.txt'):
    """
    Reads in the output data file from an ebtel++ simulation
    
    Parameters
    ----------
    filename : `str`, default: `ebtel++_results_file.txt`
        The name of the data file
    
    Returns
    -------
    time:
        An array of the time-steps in the simulation [s]
    electron_temperature:
        A time-array of the coronal-averaged electron temperature [K]
    ion_temperature:
        A time-array of the coronal-averaged ion temperature [K]
    density:
        A time-array of the coronal-averaged density [cm**-3]
    electron_pressure:
        A time-array of the coronal-averaged electron pressure [dyn cm**-2]
    ion_pressure:
        A time-array of the coronal-averaged ion pressure [dyn cm**-2]
    velocity:
        A time-array of the bulk flow velocity [cm s**-1]
    heating_rate:
        A time-array of the coronal-averaged heating rate [erg cm**-3 s**-1]
    
    """
    f = open(filename, 'r')
    time = np.empty(0)
    electron_temperature = np.empty(0)
    ion_temperature = np.empty(0)
    density = np.empty(0)
    electron_pressure = np.empty(0)
    ion_pressure = np.empty(0)
    velocity = np.empty(0)
    heating_rate = np.empty(0)
    for line in f:
        line = line.strip()
        columns = line.split()
        time = np.append(time, float(columns[0]))
        electron_temperature = np.append(electron_temperature, float(columns[1]))
        ion_temperature = np.append(ion_temperature, float(columns[2]))
        density = np.append(density, float(columns[3]))
        electron_pressure = np.append(electron_pressure, float(columns[4]))
        ion_pressure = np.append(ion_pressure, float(columns[5]))
        velocity = np.append(velocity, float(columns[6]))
        heating_rate = np.append(heating_rate, float(columns[7]))     
        
    f.close()

    return time, electron_temperature, ion_temperature, density, electron_pressure, ion_pressure, velocity, heating_rate
