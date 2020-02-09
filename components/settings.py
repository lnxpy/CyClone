MARK = """
  _____     _______
 / ___/_ __/ ___/ /__  ___  ___
/ /__/ // / /__/ / _ \/ _ \/ -_)
\___/\_, /\___/_/\___/_//_/\__/
    /___/ V E R S I O N - 1 . 0
"""

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

red = colors.fg.red
cyan = colors.fg.cyan
blue = colors.fg.blue
reset = colors.reset
under = colors.underline
bold = colors.bold

information = ' [%s] %s'%(red+'ERROR'+reset, 'https://github.com/lnxpy/cyclone'+bold+' for more informations'+reset)
