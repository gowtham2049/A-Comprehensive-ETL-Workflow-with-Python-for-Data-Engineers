from Scripts.csv_extract import extract_csv
from Scripts.json_extract import extract_json
from Scripts.xml_extract import extract_xml
from Scripts.transform import transform_df
from Scripts.load import load_csv
import pandas as pd
import glob
import logging 

def log_setup():
    with open('logs\\log.txt','a') as log_file:
        log_file.write('\n \n ETL PROCESS \n')

    logging.basicConfig(
        filename=r"logs\log.txt",  # Use raw string to handle backslash properly
        encoding="utf-8",
        filemode="a",  # Append to the log file
        format="{asctime} - {levelname} - {message}",  # Custom log message format
        style="{",  # Use { as the placeholder for formatting
        datefmt="%Y-%m-%d %H:%M",  # Custom date format
        level=logging.DEBUG 
        )
  
def main():
    log_setup()
    logging.info("ETL Starting ")

    logging.info("csv extraction ")
    csv_df=extract_csv('dataset')

    logging.info("json extraction ")
    json_df=extract_json('dataset')

    logging.info("xml extraction ")
    xml_df=extract_xml('dataset')

    logging.info("Concating the dataframes")
    concat_df=pd.concat([csv_df,json_df,xml_df],ignore_index=True)

    logging.info("transformation process")
    transformed_df=transform_df(concat_df)

    logging.info("Loading data")
    load_csv(transformed_df)
    logging.info("ETL process completed")

if __name__=='__main__':
    main()

