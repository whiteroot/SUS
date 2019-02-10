#!/usr/bin/env python3

import subprocess

cmde = 'python3 -m pip install -r requirements.txt'
p = subprocess.run(cmde.split())
