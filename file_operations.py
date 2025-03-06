import json
import os


# 1. Metin Dosyası İşleme
def ogrenci_ekle():
    with open("ogrenciler.txt", "a", encoding="utf-8") as file:
        while True:
            ad = input("Dosyaya ekleceğiniz kişinin isim ve soyismini yazınız. [ekleme işlemi bittiğinde 'bitti' yazınız.] = ")
            if ad == "bitti":  # Kullanıcı 'bitti' yazarsa döngü durur
                break
            file.write(f"{ad}\n")  # Yeni ismi dosyaya ekler
    print("Kişiler başarıyla eklendi uygulamadan çıkış yapılıyor.")


def goruntuleme():
    print("\n***Öğrenci İsimlerini Görme***")
    with open("ogrenciler.txt", "r", encoding="utf-8") as file:
        reading = file.read()  # Dosyadaki tüm içerik okunur
        print(reading)  # İçeriği ekrana yazdırır


# 2. Günlük Kayıt Defteri
def gunluk():
    notes = input("Aldığınız notları giriniz [Görüntülemek için 'goruntule' | Dosya'yı silmek için 'sil' yazınız.] = ")
    if notes == "goruntule":
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            reading = dosya.read()  # Dosyadaki notları okur
            print("\n***Kaydedilen Notlar***")
            print(reading)  # Notları ekrana yazdırır
    elif notes == "sil":
        os.remove("gunluk.txt")  # "gunluk.txt" dosyasını siler
        print("Dosya başarıyla silindi.")
    else:
        with open("gunluk.txt", "a", encoding="utf-8") as file:
            file.write(f"{notes}\n")  # Yeni notu dosyaya ekler
            print("Notunuz Kayıt edildi.")


# 3. JSON Kullanarak Kullanıcı Bilgileri Saklama
def kullanici_ekle():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    yas = input("Yaşınız: ")
    kullanici = {'Ad': ad, "Soyad": soyad, "Yaş": yas}
    with open("kullanicilar.json", "a", encoding="utf-8") as dosya:
        json.dump(kullanici, dosya, ensure_ascii=False, indent=4)  # Kullanıcı bilgilerini JSON formatında kaydeder


def listeleme():
    while True:
        liste_ = input("Tüm kullanıcıları görmek için 'listele' komutunu kullanınız = ")
        if liste_.lower() == "listele":
            with open("kullanicilar.json", "r", encoding="utf-8") as dosya:
                data = json.load(dosya)  # JSON dosyasındaki veriyi okur
                print("***Kullanıcı Listeleri***")
                print(data)  # Kullanıcı bilgilerini ekrana yazdırır
        else:
            print("Hatalı komut kullanımı tekrar deneyiniz.")
        break


# 4. Telefon Rehberi Uygulaması
def rehber():
    print("*** Telefon Rehber Uygulaması *** "
          "\n 1. Ekle "
          "\n 2. Ara "
          "\n 3. Listele ")
    while True:
        komut = input("\nYapmak istediğiniz komutu giriniz = ")
        if komut.lower() == "ekle":
            ad = input("Kişinin adı = ")
            no = input("Kişinin numarası = ")
            with open("rehber.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"Kişi Adı = {ad} | Tel No = {no}\n")  # Kişi bilgilerini rehber dosyasına ekler
                print(f"{ad} adlı {no} numaralı kişi rehberinize kayıt edilmiştir.")
        elif komut.lower() == "ara":
            cagri = input("\nAramak istediğiniz kişinin adını giriniz = ")
            with open("rehber.txt", "r", encoding="utf-8") as dosya2:
                for satir in dosya2:
                    if cagri.lower() in satir.lower():  # Aranan kişinin adı rehberde bulunursa, numarası yazdırılır
                        print(f"{ad} adlı kişinin telefon numarası {no}")
                        break
        elif komut.lower() == "listele":
            with open("rehber.txt", "r", encoding="utf-8") as dosya3:
                okuma = dosya3.read()
                if okuma:
                    print(okuma)  # Rehberdeki tüm kayıtları ekrana yazdırır
                else:
                    print("Rehberde hiç kayıt bulunamadı.")
        else:
            print("Hatalı komut kullanımı tekrar deneyiniz.\n")


# 5. Otomatik Log Kayıt Sistemi
def log():
    print("***Otomatik Log Kayıt Sistemi***")
    print("\n Tüm logları görüntülemek istiyorsanız komutu giriniz = [loglari_goruntule")
    input("")  # Logları görüntülemek için komut bekler
    # BURASI EKSİK YAPAMADIM
