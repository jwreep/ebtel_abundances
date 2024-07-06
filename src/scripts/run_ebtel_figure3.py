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

# nanoflare trains
lengths = ['40', '80']
heat = ['0.01']
duration = ['20']
for L in lengths:
    for H in heat:
        for t in duration:
            vfile = 'var_train_L'+L+'_H'+H+'_t'+t+'.txt'
            pfile = 'pho_train_L'+L+'_H'+H+'_t'+t+'.txt'
            cfile = 'cor_train_L'+L+'_H'+H+'_t'+t+'.txt'

            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'variable',
                                    heating_rate = [H, H, H, H, H], 
                                    heating_duration = [t, t, t, t, t],
                                    heating_start = ['0','300','600','900','1200'],
                                    output_filename = paths.figure3 / vfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
            
            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'photospheric',
                                    heating_rate = [H, H, H, H, H], 
                                    heating_duration = [t, t, t, t, t],
                                    heating_start = ['0','300','600','900','1200'],
                                    output_filename = paths.figure3 / pfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
            
            os.chdir(paths.data)
            write_new_configuration(initial_lines, length = L, radiation = 'coronal',
                                    heating_rate = [H, H, H, H, H], 
                                    heating_duration = [t, t, t, t, t],
                                    heating_start = ['0','300','600','900','1200'],
                                    output_filename = paths.figure3 / cfile)
            os.chdir(paths.ebtel_root)
            subprocess.run(["bin/ebtel++.run"])
