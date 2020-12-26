# MATE Layouts

![MATE Layouts](https://github.com/FreaxMATE/mate-layouts/blob/main/data/screenhot.png "MATE Layouts")

Mate Layouts is a small panel layout switching application for the MATE Desktop.

## Installation

### Dependencies

#### Manjaro:
```bash 
sudo pacman -S python-distutils-extra 
```

#### Debian / Ubuntu:
```bash 
sudo apt install python3-pip python3-distutils python3-distutils-extra python3-psutil python3-setproctitle libnotify-dev dconf-cli
```


### Build and Install from source

```bash
git clone https://github.com/FreaxMATE/mate-layouts.git
cd mate-layouts
sudo pip3 install .
# Uninstall
sudo pip3 uninstall mate-layouts
```

## License

Copyright 2020 FreaxMATE

Licensed under the terms of the GPLv3 license: https://www.gnu.org/licenses/gpl-3.0.html
