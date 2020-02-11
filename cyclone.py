from components import modules, settings
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', '-r', help='github python repository')
    parser.add_argument('--source', '-s', help='source file (e.g requirements.txt)')
    args = parser.parse_args()

    modules.introducer()
    if all(value for value in vars(args).values()):
        status = modules.progress(
        {
            'repository':vars(args)['repository'],
            'source':vars(args)['source'],
        })[0]
    else:
        modules.progress(False)
        return

    if status:
        modules.printer(['CHECK', 'configuration started'])
        configs = status[1]
        configs.append(vars(args))
        with open('./disk/_conf.json', 'w') as conf_file:
            json.dump(configs, conf_file)
        modules.printer(['CHECK', 'config file created'])
    else:
        modules.printer()

if __name__ == '__main__':
    main()
