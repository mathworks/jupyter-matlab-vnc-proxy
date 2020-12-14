# Copyright 2020 The MathWorks, Inc.

import os
import shlex
import tempfile

def setup_desktop():
    # Get path to noVNC installation through environment variables
    NOVNC_PATH = os.getenv('NOVNC_PATH', '/opt/noVNC')
    # make a secure temporary directory for sockets
    # This is only readable, writeable & searchable by our uid
    sockets_dir = tempfile.mkdtemp()
    sockets_path = os.path.join(sockets_dir, 'vnc-socket')
    vnc_command = ' '.join((shlex.quote(p) for p in [
        'vncserver',
        '-verbose',
        '-xstartup', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'xstartup'),
        '-geometry', '1680x1050',
        '-SecurityTypes', 'None',
        '-rfbunixpath', sockets_path,
        '-fg',
        ':1',
    ]))
    return {
        'command': [
            'websockify', '-v',
            '--web', NOVNC_PATH,
            '--heartbeat', '30',
            '5901',
            '--unix-target', sockets_path,
            '--',
            '/bin/sh', '-c',
            f'cd {os.getcwd()} && {vnc_command}'
        ],
        'port': 5901,
        'timeout': 30,
        'mappath': {'/': '/mw_lite.html'},
        'new_browser_window': True,
        'launcher_entry': {
            'title': 'MATLAB VNC DESKTOP',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'matlab_icon.svg')
        }
    }
