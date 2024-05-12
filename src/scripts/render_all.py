"""
Script to render the data into figure data

"""
import os
import paths
from plot import plot_figures
from read import read_ebtel_file

# Call the script to run all of the simulations
os.system("python "+ str(paths.scripts / "run_all_ebtel.py"))

# Plot cases with single heating events first
lengths = ['40', '80']
heat = ['1.0','0.1','0.03','0.01']
duration = ['20']

for L in lengths:
    for H in heat:
        for t in duration:
            vfile = 'var_L'+L+'_H'+H+'_t'+t+'.txt'
            pfile = 'pho_L'+L+'_H'+H+'_t'+t+'.txt'
            cfile = 'cor_L'+L+'_H'+H+'_t'+t+'.txt'

            t_v, T_e_v, T_i_v, n_v, P_e_v, P_i_v, v_v, Q_v = read_ebtel_file(filename=paths.data / vfile)
            t_p, T_e_p, T_i_p, n_p, P_e_p, P_i_p, v_p, Q_p = read_ebtel_file(filename=paths.data / pfile)
            t_c, T_e_c, T_i_c, n_c, P_e_c, P_i_c, v_c, Q_c = read_ebtel_file(filename=paths.data / cfile)
            
            time = [t_v, t_p, t_c]
            temperature = [T_e_v, T_e_p, T_e_c]
            density = [n_v, n_p, n_c]
            
            plot_figures(time, temperature, density, L, H, t)
            
            
# Then plot the nanoflare trains for comparison
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
