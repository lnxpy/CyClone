from . import settings
from time import sleep as slp
from requests import get
import os.path

def introducer():
    new_mark = ''
    for line in settings.MARK.split('\n'):
        for char in line:
            if char=='_':
                new_mark += settings.blue + char + settings.reset
            else:
                new_mark += settings.cyan + char + settings.reset
        new_mark += '\n'
    print(new_mark)

def progress(events):
    if events is False:
        print(' [%s] %s\n'%(settings.red+'ERROR'+settings.reset, 'Failed to read options'))
        return
    errors = True
    for key,value in zip(events.keys(),events.values()):
        if key == 'repository':
            print(' [%s] %s %s'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset,key))
            if get(value).status_code == 200:
                print(' [%s] %s found'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value.split('/')[-1] + settings.reset))
            else:
                errors = False
                print(' [%s] %s'%(settings.red+'ERROR'+settings.reset, settings.bold + value.split('/')[-1] + settings.reset + ' does not exist'))
        elif key == 'source':
            print(' [%s] %s %s'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset,key))
            if os.path.isfile(events[key]):
                print(' [%s] %s source file found'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset))
            else:
                errors = False
                print(' [%s] %s'%(settings.red+'ERROR'+settings.reset, settings.bold + value + settings.reset + ' not found'))
    return [True if errors else False]
