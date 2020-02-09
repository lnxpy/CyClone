from components import settings, modules
import argparse

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
        modules.updater(vars(args))
    else:
        print(settings.information)

if __name__ == '__main__':
    main()
