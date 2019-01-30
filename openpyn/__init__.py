import sys
import os.path
import subprocess


__version__ = "2.7.6.dev1"
__license__ = "GNU General Public License v3 or later (GPLv3+)"
__data_files__ = []
__basefilepath__ = os.path.dirname(os.path.abspath(__file__)) + "/"

log_format = "%(asctime)s [%(levelname)s] %(message)s"

_xdg_data_home = os.environ.get('XDG_DATA_HOME')
if not _xdg_data_home:
    _xdg_data_home = os.path.join(os.environ.get('HOME'), '.local', 'share')
ovpn_folder = os.path.join(_xdg_data_home, 'openpyn', 'files')
log_folder = os.path.join(_xdg_data_home, 'openpyn', 'logs')      # logs will be saved here


if sys.platform == "linux":
    if subprocess.check_output(["/bin/uname", "-o"]).decode(sys.stdout.encoding).strip() == "ASUSWRT-Merlin":
        __data_files__ = [("/opt/etc/init.d", ["./openpyn/S23openpyn"])]
    elif os.path.exists("/etc/openwrt_release"):
        __data_files__ = [("/opt/etc/init.d", ["./openpyn/S23openpyn"])]


# import gc
# print("\n".join(sorted({attrname for item in gc.get_objects() for attrname in dir(item) if attrname.startswith("__")})))
#
# print(__basefilepath__)
# print(__build_class__)
# print(__builtins__)
# print(__data_files__)
# print(__debug__)
# print(__doc__)
# print(__file__)
# print(__import__)
# print(__license__)
# print(__loader__)
# print(__name__)
# print(__package__)
# print(__path__)
# print(__spec__)
# print(__version__)
