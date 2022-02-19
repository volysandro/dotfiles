import sys
import os
import os.path
from clunky import update_cfg

if not len(sys.argv) == 3:
    print("Usage: python3 send_backup.py <archive> <host>")
    exit(1)

archive = sys.argv[1]
host = sys.argv[2]
pwd = os.path.dirname(os.path.realpath(__file__))
hwd = pwd + "/" + host
hcg = hwd + "/config"
f = open(hwd + "/hostname")
hostname = f.read()

cfg = {
    "STORE_LOCATION": "/root",
    "REMOTE_USER": "root",
    "QUERY_BEFORE": False
}

if os.path.isfile(hcg):
    cfg = update_cfg(cfg, hcg)

cmd = "scp "
cmd += "-i $BACKUPPYPATH/"
cmd += host
cmd += "/id_rsa "
cmd += archive
cmd += " "
cmd += cfg["REMOTE_USER"]
cmd += "@'"
cmd += hostname.strip('\n')
cmd += "':"
cmd += cfg["STORE_LOCATION"]

os.system(cmd)

