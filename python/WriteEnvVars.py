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

def env_as_dict():
    """
    Return a dictionary of environment variables.
    """
    return os.environ

def env_vars_to_filter():
    """
    Return a list of environment variables to filter based on a common naming convention.
    """
    naming_convention = 'Z_'
    new_filt = dict(filter(lambda item: item[0].startswith(naming_convention), env_as_dict().items()))
    return new_filt
def filter_env_vars(env_vars):
    """
    Return a dictionary of environment variables that are not in the list of
    environment variables to filter.
    """
    filtered_env_vars = {}
    for key in env_vars.keys():
        if key in env_vars_to_filter():
            filtered_env_vars[key] = env_vars[key]
    return filtered_env_vars

def env_vars_to_dataframe():
    env_vars = env_as_dict()
    filtered_env_vars = filter_env_vars(env_vars)
    df = pd.DataFrame(filtered_env_vars, index=[0])
    return df

def write_env_vars():
    df = env_vars_to_dataframe()
    print(df)
    df.to_csv('.password-store/env_vars.csv')

def main():
    write_env_vars()

main()