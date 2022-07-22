#!/usr/bin/env python
"""docstring TBD
"""

import os
import pandas as pd

__author__ = "Daniel Smith"
__copyright__ = "n/a"
__credits__ = ["Daniel Smith"]
__license__ = "GNU"
__version__ = "3.0"
__maintainer__ = "Daniel Smith"
__email__ = "daniel.g.smith@emory.edu"
__status__ = "Development"

def read_env_vars():
    df = pd.read_csv('.password-store/env_vars.csv')
    return df

def set_env_vars():
    df = read_env_vars()
    for key in df.keys():
        if key != 'PATH':
            value = df[key][0]
            os.system("SETX {0} {1} /M".format(key, value)) 
            ## YOU SHOULD NEVER USE THIS FOR PATH VARIABLES!! SETX SCREWS THINGS UP IF PATH as will trunc paths ##
            ## https://stackoverflow.com/a/59489965 ##
        else:
            print('skipping PATH')

if __name__ == '__main__':
    set_env_vars()