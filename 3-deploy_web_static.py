#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder."""
from fabric.api import *
from os.path import exists, getsize
from datetime import datetime
env.hosts = ['34.207.212.213', '3.94.181.175']


def do_pack():
    """Use generate the archive."""
    time = datetime.now()
    arc = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    try:
        if not exists("versions"):
            local('mkdir versions')
        local("tar -cvzf versions/{} web_static".format(arc))
        size = getsize(f"versions/{arc}")
        print(f"web_static packed: versions/{arc} -> {size}")
        arc = "versions/{}".format(arc)
        return arc
    except:
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not exists(archive_path):
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


def deploy():
    """Create and distributes an archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
