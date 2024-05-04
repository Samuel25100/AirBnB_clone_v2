#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder."""
from fabric.api import local
from os.path import exists
from datetime import datetime


def do_pack():
    """Use generate the archive."""
    time = datetime.now()
    arc = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    if not exists("versions"):
        local('mkdir -p versions')
    create = local("tar -cvzf versions/{} web_static".format(arc))
    if create is not None:
        return "versions/{}".format(arc)
    else:
        return None
