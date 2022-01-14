#!/usr/bin/python3
"""
all all
"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env


env.hosts = ['34.138.95.23', '18.212.250.192']


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
    son los 40 de los 40 de los 40 que llegaron antes
    """
    if os.path.exists(archive_path):
        try:
            file_n = archive_path.split("/")[-1]
            no_ext = file_n.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, no_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
            run('rm /tmp/{}'.format(file_n))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
            run('rm -rf {}{}/web_static'.format(path, no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
            return True
        except Exception:
            return False
    else:
        return False
