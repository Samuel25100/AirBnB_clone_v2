#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder."""
from fabric.api import *
from os.path import exists
from datetime import datetime
env.hosts = ['34.207.212.213', '3.94.181.175']


def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if (not exists(archive_path)):
        return (False)
    fil_n = archive_path.split('/')[1].split('.')[0]

    r = put(archive_path, '/tmp/')
    if r.failed:
        return False
    r = run('mkdir -p /data/web_static/releases/{}'.format(fil_n))
    if r.failed:
        return False
    tmp = "/data/web_static/releases/{}/".format(fil_n)
    r = run('tar -xzf /tmp/{}.tgz -C {}'.format(fil_n, tmp))
    if r.failed:
        return False
    r = run('rm /tmp/{}.tgz'.format(fil_n))
    if r.failed:
        return False
    tmp = "/data/web_static/releases/{}/web_static/*".format(fil_n)
    r = run('mv {} /data/web_static/releases/{}/'.format(tmp, fil_n))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/releases/{}/web_static'.format(fil_n))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    tmp = "/data/web_static/current"
    r = run('ln -s /data/web_static/releases/{}/ {}'.format(fil_n, tmp))
    if r.failed:
        return False
    return True
