#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Zaafiyet Analiz Aracı")
hedef_ip = raw_input("Hedef IP: ")
os.system("nikto -h " + hedef_ip)
