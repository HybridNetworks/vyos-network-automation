#!/usr/bin/python3

# Copyright (c) 2024 HybridNetworks Ltd.
#
# Author: danielcshn - https://github.com/danielcshn/
# Creation date: 2024-05-16
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

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# Definimos los detalles de conexión del dispositivo VyOS
VYOS1 = {
    'device_type': 'vyos',
    'ip': '192.168.88.249',
    'username': 'vyos',
    'password': 'vyos',
    'secret': 'secret',
    'port': 22,
}

VYOS2 = {
    'device_type': 'vyos',
    'ip': '192.168.88.236',
    'username': 'vyos',
    'password': 'vyos',
    'secret': 'secret',
    'port': 22,
}

all_devices = [VYOS1, VYOS2]

try:
    for devices in all_devices:
        # Establecemos la conexión al dispositivo VyOS
        print(f'Connecting to {devices["ip"]}')
        net_connect = ConnectHandler(**devices)

        output = net_connect.send_command("show system uptime")
        print(output)

        # Cerramos la conexión
        net_connect.disconnect()

except NetmikoTimeoutException:
    print("Conexión expirada. No se pudo conectar al dispositivo VyOS.")
except NetmikoAuthenticationException:
    print("Fallo de autenticación. Verifique las credenciales e intente de nuevo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")