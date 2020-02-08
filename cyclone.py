from components import settings, modules
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository',help='github python repository')
    parser.add_argument('-s', '--source', help='source file (e.g requirements.txt)')
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

    if status:
        data = vars(args)
        print(data)


if __name__ == '__main__':
    main()
