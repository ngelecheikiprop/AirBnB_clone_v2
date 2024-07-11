#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local

def do_pack():
    local('mkdir -p versions', shell=True)
    local('time_now=$(date "+%Y%m%d%H%M%S")', shell=True)
    local('file_name=web_static_$time_now.tgz', shell=True)
    local('mypath=versions/$file_name', shell=True)
    local('tar -zcfv $mypath web_static', shell=True)
