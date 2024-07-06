"""
Configure and run ebtel++ to produce the simulation data

It is required that ebtel++ is installed in order to run this
code.  
"""
import os
import subprocess
import paths
from configure import read_initial_configuration, write_new_configuration

initial_lines = read_initial_configuration()

# single heating events
lengths = ['80']
heat = ['1.0','0.1','0.03','0.01']
duration = ['20']

for L in lengths:
    for H in heat:
        for t in duration:
            vfile = 'var_L'+L+'_H'+H+'_t'+t+'.txt'
            pfile = 'pho_L'+L+'_H'+H+'_t'+t+'.txt'
            cfile = 'cor_L'+L+'_H'+H+'_t'+t+'.txt'
            
            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'variable',
                                    heating_rate = [H], heating_duration = [t], 
                                    output_filename = paths.figure2 / vfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
            
            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'photospheric',
                                    heating_rate = [H], heating_duration = [t], 
                                    output_filename = paths.figure2 / pfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
            
            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'coronal',
                                    heating_rate = [H], heating_duration = [t], 
                                    output_filename = paths.figure2 / cfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
