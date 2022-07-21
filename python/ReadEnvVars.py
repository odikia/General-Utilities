import os
import pandas as pd


def read_env_vars():
    df = pd.read_csv('env_vars.csv')
    print(df)

def set_env_vars():
    df = read_env_vars()
    for key in df.keys():
        os.environ[key] = df[key][0]

def main():
    set_env_vars()

main()