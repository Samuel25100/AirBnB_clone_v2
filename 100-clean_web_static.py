#!/usr/bin/python3
"""Delete out-of-date archive."""
from fabric.api import *


def do_clean(number=0):
    """Delete out-of-date archive."""
    num = local("ls -l versions/ | wc -l", hide=True)
    num = int(num.stdout.strip())
    for i in range(number):
        if num > 1:
            n = local("ls -t1r versions/ | head -n 1")
            n = str(n.stdout.strip())
            local(f"rm versions/{n}")
    #For the server
    num = run("ls -l /data/web_static/releases/ | wc -l", hide=True)
    num = int(num.stdout.strip())
    for i in range(number):
        if num > 2:
            n = run("ls -t1r /data/web_static/releases/ | head -n 2 | tail -n 1")
            n = str(n.stdout.strip())
            run(f"rm /data/web_static/releases/{n}")
