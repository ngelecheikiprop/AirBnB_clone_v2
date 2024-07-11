#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local, run, env, put, sudo
from datetime import datetime
import os
env.hosts = ['54.237.18.27', '34.232.66.181']
env.user = 'ubuntu'


def do_pack():
    'compress the webstatic folder into versions folder'
    local('mkdir -p versions/')
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{time_now}.tgz"
    local(f'cd web_static && tar -czvf ../{file_path} * && cd -')
    return file_path


def do_deploy(archive_path):
    'distributes archive to webservers'
    if not os.path.exists(archive_path):
        return False
    try:
        sudo('mkdir -p /tmp/')
        put(archive_path, '/tmp/')
        file_name = os.path.basename(archive_path)
        sudo('mkdir -p /data/web_static/releases/')
        sudo(f'tar -xf /tmp/{file_name} \
                --one-top-level -C /data/web_static/releases/')
        sudo(f'rm -f /tmp/{file_name}')
        sudo(f'rm -f /data/web_static/current')
        extracted_file = os.path.splitext(file_name)[0]
        sudo(f'ln -s /data/web_static/releases/{extracted_file}\
                /data/web_static/current')
        return True
    except Exception:
        return False
