import pandas as pd

def load_csv(df):
    df.to_csv(r'output\transformed_data.csv',index=False,mode='w')