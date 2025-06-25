# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 7. GÜN – STM CRC UYGULAMASI 

Bugün STM32 mikrodenetleyici üzerinde CRC (Cyclic Redundancy Check) modülünü kullanarak veri bütünlüğü kontrolü gerçekleştirdim. Çalışmalarım aşağıdaki adımlardan oluştu:

Yapılanlar:
Proje Oluşturma:

STM32CubeIDE kullanılarak yeni bir proje oluşturuldu.

Hedef kart olarak STM32F4 serisi seçildi.

CRC Donanım Modülünü Aktifleştirme:

CubeMX konfigürasyon arayüzünde CRC donanım birimi aktif edildi.

CRC'nin çalışma parametreleri (standart polinom vs.) varsayılan olarak bırakıldı.

Kod Üretimi ve Geliştirme:

Otomatik olarak oluşturulan temel koda ek olarak CRC hesaplama işlemi için bir fonksiyon eklendi.

HAL_CRC_Calculate() fonksiyonu kullanılarak belirli bir veri dizisinin CRC değeri hesaplandı.

Test ve Doğrulama:

Kod, 4 elemandan oluşan bir veri dizisi üzerinde test edildi ve CRC değeri hesaplanarak doğrulandı.

Hesaplanan CRC değeri bir değişkene (crcVal) atandı ve test başarılı bir şekilde tamamlandı.

Gelecek Adımlar:

Bu uygulama, veri doğrulama ve hata tespiti gerektiren projelerde kullanılabilir.

CRC hesaplama fonksiyonunun daha karmaşık veri setleri ve farklı polinomlarla test edilmesi planlanmaktadır.
