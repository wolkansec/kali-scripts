#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Sistem Zafiyet Analiz Programı")

os.system("apt-get install lynis")
os.system("lynis audit system")
