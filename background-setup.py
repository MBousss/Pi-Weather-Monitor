#!/usr/bin/env python

import os

service_name = 'weather.service'
service_path = '/lib/systemd/system/{}'.format(service_name)

if not os.path.exists(service_path):
    os.mknod(service_path)

service_content = [
    '[Unit]\n',
    'Description=Weather displayer\n',
    'After=multi-user.target\n',
    '\n',
    '[Service]\n',
    'Type=idle\n',
    'ExecStart=/usr/bin/python {}\n'.format(os.path.dirname(os.path.abspath(__file__)) + "/weather.py"),
    'User={}\n'.format(os.getlogin()),
    '\n',
    '[Install]\n',
    'WantedBy=multi-user.target\n'
    ]
with open(service_path, 'w') as f:
    f.writelines(service_content)

os.chmod(service_path, 644)
os.system("systemctl daemon-reload")
os.system("systemctl enable {}".format(service_name))
os.system("reboot")