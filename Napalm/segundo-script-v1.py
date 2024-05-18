#!/usr/bin/python3

# Copyright (c) 2024 HybridNetworks Ltd.
#
# Author: danielcshn - https://github.com/danielcshn/
# Creation date: 2024-05-17
# Version: 1.0
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from napalm import get_network_driver

driver = get_network_driver('vyos')

vyos_router = driver(
    hostname="192.168.88.249",
    username="vyos",
    password="vyos",
    optional_args={"port": 22},
)

vyos_router.open()

vyos_router.load_merge_candidate(filename='firewall.config')
diffs = vyos_router.compare_config()

if bool(diffs) == True:
    print(diffs)
    vyos_router.commit_config()
else:
    print('INFO: No hay cambios de configuracion para confirmar.')
    vyos_router.discard_config()

vyos_router.close()