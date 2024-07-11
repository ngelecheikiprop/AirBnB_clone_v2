#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local, run, env, put
import os
env.hosts = ['54.237.18.27', '34.232.66.181']
env.user = 'ubuntu'


def do_pack():
    from fabric.api import local
    from datetime import datetime
    'compress the webstatic folder into versions folder'
    local('mkdir -p versions/')
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{time_now}.tgz"
    local(f'tar -cavf {file_path} web_static')
    return file_path


def do_deploy(archive_path):
    'distributes archive to webservers'
    if not os.path.exists(archive_path):
        return False
    file_path = do_pack()
    run('mkdir -p /tmp/')
    put(file_path, '/tmp/')
    run(f'tar -xvf /tmp/{file_path}'
        '--one-top-level -C /data/web_static/releases/')
    run(f'rm /tmp/{file_path}')
    run(f'rm /data/web_static/current')
    run(f'ln -s {file_path} /data/web_static/current')
    return True
