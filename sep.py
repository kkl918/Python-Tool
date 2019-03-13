import os, shutil, glob, re
import pathlib

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

pathlib.Path('./1').mkdir(parents=True, exist_ok=True)
pathlib.Path('./2').mkdir(parents=True, exist_ok=True)

allfiles = glob.glob('*.jpg')

allfiles.sort(key=natural_keys)

for index ,afile in enumerate(allfiles):   
    if index % 2 == 0:
        shutil.move(afile, './1')
    else:
        shutil.move(afile, './2')