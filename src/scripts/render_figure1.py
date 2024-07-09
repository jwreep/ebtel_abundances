"""
Script to render the data into Figure 1

"""
# import os
import paths
from plot import plot_figures
from read import read_ebtel_file

# Call the script to run the simulations for Figure 1
# os.system("python "+ str(paths.scripts / "run_ebtel_figure1.py"))

# Let's calculate some cases with single heating events first
lengths = ['40']
heat = ['1.0','0.1','0.03','0.01']
duration = ['20']

for L in lengths:
    for H in heat:
        for t in duration:
            vfile = 'var_L'+L+'_H'+H+'_t'+t+'.txt'
            pfile = 'pho_L'+L+'_H'+H+'_t'+t+'.txt'
            cfile = 'cor_L'+L+'_H'+H+'_t'+t+'.txt'

            t_v, T_e_v, T_i_v, n_v, P_e_v, P_i_v, v_v, Q_v = read_ebtel_file(filename=paths.figure1 / vfile)
            t_p, T_e_p, T_i_p, n_p, P_e_p, P_i_p, v_p, Q_p = read_ebtel_file(filename=paths.figure1 / pfile)
            t_c, T_e_c, T_i_c, n_c, P_e_c, P_i_c, v_c, Q_c = read_ebtel_file(filename=paths.figure1 / cfile)
            
            time = [t_v, t_p, t_c]
            temperature = [T_e_v, T_e_p, T_e_c]
            density = [n_v, n_p, n_c]
            
            if H == '0.01':
                show_legend = True
            else:
                show_legend = False
            
            plot_figures(time, temperature, density, L, H, t, show_legend=show_legend)