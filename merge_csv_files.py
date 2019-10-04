"""
merge multiple csv files in one directory

"""

# --------------------------------------------------------
import os
import glob
import shutil
import pandas as pd
from datetime import datetime

# --------------------------------------------------------
# get start time stamp
start_time = datetime.now()
start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
print('start date & time:\n', start_time_str, '\n')

# --------------------------------------------------------
def concat_csv_files(path_csv, path_and_name_merged_csv, cwd):
    if os.path.exists(path_and_name_merged_csv):
        try:
            os.remove(path_and_name_merged_csv)
        except OSError:
            print("ERROR!")

    os.chdir(path_csv)
    csvList = glob.glob('*.csv')

    dfList = []

    for f in csvList:
        df = pd.read_csv(f, header=0)
        dfList.append(df)
        print(f)
        print(df.shape)
        print(df.describe())
        print(df.head(), '\n')

    concatDf = pd.concat(dfList, axis=0)
    concatDf.to_csv(path_and_name_merged_csv, index=None)

    print('output file is:\n', path_and_name_merged_csv, '\n')
    print('shape:\n', concatDf.shape, '\n')
    print('description:\n', concatDf.describe(), '\n')
    print('head:\n', concatDf.head(), '\n')

    os.chdir(cwd)

# --------------------------------------------------------
# get the cwd of this script
cwd = os.getcwd()
print('full path of current working directory:', '\n', cwd, '\n')

# --------------------------------------------------------
# specify the directory of the csv files
dir_csv  = 'data'
path_csv = os.path.join(cwd, dir_csv)
print('full path of csv files:\n', path_csv, '\n')

# --------------------------------------------------------
# specify the path and name of merged csv file
dir_merged_csv  = 'merged_csv'
merged_csv_file_name = 'merged_results.csv'
path_and_name_merged_csv = os.path.join(cwd, dir_merged_csv, merged_csv_file_name)
print('full path and name of merged csv:\n', path_and_name_merged_csv, '\n')

# --------------------------------------------------------
# concate csv files
concat_csv_files(path_csv, path_and_name_merged_csv, cwd)

# --------------------------------------------------------
# print finish time stamp and time used
finish_time = datetime.now()
finish_time_str = finish_time.strftime('%Y-%m-%d %H:%M:%S')

time_used = finish_time - start_time

print('started  at : ' + start_time_str )
print('finished at : ' + finish_time_str )
print('time used   : ' + str(round(time_used.seconds/60, 1)) + ' minutes' + '\n')
print("＼(^o^)／... D'oh! .....................................................")
