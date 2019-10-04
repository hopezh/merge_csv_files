"""
merge multiple csv files in one directory

"""

#--------------------------------------------------------
import os
import glob
import shutil
import pandas as pd
from datetime import datetime

#--------------------------------------------------------
# get start date & time
start_time = datetime.now()
start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')

# --------------------------------------------------------
def concat_csv_files(csv_dir, output_csv_dir_name):
    if os.path.exists(output_csv_dir_name):
        try:
            os.remove(output_csv_dir_name)
        except OSError:
            print("ERROR!")

    os.chdir(csv_dir)
    csvList = glob.glob('*.csv')

    dfList = []

    for f in csvList:
        df = pd.read_csv(f, header=0)
        dfList.append(df)
    #         print(f)
    #         print(df.shape)
    #         print(df.describe())
    #         print(df.head())

    concatDf = pd.concat(dfList, axis=0)
    concatDf.to_csv(output_csv_dir_name, index=None)
    print(output_csv_dir_name)
    print(concatDf.shape)
#     print(concatDf.describe())
#     print(concatDf.head())
