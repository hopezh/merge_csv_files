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
def concat_csv_files(_dir_csv, _dir_merged_csv, _path_merged_csv, _cwd):
    if os.path.exists(_dir_merged_csv):
        if os.path.exists(_path_merged_csv):
            try:
                os.remove(_path_merged_csv)
            except OSError:
                print("ERROR!")
    else: 
        try:
            os.mkdir(_dir_merged_csv)
        except OSError:
            print('unable to create directory!')

    os.chdir(_dir_csv)
    csvList = glob.glob('*.csv')
    # print('csv file list:\n', csvList)

    dfList = []

    for f in csvList:
        # bld_id = f.split('.')[0]

        df = pd.read_csv(f, header=0)

        # df['building_id'] = bld_id

        dfList.append(df)

        print(f)
        print(df.shape)
        print(df.describe())
        print(df.head(), '\n')

    concatDf = pd.concat(dfList, axis=0)
    concatDf.to_csv(_path_merged_csv, index=None)

    print('merged csv file is:\n', _path_merged_csv, '\n')
    print('shape:\n', concatDf.shape, '\n')
    print('head:\n', concatDf.head(), '\n')
    print('tail:\n', concatDf.tail(), '\n')
    print('description:\n', concatDf.describe(), '\n')
    print('info:\n', concatDf.info(), '\n')

    os.chdir(cwd)


# --------------------------------------------------------
# get the cwd of this script
cwd = os.getcwd()
print('full path of current working directory:', '\n', cwd, '\n')


# --------------------------------------------------------
# specify the directory of the csv files
dir_csv  = 'data'
path_csv = os.path.join(cwd, dir_csv)
print('path of csv files:\n', path_csv, '\n')


# --------------------------------------------------------
# specify the path and name of merged csv file
merged_csv_dir_name  = 'merged_csv'
merged_csv_name = 'merged_results.csv'
dir_merged_csv = os.path.join(cwd, merged_csv_dir_name)
path_merged_csv = os.path.join(cwd, dir_merged_csv, merged_csv_name)
print('full path of merged csv:\n', path_merged_csv, '\n')


# --------------------------------------------------------
# concate csv files
concat_csv_files(path_csv, dir_merged_csv, path_merged_csv, cwd)


# --------------------------------------------------------
# print finish time stamp and time used
finish_time = datetime.now()
finish_time_str = finish_time.strftime('%Y-%m-%d %H:%M:%S')

time_used = finish_time - start_time

print('started  at : ' + start_time_str )
print('finished at : ' + finish_time_str )
print('time used   : ' + str(round(time_used.seconds/60, 1)) + ' minutes' + '\n')
print("＼(^o^)／... D'oh! .....................................................")
