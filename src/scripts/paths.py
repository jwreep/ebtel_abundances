"""
Exposes common paths useful for manipulating datasets and generating figures.

"""
import os
from pathlib import Path

# Absolute path to the top level of the repository
root = Path(__file__).resolve().parents[2].absolute()

# Absolute path to the `src` folder
src = root / "src"

# Absolute path to the `src/data` folder (contains datasets)
data = src / "data"
figure1 = data / "Figure1"
figure2 = data / "Figure2"
figure3 = data / "Figure3"

# Absolute path to the `src/static` folder (contains static images)
static = src / "static"

# Absolute path to the `src/scripts` folder (contains figure/pipeline scripts)
scripts = src / "scripts"

# Absolute path to the `src/tex` folder (contains the manuscript)
tex = src / "tex"

# Absolute path to the `src/tex/figures` folder (contains figure output)
figures = tex / "figures"

# Absolute path to the `src/tex/output` folder (contains other user-defined output)
output = tex / "output"

# Absolute path to the ebtel++ code
ebtel_root = Path(os.environ['EBTELPLUSPLUS_DIR'])
