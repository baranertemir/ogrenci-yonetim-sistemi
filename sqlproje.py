#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 03:33:41 2020

@author: A.Baran Ertemir
"""

import sqlite3

veri = sqlite3.connect("ogrenciler.db") # ogrenciler.db adli database dosyasini olusturur ve bizi ona baglar.
cursor = veri.cursor() # Database uzerindeki tum islemleri bu cursor uzerinden yapicagiz.


def table_create():
    # Bu fonksiyon sayesinde database uzerinde table olusturma islemlerimizi yapiyoruz.
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (isim TEXT,soyisim TEXT,sinif INT,sube TEXT,okul TEXT)")
    # Execute metodu bizim SQL sorgusu execute etmemize yarar.
    veri.commit()
    # Her islemden sonra database uzerinde bu verilerin guncellenmesi icin commit metodunu kullanmamiz gerekir.

#Olusturdugumuz bu fonksiyonu cagiriyoruz.
table_create()   
 
def ogrenci_ekle(a,b,c,d,e):
    # Veri ekleme islemi icin kullandigimiz fonksiyon.
    cursor.execute("INSERT INTO ogrenciler Values(?,?,?,?,?)",(isim,soyisim,sinif,sube,okul))
    veri.commit()
    
def verileri_al():
    # Database uzerindeki verilerin cagirilmasi yapiliyor.
    cursor.execute('SELECT * FROM ogrenciler')
    liste = cursor.fetchall()
    print('Ogrencilerin bilgileri yukleniyor...')
    for i in liste:
        print(i)

def sinif_degis(eski,yeni):
    # Bu fonksiyonlar sayesinde sinif,okul,sube degisiklikleri yapiliyor.
    cursor.execute("UPDATE ogrenciler set sinif = ? where sinif = ?",(yeni,eski))
    veri.commit()
    
# sinif_degis(11,12)
    
def okul_degis(eski,yeni):
    cursor.execute("UPDATE ogrenciler set okul = ? where okul = ?",(yeni,eski))
    veri.commit()

# okul_degis("Ataturk Ortaokulu,Selimiye Ortaokulu")

def sube_degis(eski,yeni):
    cursor.execute("UPDATE ogrenciler set sube = ? where sube = ?",(yeni,eski))
    veri.commit()

# sube_degis("A,F")

def sinifi_sil(sinif):
    cursor.execute("DELETE FROM ogrenciler where sinif = ?",(sinif,)) #DELETE from ogrenciler where sinif = 12
    veri.commit

#sinifi_sil(9)
#Sinif sırasına göre silme işlemi yapmaya yarayan fonksiyon.

print("""-----------------------------------

Ogrenci Veri Tabani Programına Hoşgeldiniz.

İşlemler;

[1] Ogrencileri Göster

[2] Ogrenci Ekle

Çıkmak için 'q' ya basın.
-----------------------------------""")



while True:
    islem = input("Islem :")
    
    if islem == '1':
        verileri_al()

    elif islem == '2':
        isim = input("Ogrencinin Adi:")
        soyisim = input("Ogrencinin Soyadi:")
        sinif = input('Ogrencinin Sinifi:')
        sube = input('Ogrencinin Subesi:')
        okul = input('Ogrencinin Okulu:')
        ogrenci_ekle(isim,soyisim,sinif,sube,okul)
    elif islem == "q" or islem == "Q":
        print('Basariyla cikis yapildi.')
        break    
        



