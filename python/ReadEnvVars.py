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
    print(df)

def set_env_vars():
    df = read_env_vars()
    for key in df.keys():
        os.environ[key] = df[key][0]

def main():
    set_env_vars()

main()