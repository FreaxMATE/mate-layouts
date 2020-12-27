#!/usr/bin/env python3

# Copyright (C) 2020 Konstantin Unruh <freaxmate@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys

from glob import glob
from setuptools import setup

import DistUtilsExtra.command.build_extra
import DistUtilsExtra.command.build_i18n
import DistUtilsExtra.command.clean_i18n

# to update i18n .mo files (and merge .pot file into .po files) run on Linux:
#   tx pull -a --minimum-perc=5
#   python3 setup.py build_i18n -m
#   tx push -s

# silence pyflakes, __VERSION__ is properly assigned below...
__VERSION__ = '0.0.0.0'
with open('src/mate-layouts') as f:
    for line in f:
        if (line.startswith('__VERSION__')):
            exec(line.strip())
            break

PROGRAM_VERSION = __VERSION__

data_files = [
    ('{prefix}/share/applications'.format(prefix=sys.prefix), ['data/org.github.FreaxMATE.mate-layouts.desktop',]),
    ('{prefix}/lib/mate-layouts'.format(prefix=sys.prefix), ['src/mate-layouts-helper']),
    ('{prefix}/share/mate-layouts'.format(prefix=sys.prefix), ['data/org.github.FreaxMATE.mate-layouts.ui']),
    ('{prefix}/share/icons/hicolor/scalable/apps'.format(prefix=sys.prefix), ['data/org.github.FreaxMATE.mate-layouts.svg']),
    ('{prefix}/share/icons/hicolor/64x64/apps'.format(prefix=sys.prefix), ['data/org.github.FreaxMATE.mate-layouts.svg']),
    ('{prefix}/share/polkit-1/actions'.format(prefix=sys.prefix), ['data/org.github.FreaxMATE.mate-layouts.policy',]),

    # layout previews
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/custom.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/default.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/fedora.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/manjaro.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/opensuse.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/redmond-no-indicators.svg']),
    # with the logo on them
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/default-logo.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/fedora-logo.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/manjaro-logo.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/opensuse-logo.svg']),
    ('{prefix}/share/mate-layouts/layout-previews'.format(prefix=sys.prefix), ['data/layout-previews/redmond-no-indicators-logo.svg']),
]

cmdclass ={
            "build" : DistUtilsExtra.command.build_extra.build_extra,
            "clean": DistUtilsExtra.command.clean_i18n.clean_i18n,
}

setup(
    name = "mate-layouts",
    version = PROGRAM_VERSION,
    description = "MATE Layouts",
    license = 'GPLv3+',
    author = 'Konstantin Unruh',
    url = 'https://github.com/FreaxMATE/mate-layouts',
    package_dir = {'': '.'},
    data_files = data_files,
    install_requires = [ 'setuptools', ],
    scripts = ['src/mate-layouts'],
    cmdclass = cmdclass,
)
