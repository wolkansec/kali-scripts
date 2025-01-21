#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("VPN Kontrol Aracı")
hedef_ip = raw_input("Hedef IP: ")
os.system("ike-scan " + hedef_ip)
