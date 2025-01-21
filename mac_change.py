#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
MAC Adresi Değiştirme
1) MAC Adresini Rastgele Belirle
2) MAC Adresini Elle Belirle
3) MAC Adresini Orijinale Döndür

""")

islem_no = raw_input("İşlem Numarasını Girin (1,2,3): ")

if(islem_no == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\nMac Adresi Rastgele Belirlendi!")

elif(islem_no == "2"):
	mac_adres = raw_input("Yeni MAC Adresini Girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + mac_adres + " eth0")
	os.system("ifconfig eth0 up")
	print("\nMAC Adresi Elle Belirlendi!")

elif(islem_no == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\nMAC Adresi Orijinale Döndürüldü!")

else:
	print("Hatalı tuşlama yaptınız.!")

