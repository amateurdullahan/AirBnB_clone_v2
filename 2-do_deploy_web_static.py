#!/usr/bin/python3
"""comment"""
from os.path import exists
from fabric.api import *
env.hosts = ['35.237.97.2', '3.88.171.89']


def do_deploy(archive_path):
    """deep loy"""
    if exists(archive_path) is False:
        return False
    try:
        archive = archive_path.split('/')[-1]
        put(archive, '/tmp/')
        release = '/data/web_static/releases/{}'.format(archive.split('.')[1])
        run('mkdir -p {}'.format(release))
        run('tar -xzvf /tmp/{} -C {}'.format(archive, release))
        run('rm /tmp/{}'.format(archive))
        run('rm /data/web_static/current')
        run('ln -sf /data/web_static/current {}'.format(release))
        return True
    except:
        return False
