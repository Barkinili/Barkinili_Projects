# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 3. GÜN CİRCULAR BUFFER İLE C DİLİNDE ÖRNEKLEME__

Amaç
Bu proje, sabit boyutlu bir bellek alanı üzerinde karakter tabanlı verileri FIFO (First In First Out) mantığıyla işleyen bir dairesel tampon 
(circular buffer) yapısının C dilinde gerçekleştirilmesini amaçlamaktadır. 
Dairesel tampon yapıları, gömülü sistemler, veri iletim hatları ve donanım arayüzlerinde sıkça kullanılan, verimli bir bellek yönetim yöntemidir.

Yapım Aşamaları
1. Konsept ve Gereksinim Belirleme
FIFO prensibi, veri yapıları ve tampon yönetimi konuları araştırıldı.

Proje C dili ile yazılacak şekilde planlandı.

Karakter tabanlı bir tampon (char buffer) kullanılmasına karar verildi.

Temel işlevler belirlendi: veri ekleme (push), veri okuma (pop), tampon durumunu gösterme (buffer_goster).

2. Değişkenlerin Tanımlanması
char buffer[BUYUKLUK]: Tampon dizisi.

int head: Yeni verinin ekleneceği indeks.

int tail: Okunacak verinin bulunduğu indeks.

int count: Tampondaki mevcut veri sayısı.

BUYUKLUK: Tamponun maksimum kapasitesi olarak #define ile tanımlandı.

3. Fonksiyonların Yazılması
push(char value): Tampon dolu değilse, verilen karakteri ekler. head konumu güncellenir.

*pop(char value): Tampon boş değilse, karakteri okur ve tail konumu güncellenir.

buffer_goster(): Tamponun anlık durumunu grafiksel olarak terminalde gösterir.

4. Kullanıcı Arayüzü (CLI) Oluşturulması
Basit bir menü sistemi eklendi:

1: Çoklu karakter ekleme

2: FIFO’dan karakter çıkarma

0: Programdan çıkış

Kullanıcının giriş yaptığı karakter dizisi sırayla tampon içine yerleştirilir.

Her işlem sonrası tamponun durumu ekranda gösterilir.

5. Test ve Hata Kontrolü
Tamponun dolu ve boş olduğu durumlar test edilerek sınır kontrolleri yapıldı.

Giriş kontrolleri (örneğin: fazla karakter girişi, boş tampondan okuma gibi) eklendi.

Terminal çıktılarının kullanıcı dostu olması sağlandı.

6. Dokümantasyon
Tüm fonksiyonlar ve global değişkenler Doxygen standartlarına uygun şekilde belgelendi.

Kod içerisinde anlaşılır açıklamalar ve yorum satırları eklendi.

Doxyfile ile HTML formatında otomatik belge üretimi test edildi.

Kazanımlar
Bu proje ile aşağıdaki konularda pratik bilgi edinildi:

Dairesel tampon (circular buffer) mantığı ve uygulaması

Gömülü sistemlerde bellek yönetimi yaklaşımı

Fonksiyon tasarımı, sınır kontrolü ve kullanıcı arayüzü mantığı

Doxygen ile kodun otomatik belgelenmesi
