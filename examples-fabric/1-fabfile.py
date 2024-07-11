#!/usr/bin/python3
from fabric.api import env, run, local, get, put
env.hosts = ['54.237.18.27', '34.232.66.181']
env.user = 'ubuntu'
def list_at_home():
    run('ls ~/')

def transfer_file(file):
    run('mkdir -p ~/my_fab_files')
    put(file, '~/my_fab_files')
