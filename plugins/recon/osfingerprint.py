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

from creak.baseplugin import BasePlugin

class Plugin(BasePlugin):

    """
    TODO
    """

    def init_plugin(self):
        self._set_info(
            author='codep',
            version='1.0',
            description='OS fingerprinting plugin')
        self._set_root(True)
        self._set_required_params(target=True)

    def run(self, kwargs):
        raise NotImplementedError('TODO')
