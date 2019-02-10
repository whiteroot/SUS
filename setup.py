#!/usr/bin/env python

import subprocess
import sys

if sys.version_info.major < 3:
    print ('please use python3')
    sys.exit(1)

cmde = 'python -m pip install -r requirements.txt'
p = subprocess.run(cmde.split())
