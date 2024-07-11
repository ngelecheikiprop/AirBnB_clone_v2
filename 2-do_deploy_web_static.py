#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local, run, env, put
from datetime import datetime
import os
env.hosts = ['54.237.18.27', '34.232.66.181']
env.user = 'ubuntu'


def do_pack():
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
    run('mkdir -p /tmp/')
    put(archive_path, '/tmp/')
    run(f'tar -xvf /tmp/{archive_path}'
        '--one-top-level -C /data/web_static/releases/')
    run(f'rm /tmp/{archive_path}')
    run(f'rm /data/web_static/current')
    run(f'ln -s {archive_path} /data/web_static/current')
    return True
