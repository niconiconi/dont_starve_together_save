import os
import zipfile
import shutil
import time
print(os.listdir(os.environ['USERPROFILE'] + '\documents\klei'))

current_time = time.asctime()
time_no_space = ''
for x in current_time.split(' '):
    time_no_space = time_no_space + '-' + x

current_time = time_no_space[1:]
time_no_space = ''
for x in current_time.split(':'):
    time_no_space = time_no_space + '-' + x

file_name = 'dont_starve' + time_no_space

shutil.make_archive(file_name, 'zip', os.environ['USERPROFILE'] + '\documents\klei' + '\DoNotStarveTogether')