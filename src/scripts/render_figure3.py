"""
Script to render the data into Figure 3

"""
import os
import paths
from plot import plot_figures
from read import read_ebtel_file

# Call the script to run the simulations for Figure 3
os.system("python run_ebtel_figure3.py")

# Let's calculate a couple of nanoflare trains for comparison
lengths = ['40', '80']
heat = ['0.01']
duration = ['20']
for L in lengths:
    for H in heat:
        for t in duration:
            vfile = 'var_train_L'+L+'_H'+H+'_t'+t+'.txt'
            pfile = 'pho_train_L'+L+'_H'+H+'_t'+t+'.txt'
            cfile = 'cor_train_L'+L+'_H'+H+'_t'+t+'.txt'
            
            t_v, T_e_v, T_i_v, n_v, P_e_v, P_i_v, v_v, Q_v = read_ebtel_file(filename=paths.data / vfile)
            t_p, T_e_p, T_i_p, n_p, P_e_p, P_i_p, v_p, Q_p = read_ebtel_file(filename=paths.data / pfile)
            t_c, T_e_c, T_i_c, n_c, P_e_c, P_i_c, v_c, Q_c = read_ebtel_file(filename=paths.data / cfile)
            
            time = [t_v, t_p, t_c]
            temperature = [T_e_v, T_e_p, T_e_c]
            density = [n_v, n_p, n_c]
            
            plot_figures(time, temperature, density, L, H, t, 
                            filename = 'train_L'+L+'_H'+H+'_t'+t+'.png',
                            xlim = [0, 40])
