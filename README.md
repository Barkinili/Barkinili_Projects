# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 8. GÜN TİMER ile SAYAÇ ÖRNEĞİ

---

# STM32F429ZIT6 – TIM7 ile Zaman Takibi

Bu projede STM32F429ZIT6 mikrodenetleyicisi kullanılarak TIM7 zamanlayıcısı ile yazılım tabanlı bir zaman ölçüm sistemi geliştirildi. Mikrosaniye, milisaniye ve saniye cinsinden süreler bir sayaç mantığıyla hesaplanıyor.

## Projenin Amacı

Temel amaç, bir zamanlayıcı kesmesi (TIM7 interrupt) kullanarak zamanın nasıl takip edileceğini göstermekti. Bu yapı, ileride süreye bağlı çalışan görevlerde veya zaman kontrolü gereken işlemlerde temel olarak kullanılabilir.

## Uygulama Detayları

* TIM7 kesmesi her tetiklendiğinde mikrosaniye sayacı artırılıyor.
* Mikrosaniye 1000 olduğunda sıfırlanıp milisaniye bir artırılıyor.
* Milisaniye 100 olduğunda sıfırlanıyor ve saniye bir artırılıyor.
* Saniye 60’a ulaştığında tekrar sıfırlanıyor.

Bu şekilde sistemde geçen süre yazılım tabanlı olarak takip ediliyor.

## Kullanılan Değişkenler

```c
uint16_t mikrosaniye, milisaniye;
uint8_t saniye, dakika;
```

> Not: `dakika` değişkeni projeye eklendi ama bu örnekte kullanılmadı.

## Donanım ve Ayarlar

* TIM7 aktif hale getirildi ve kesme özelliği açıldı.
* Zamanlayıcı ayarları, her 1 mikrosaniyede bir kesme olacak şekilde yapıldı.
* Kesme fonksiyonu `stm32f4xx_it.c` dosyasında `TIM7_IRQHandler()` içine yazıldı.
* HAL kütüphanesiyle uyumlu çalışması için `HAL_TIM_IRQHandler()` fonksiyonu da çağrıldı.

## Geliştirme Ortamı

* STM32CubeIDE (veya Keil, IAR vs.)
* STM32CubeMX ile temel yapılandırmalar yapıldı
* STM32F429ZIT6 mikrodenetleyici

## Ek Bilgi

Bu tür zamanlayıcı tabanlı sayaç sistemleri, basit süre takibi için oldukça yeterlidir. Daha hassas zamanlama veya gerçek zamanlı uygulamalar için donanımsal timerlar veya RTC kullanımı tercih edilebilir.

---

