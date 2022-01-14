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
    if os.path.exists(archive_path) is False:
        print('file not found')
        return False
    try:
        slash = archive_path.find('/') + 1
        filename = archive_path[slash:]
        put(archive_path, '/tmp/{}'.format(filename))
        run('mkdir -p /data/web_static/releases/' + filename[:-4])
        run('tar -xzvf /tmp/' + filename + ' -C /data/web_static/releases/' +
            filename[:-4] + '/')
        run('rm /tmp/' + filename)
        run('mv /data/web_static/releases/' + filename[:-4] + '/web_static/* \
            /data/web_static/releases/' + filename[:-4] + '/')
        run('rm -rf /data/web_static/releases/' + filename[:-4] +
            '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename[:-4]))
        return True
    except Exception:
        return False


def deploy():
    """ deploy """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
