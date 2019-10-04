# --------------------------------------------------------
import os
import glob
import shutil
import pandas as pd
from datetime import datetime

# --------------------------------------------------------
# get the cwd of this script
cwd = os.getcwd()
print('full path of current working directory:', '\n', cwd, '\n')

# --------------------------------------------------------
# specify the directory of the csv files
csv_file_name = 'B-1_2_LoD0_LoD1_LoD2_598.csv'
full_path_csv = os.path.join(cwd, csv_file_name)
print('full path of csv files:\n', full_path_csv, '\n')