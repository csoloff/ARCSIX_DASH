from datetime import datetime
import pandas as pd
import numpy as np
import glob
def simple_read(path):
    '''
    Reads .ict files to a Pandas DataFrame
    :param path: path to the .ict data
    :return: Pandas DataFrame with .ict data
    '''
    with open(path) as f:
        # find the value in the file which tells you how many lines to skip to get to the table
        first_line = f.readline()
        header_line = int(first_line[0:-2].split(",")[0])-1
    data = pd.read_csv(path, sep=',', skiprows=header_line)

    # finds the location in the path containing the date
    acc = 0
    boo = False
    for letter in path:
        if letter == '2':
            boo = True
        elif boo and letter == '0':
            acc -= 1
            break
        acc += 1
        
    # creates datetime object with the date the data was collected
    dt = datetime(int(path[acc:acc+4]), int(path[acc+4:acc+6]), int(path[acc+6:acc+8])) 
    
    for column in data.keys():
        if 'Time' in column:
            # converts seconds after midnight columns to datetime
            data[column] = dt + pd.to_timedelta(data[column], unit='seconds')
    data.columns = data.columns.str.replace(' ', '')
    return data.replace(-9999, np.nan) # Converts -9999 values to NaN
def read_all(glob_key):
    '''
    Takes a key to look for in the file name and reads and concatenates all those ict files into a single Pandas DataFrame
    :param glob_key: a str which all files you want to concatenate contains
    :return: Pandas DataFrame
    '''
    paths = sorted(glob.glob('../data/*' + glob_key + '*.ict'))
    d_list = []
    for i in range(0,len(paths)):
        d_list.append(simple_read(paths[i]))
    return pd.concat(d_list)