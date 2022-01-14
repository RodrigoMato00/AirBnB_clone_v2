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
    static
    """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """
    web servers
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


def deploy():
    """ deploy """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
