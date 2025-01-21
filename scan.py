#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Port Tarama Seçenekleri
1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi
4) Güvenlik Açığı Taraması
5) Derinlemesine Tarama
6) Belirli Portları Tara
""")

islem_no = input("İşlem Numarasını Girin (1,2,3,4,5,6): ")
hedef_ip = input("Hedef IP veya Domain Girin: ")

if islem_no == "1":
	os.system(f"nmap -T4 {hedef_ip}")

elif islem_no == "2":
	os.system(f"nmap -sS -sV {hedef_ip}")
	
elif islem_no == "3":
        os.system(f"nmap -O {hedef_ip}")
   
elif islem_no == "4":
        os.system(f"nmap --script vuln {hedef_ip}")

elif islem_no == "5":
        os.system(f"nmap -A -T4 {hedef_ip}")

elif islem_no == "6":
        portlar = input("Tarayacağınız portları virgülle ayırarak girin (örn: 80,443,22): ")
        os.system(f"nmap -p {portlar} {hedef_ip}")

else:
        print("Hatalı tuşlama yaptınız!")
