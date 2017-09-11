import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/Dominic Gaiero/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/Dominic Gaiero/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=[],
    excludes=[],
    include_files=['icon.ico', 'C:/Users/Dominic Gaiero/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll',
                   'C:/Users/Dominic Gaiero/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py',
               targetName="CPIEEE_RESISTOR.exe",
               base=base,
               icon="icon.ico")
]

setup(
    name="Resistor Setup",
    version="0.2",
    description="Generates images from resisitor values",
    author="Dominic Gaiero",
    options=dict(build_exe=buildOptions),
    executables=executables)
