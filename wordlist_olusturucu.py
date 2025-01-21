#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Wordlist Oluşturma Programı")

minimumkarakter = raw_input("Minimum Karakter Sayısını Girin: ")
maksimumkarakter = raw_input("Maksimum Karakter Sayısını Girin: ")
karakter = raw_input("İstediğiniz Karakterleri Girin: ")

os.system("crunch "+minimumkarakter+" "+maksimumkarakter+" "+karakter)
print("İşlem Tamamlandı!")
