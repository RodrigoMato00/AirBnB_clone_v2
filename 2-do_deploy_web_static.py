#!/usr/bin/python3
"""
abric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local
from fabric.api import env
from datetime import datetime
import os

env.host["34.138.95.23", "18.212.250.192"]


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


def do_deploy(archive_path):
    """
    do_deploy(archive_path)
    """
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
        put(archive_path, "/tmp/")
        archive = archive_path.replace(".tgz", "")
        archive = archive.replace("versions", "")
        run("mkdir -p /data/web_static/releases/{}".format(archive))
        run("tar -xvz /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(archive, archive))
        run("rm /tmp/{}.tgz".format(archive))
        run("mv /data/web_static/releases/{}/web_static/*".format(archive) +
            "/data/web_static/releases/{}/".format(archive))
        run("rm -rf /data/web_static/releases/{}/web_static".fotmat(archive))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive))
        print("New version deployed!")
        return True
