"""
Configures the input data file for ebtel++

"""
import numpy as np
import paths

def read_initial_configuration(file=paths.data / "ebtel.example.cfg.xml"):
    with file.open() as f:
        lines = f.readlines()
    return lines
    
def write_new_configuration(lines,
                            file= paths.ebtel_root / "config/ebtel.example.cfg.xml",
                            length = '40.0',
                            radiation = 'variable',
                            output_filename = 'ebtel++_results_file.txt',
                            heating_rate = ['0.01'],
                            heating_duration = ['20'],
                            heating_start = ['0'],
                            ):
    lines[5] = '  <loop_length>'+length+'e+8</loop_length>\n'
    lines[14] = '  <radiation>'+radiation+'</radiation>\n'
    lines[15] = '  <output_filename>'+str(output_filename)+'</output_filename>\n'
    if (len(heating_rate) != len(heating_duration) or
        len(heating_rate) != len(heating_start) ):
        raise ValueError("Heating arrays must have the same length.\n")
    
    f = open(file, "w")
    for i in range(30):
        f.write(lines[i])
    for i in range(len(heating_rate)):
        rise_end = str(float(heating_duration[i])/2.0 + float(heating_start[i]))
        decay_end = str(float(heating_start[i]) + float(heating_duration[i]))
        event = (
                 '      <event magnitude="'+heating_rate[i]+
                 '" rise_start="'+heating_start[i]+'" rise_end="'+
                 rise_end+'" decay_start="'+rise_end+'" decay_end="'+
                 decay_end+'"/>\n'
        )
        f.write(event)
    f.write('    </events>\n  </heating>\n</root>\n')
    f.close()
    
