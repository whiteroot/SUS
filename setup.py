#!/usr/bin/env python
# coding: utf8

import subprocess

cmde = 'python -m pip install -r requirements.txt'
p = subprocess.call(cmde, shell=True)
