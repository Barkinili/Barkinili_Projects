# ASISP PROJELER

Bu `main` dosyasinda isterler sonucunda elde edilen arastirma sonuclari ve kodlar yer almaktadir.

---

## 1. GÜN GÖMÜLÜ YAZILIM KATMANLARI

### GÖMÜLÜ YAZILIM KATMANLARI

1. **Application Layer (Uygulama Katmani)**  
   - En ust katmandir.  
   - Kullanicinin istegini yerine getirir.  
   - Sensor okuma, veri isleme, ekran yazdirma gibi gorevler burada yazilir.  
   - Middleware veya API'leri kullanarak alt katmanlara erisir.

2. **Middleware Layer (Ara Yazilim Katmani)**  
   - Middleware, uygulama programlama arabirimi olusturmamizi saglayan ara yazilim katmanidir.  
   - Dosya sistemi, ag protokolleri, USB surucusu, kriptografi gibi hizmetler sunar.  
   - Kod tekrarini azaltir, tasinabilirligi artirir.  
   - Ornekler: LWIP, FATFS, MQTT, USB stack, GUI kutuphaneleri  
   - RTOS degildir ama RTOS uzerinde calisir.  
   - RTOS ≠ Middleware

3. **RTOS Layer (Gercek Zamanli Isletim Sistemi)**  
   - Gorevleri planlar, zamanlayici calistirir, kaynaklari yonetir.  
   - Gorevler arasi gecis, oncelik, zamanlama saglar.  
   - Ornekler: FreeRTOS, ThreadX (Azure RTOS), QNX, embOS  
   - Middleware bu katmanin ustunde calisir.

4. **Hardware Abstraction Layer (HAL)**  
   - Donanim erisimini kolaylastirir.  
   - Her mikrondenetleyiciye ozel suruculer icerir.  
   - GPIO, UART, ADC gibi cevre birimlerini soyutlar.  
   - Kodun tasinabilir olmasina katki saglar.

5. **Low-Level Drivers / Peripherals**  
   - Mikrondenetleyicinin dogrudan kontrol edildigi katmandir.  
   - Register tabanli donanim kontrolu buradadir.  
   - Ornegin: GPIO pin'ine HIGH/LOW yazmak.

6. **Hardware (Fiziksel Katman)**  
   - Gercek fiziksel devre, mikrondenetleyici, sensorler, butonlar, motorlar vs.

---

### MUTEX ve SEMAPHORE BENZETMESI

1. **Mutex (Karsilikli Dislama)**  
   - Tuvalet anahtari gibidir.  
   - Anahtar kimdeyse sadece o girebilir.  
   - Digerleri bekler. Sadece bir kisi kullanabilir.

2. **Binary Semaphore**  
   - Tuvalet kapisinin kilidi gibidir.  
   - Iceri biri girince kapi kapanir.  
   - Digerleri icerisi bosalana kadar bekler.

3. **Counting Semaphore**  
   - Birden fazla tuvaletin oldugu bir yerde sira gibidir.  
   - Ornegin 3 kabin varsa 3 kisi ayni anda girebilir.  
   - Digerleri sirada bekler. Bekleyen sayisi semafor sayisidir.

---

### NOTLAR

- Middleware RTOS degildir, RTOS uzerinde calisir.  
- RTOS sistem kaynaklarini yonetirken, middleware uygulama destegi sunar.  
- Uygulama katmani yalnizca ustteki is mantigini icerir.
