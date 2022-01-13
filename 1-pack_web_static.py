#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    fabric script
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    name_tgz = "versions/web_static_" + date_time + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + name_tgz + " web_static")
    if not (os.path.exists(name_tgz)):
        return None
    else:
        return (name_tgz)
