import os
import sys

INTERP = "/home/your-cpanel-user/virtualenv/nexus/3.11/bin/python"
if sys.executable != INTERP:
    os.environ["HOME"] = "/home/your-cpanel-user"
    os.execv(INTERP, [INTERP] + sys.argv)

from app import app as application
