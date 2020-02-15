# CyClone :cyclone:
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

<p align="center">
  <br>
  <img src="https://github.com/lnxpy/Cyclone/blob/master/icons/texture.png" width="500">
  <br>
</p>

## How CyClone Works?

First of all, CyClone checks up your git and tries to pull all changes from the Github server to your local environment. Then, reinstalls all new packages from the requirements file and updates importing module lists.

## Setting up

After cloned the repository, install the requirements to make the main script ready to get in the work as follows.
```
cyclone$ pip3 install -r requirements.txt
```
When the installation finished up, you need to run the script and fill both `SOURCE` and `REPOSITORY` options up. Take a look at the following table to get informed about the options.

| Short Form    | Standard Form    | Descryption                                          | is Essential       |
| :-----------: | :--------------: | :--------------------------------------------------: | :----------------: |
| `-r`          | `--repository`   | repository address                                   | :heavy_check_mark: |
| `-s`          | `--source`       | library list source file (mostly `requirements.txt`) | :heavy_check_mark: |

| Examples                                                  |
| --------------------------------------------------------- |
| `python3 cyclone.py -r lnxpy/postern -s requirements.txt` |
| `python3 cyclone.py -r sys313/negar -s requires.txt`      |

Once you fill up all the options correctly, you will have such a status:
```
 [CHECK] lnxpy/cyclone repository
 [CHECK] cyclone found
 [CHECK] requirements.txt source
 [CHECK] configuration started
 [CHECK] config file created
```
Now, It's time the check the new path `disk/`. Let's take a tree from this directory and see what we have. You should not modify this directory because all of them are attached to eachother.
```
disk
├── conf.json
├── DONT_CHANGE_THIS_DIR
├── ReadMe.txt
└── update.py

0 directories, 4 files
```

## Time to Run up

Copy the all contents of the `disk/` directory into your python local repository and push it up to the cloud side. Now make a change in your github repository and try to fetch it up in your local system using the `update.py` file. **The configuration file should not be modified ever**.

## License
Licensed from [MIT](https://opensource.org/licenses/MIT).

## Fork
Fork and feed for free :)
