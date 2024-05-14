#!/usr/bin/python3

# Copyright (c) 2024 HybridNetworks Ltd.
#
# Author: danielcshn - https://github.com/danielcshn/
# Creation date: 2024-05-14
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

import paramiko
import time

# Configura los parámetros de conexión
host = 'tu_direccion_ip'
port = 22
username = 'tu_usuario'
password = 'tu_contraseña'
command = 'show version'

# Crea una instancia de cliente SSH
ssh_client = paramiko.SSHClient()

# Configura el cliente SSH para que acepte automáticamente las claves SSH desconocidas
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conéctate al dispositivo VyOS
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    commands = ssh_client.invoke_shell()

    commands.send(f"{command}\n")
    time.sleep(2)

    output = commands.recv(65535)  # Ajuste el tamaño del búfer según sea necesario
    output = output.decode("utf-8")
    print(output)

finally:
    # Cierra la conexión SSH
    ssh_client.close()
