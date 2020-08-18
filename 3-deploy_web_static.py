#!/usr/bin/python3
"""loud dog upstairs"""
from fabric.api import *
from datetime import datetime
env.hosts = ['35.237.97.2', '3.88.171.89']


def deploy():
    """call do_pack"""
    archive = do_pack()
    if (archive is None):
        return False
    return do_deploy(archive)


def do_deploy(archive_path):
    """ do_deploy docstring """
    from os.path import isfile
    if not isfile(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split('/')[1]
        output = "/data/web_static/releases/{}".format(archive.split('.')[0])
        run("mkdir -p {}/".format(output))
        run("tar -xzf /tmp/{} -C {}/".format(archive, output))
        run("rm -rf /tmp/{}".format(archive))
        run("mv {}/web_static/* {}".format(output, output))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(output))
        print("New version deployed!")
        return True
    except:
        return False


def do_pack():
    """func"""
    date = datetime.now()
    timestamp = date.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(
            timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None
