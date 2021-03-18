# MATE Layouts

<img src="https://github.com/FreaxMATE/mate-layouts/blob/main/data/icons/hicolor/scalable/apps/org.github.FreaxMATE.mate-layouts.svg" alt="MATE Layouts Icon" width="256"/>
<!--- ![MATE Layouts Logo](https://github.com/FreaxMATE/mate-layouts/blob/main/data/org.github.FreaxMATE.mate-layouts.svg ==250x) -->

MATE Layouts is a small panel layout switching application for the MATE Desktop.

This application makes it easy to quickly metamorphose your desktop to your favourite workflow. \
You are nostalgic and prefer a traditional experience? Check out the timeless, productive Gnome 2 desktop! \
Want to use the more trendy, innovative layouts? Maybe you should try the Contemporary or Cupertino layout!

![MATE Layouts](https://github.com/FreaxMATE/mate-layouts/blob/main/data/screenshot.png "MATE Layouts")

MATE Layouts is written in Python with the GTK Toolkit and based on mate-tweak.

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

#### Using meson
```bash
git clone https://github.com/FreaxMATE/mate-layouts.git
cd mate-layouts
meson build --prefix=/usr
cd build
sudo ninja install
# Uninstall
sudo ninja uninstall
```

#### Using Pip / python setuptools
```bash
git clone https://github.com/FreaxMATE/mate-layouts.git
cd mate-layouts
sudo pip3 install .
# Uninstall
sudo pip3 uninstall mate-layouts
```

**on Debian as for now you have to use ```sudo python setup.py install``` instead of ```pip``` (you'll have to manually uninstall the application)**

## License

Copyright 2020 FreaxMATE

Licensed under the terms of the GPLv3 license: https://www.gnu.org/licenses/gpl-3.0.html
