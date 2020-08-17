#!/usr/bin/python3
"""comment"""
from fabric.api import *
import time
from datetime import date


def do_pack():
    """func"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p version")
        local("tar -cvzf version/web_static_{}.tgz web_static/".format(timestamp))
        return ("versions/web_static_{}.tgz".format(timestamp))
    except:
        return None
