# CyClone 🌀
<p align="center">
  <br>
  <img src="https://github.com/lnxpy/Cyclone/blob/master/icons/temp.svg" width="140">
  <br>
  <br>
  <span>★ Make Updater Scripts for Your Python Projects ★</span>
  <br>
  <span>Build it ∘ Cross it ∘ Update it</span>
  <br>
  <br>
  <a href="#"><img src="https://img.shields.io/github/issues/lnxpy/cyclone?style=flat-square" alt="Version" style="max-width:100%;"></a>
  <a href="#"><img src="https://img.shields.io/github/stars/lnxpy/cyclone?style=flat-square" alt="Version" style="max-width:100%;"></a>
  <a href="#"><img src="https://img.shields.io/github/license/lnxpy/cyclone?color=purple&style=flat-square" alt="Version" style="max-width:100%;"></a>
</p>

CyClone is kind of Python-Package-Updater that allows users to create an updater-version of their python project and make them available on their Github. Although users can update their local cloned repository with their own selves, getting stuck in a bunch of files and modules and trying to get out of them can be little bit noisy.
First, you need to clone this repository then, start running into it and fill up your fields.

## How CyClone Works?

First of all, CyClone checks up your git and tries to pull all changes from the Github server to your local environment. Then, reinstalls all new packages from the requirements file and updates importing module lists.

## Setting up

After cloned the repository, install the requirements to make the main script ready to get in the work as follows.
```
cyclone$ pip3 install -r requirements.txt
```
When the installation finished up, you need to run the script and fill both `SOURCE` and `REPOSITORY` options up. Take a look at the following table to be informed about the options.

| Short Form    | Standard Form    | Descryption                    |
| :-----------: | :--------------: | :----------------------------: |
| `-r`          | `--repository`   | repository address             |
| `-s`          | `--source`       | library list source file (mostly `requirements.txt`) |

| Examples                                                  |
| --------------------------------------------------------- |
| `python3 cyclone.py -r lnxpy/postern -s requirements.txt` |
| `python3 cyclone.py -r sys313/negar -s requires.txt`      |

Once you fill up all the options correctly, you will have such a status:

## License
Licensed from [MIT](https://opensource.org/licenses/MIT).

## Fork
Fork and feed for free :)
