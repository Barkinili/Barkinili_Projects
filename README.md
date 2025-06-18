*ASİSPROJELER*
Bu mainde isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.


----------------------------------------------------------------------------
__1. gün Gömülü sistem katmanları__

GÖMÜLÜ YAZILIM KATMANLARI 

1. Application Layer (Uygulama Katmanı)
- En üst katmandır.
- Kullanıcının isteğini yerine getirir.
- Sensör okuma, veri işleme, ekran yazdırma gibi görevler burada yazılır.
- Middleware veya API'leri kullanarak alt katmanlara erişir.

2. Middleware Layer (Ara Yazılım Katmanı)
- Uygulama ile işletim sistemi/donanım arasındaki ara katmandır.
- Dosya sistemi, ağ protokolleri, USB sürücüsü, kriptografi gibi hizmetler sunar.
- Kod tekrarını azaltır, taşınabilirliği artırır.
- Örnekler: LWIP, FATFS, MQTT, USB stack, GUI kütüphaneleri
- RTOS değildir ama RTOS üzerinde çalışır.
- RTOS ≠ Middleware

3. RTOS Layer (Gerçek Zamanlı İşletim Sistemi)
- Görevleri planlar, zamanlayıcı çalıştırır, kaynakları yönetir.
- Görevler arası geçiş, öncelik, zamanlama sağlar.
- Örnekler: FreeRTOS, ThreadX (Azure RTOS), QNX, embOS
- Middleware bu katmanın üstünde çalışır.

4. Hardware Abstraction Layer (HAL)
- Donanım erişimini kolaylaştırır.
- Her mikrodenetleyiciye özel sürücüler içerir.
- GPIO, UART, ADC gibi çevre birimlerini soyutlar.
- Kodun taşınabilir olmasına katkı sağlar.

5. Low-Level Drivers / Peripherals
- Mikrodenetleyicinin doğrudan kontrol edildiği katmandır.
- Register tabanlı donanım kontrolü buradadır.
- Örneğin: GPIO pin'ine HIGH/LOW yazmak.

6. Hardware (Fiziksel Katman)
- Gerçek fiziksel devre, mikrodenetleyici, sensörler, butonlar, motorlar vs.


MUTEX ve SEMAPHORE BENZETMESİ:

1. Mutex (Karşılıklı Dışlama)
- Tuvalet anahtarı gibidir.
- Anahtar kimdeyse sadece o girebilir.
- Diğerleri bekler. Sadece bir kişi kullanabilir.

2. Binary Semaphore
- Tuvalet kapısının kilidi gibidir.
- İçeri biri girince kapı kapanır.
- Diğerleri içerisi boşalana kadar bekler.

3. Counting Semaphore
- Birden fazla tuvaletin olduğu bir yerde sıra gibidir.
- Örneğin 3 kabin varsa 3 kişi aynı anda girebilir.
- Diğerleri sırada bekler. Bekleyen sayısı semafor sayısıdır.



NOTLAR:

- Middleware RTOS değildir, RTOS üzerinde çalışır.
- RTOS sistem kaynaklarını yönetirken, middleware uygulama desteği sunar.
- Uygulama katmanı yalnızca üstteki iş mantığını içerir.




----------------------------------------------------------------------------
__2. gün git bash işlemleri__

Bu bilgiler başlangıç için gereklidir.

$ git config --global user.name "[name]"

$ git config --global user.email "[email address]"


masaüstü üzerinde bir dosya oluşturup dosya içine readme ve txt oluşturma için gerekli kodlar 
cd ~/Desktop

mkdir proje

cd proje

touch yapilanlar.txt

touch README.md

git init

git add .

git commit -m "İlk commit"

git branch -M main

git remote add origin https://github.com/Barkinili/asisprojeler.git

git push -u origin main 


----------------------------------------------------------------------------
__3. gün circular buffer çalışması__

