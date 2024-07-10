#!/usr/bin/python3
'archieve web_static folder to deploy'
from fabric.api import local
def do_pack():
    local('time_now=$(date "+%Y%m%d%H%M%S")')
    local('tar -zcf web_static_<year><month><day><hour><minute><second>.tgz web_static')

