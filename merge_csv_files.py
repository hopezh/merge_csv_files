import os
import glob
import shutil
import pandas as pd
from datetime import datetime

# get start date & time
start_time = datetime.now()
start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
