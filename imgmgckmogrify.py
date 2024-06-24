import os


informat = input("type in the format that you will convert from: ")
outformat = input("type in the format that you will convert to: ")

try:
    # Sistem komutunu çalıştırarak dosya formatlarını dönüştür
    os.system(f"cmd /K magick mogrify -format {outformat} *.{informat}")
except Exception as e:
    # Hata mesajını yazdır
    print(f"could not execute command: {e}")