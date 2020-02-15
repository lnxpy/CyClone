import os
import json

mark = """
  _____     _______
 / ___/_ __/ ___/ /__  ___  ___
/ /__/ // / /__/ / _ \/ _ \/ -_)
\___/\_, /\___/_/\___/_//_/\__/
    /___/ V E R S I O N - 1 . 0

 This repository uses the CyClone to update its components.
 You can also make one for your own using CyClone.
 For more information, check the link below..
 https://github.com/lnxpy/cyclone
"""

is_permitted = True if os.getenv("SUDO_USER") else False

def main():
    print(mark)

    # Negative this part
    if is_permitted:
        printer('Permission denied', 'ERROR')
        return

    if os.path.isfile('_conf.json'):
        printer('Configs found')
    else:
        printer('Configuration could not be found', 'ERROR')
        return

    try:
        with open('_conf.json') as json_file:
            configs = json.load(json_file)
    except Exception as e:
        printer('Configuration file has been currepted', 'ERROR')

    print('NOW YOU ARE ROOT AND HAVE CONFIGURATIONS')
    print(is_permitted)
    print(configs[-1])

def printer(text, stat='CHECK'):
    print(' [%s] %s'%(stat, text))

if __name__ == '__main__':
    main()
