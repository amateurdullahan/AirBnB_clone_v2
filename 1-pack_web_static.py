#!/usr/bin/python3
"""comment"""
from fabric.api import local
import time
from datetime import date


def do_pack():
    """func"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None
