import pandas as pd
import zipfile

def zipToDataframe():
    try:
        df = pd.read_table('01-decommercialresponsive_2021-01-05.tsv.gz', sep='\t', compression='gzip')
        print(df.head())
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False


zipToDataframe()
