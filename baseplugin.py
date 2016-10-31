#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014-2016 Andrea Baldan
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import sys
import re
from creakframework import Printer

N = '\033[m' # native
R = '\033[31m' # red
G = '\033[32m' # green
O = '\033[33m' # orange
B = '\033[34m' # blue
C = '\033[36m' # cyan

class Parameters(dict):

    def __init__(self, *args, **kwargs):
        super(Parameters, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        super(Parameters, self).__setitem__(key, value)

    def __delitem__(self, key):
        super(Parameters, self).__delitem__(key)

    def set_values(self, **kwargs):
        for arg in kwargs:
            self.__setitem__(arg, kwargs[arg])

class BasePlugin(Printer):

    def __init__(self, args):
        self.app_path = sys.path[0]
        self._plugin_name = args
        self.root = False
        self.required_params = Parameters()

    def _set_required_params(self, **kwargs):
        self.required_params.set_values(**kwargs)

    def print_exception(self, line=''):
        # if self._global_options['debug']:
        #     traceback.print_exc()
        self.error(line)

    def error(self, line):
        '''Formats and presents errors.'''
        if not re.search('[.,;!?]$', line):
            line += '.'
        line = line[:1].upper() + line[1:]
        print('%s[!] %s%s' % (R, line, N))

    def print_output(self, line):
        '''Formats and presents normal output.'''
        print('%s[*]%s %s' % (C, N, line))
