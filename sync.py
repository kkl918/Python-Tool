import os
from dirsync import sync

target = r'D:\2018'
#target = r'O:\2018'
source = r'\\140.116.228.155\geodac_uav\2018'

ans = input('確定同步 ' + source + ' 到 ' + target + ' 嗎? (y/n/o): ')

yes = ['Y', 'y']
no  = ['N', 'n']
ot  = ['O', 'o']
#sync(source, target, 'sync')

if ans in yes: 
    sync(source, target, 'sync')
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