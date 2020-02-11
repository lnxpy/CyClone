from . import settings
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
            direction = {'username':value.split('/')[0],'repository':value.split('/')[1].lower()}
            print(' [%s] %s %s'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset,key))
            connection = get('https://api.github.com/users/%s/repos'%direction['username'])
            if connection.status_code == 200 and direction['repository'] in [i['name'].lower() for i in connection.json()]:
                print(' [%s] %s found'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value.split('/')[-1] + settings.reset))
            else:
                errors = False
                print(' [%s] %s'%(settings.red+'ERROR'+settings.reset, settings.bold + value.split('/')[-1] + settings.reset + ' does not exist'))
        elif key == 'source':
            print(' [%s] %s %s'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset,key))
            if os.path.isfile(events[key]):
                print(' [%s] %s source file selected as the default one'%(settings.cyan+'CHECK'+settings.reset,settings.bold + value + settings.reset))
    return [[True, connection.json()] if errors else False]

def printer(text=['ERROR', 'https://github.com/lnxpy/cyclone for more information']):
    if text[0] == 'ERROR':
        print(' [%s] %s'%(settings.red + 'ERROR' + settings.reset, text[1]))
    else:
        print(' [%s] %s'%(settings.cyan + 'CHECK' + settings.reset, text[1]))
