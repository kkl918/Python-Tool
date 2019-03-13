import os
from dirsync import sync

target = r'D:\2018_TCGE_0316'
source = r'C:\Users\RSLAB\Desktop\2018_TCGE_0316'


 
fr = r'\\140.116.228.155\geodac_uav\TCGE'
to = r'D:\TCGE'

ans = input('確定同步 \n' + source + ' \t到\t ' + target + ' \t以及\n' + fr + ' \t到\t ' + to + ' \t\t嗎? (y/n/o): ')

yes = ['Y', 'y']
no  = ['N', 'n']
ot  = ['O', 'o']
#sync(source, target, 'sync')

if ans in yes: 
    sync(source, target, 'sync')
    sync(fr    , to    , 'sync')
    print('同步: '+ source + ' 以及 ' + target)
elif ans in ot:
    other = input('(d)diff (u)update: ')
    if other == 'd':
        sync(source, target, 'diff')
    elif other == 'u':
        sync(source, target, 'update')
    else:
        print('\n退出!')
else:
    print('\n退出!')