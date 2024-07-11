#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local
from datetime import datetime


def do_pack():
    'compress the webstatic folder into versions folder'
    local('mkdir -p versions/')
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{time_now}.tgz"
    local(f'tar -cavf {file_path} web_static/*')
