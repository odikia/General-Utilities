import os
import pandas as pd

def env_as_dict():
    """
    Return a dictionary of environment variables.
    """
    return os.environ

def filter_env_vars(env_vars):
    """
    Return a dictionary of environment variables that are not in the list of
    environment variables to filter.
    """
    filtered_env_vars = {}
    env_vars_to_filter = ['z_trial']
    for key in env_vars.keys():
        if key in env_vars_to_filter:
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
    df.to_csv('env_vars.csv')

def main():
    write_env_vars()

main()