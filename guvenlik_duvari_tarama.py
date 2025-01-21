#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Güvenlik Duvarı Tespiti")
target = raw_input("Site Adresini Girin: ")
os.system("wafw00f " + target)
