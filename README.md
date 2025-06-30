# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 10. GÜN – STM32 ile SICAKLIK ÖLÇÜMÜ ve CUBE MONİTORDE GÖSTERİMİ

Bu projede STM32 mikrodenetleyicisi kullanılarak ADC üzerinden üç kanal okunur:

* **ADC\_CHANNEL\_0**: Harici analog giriş (Vadc1)
* **VREFINT**: Besleme voltajı (Vdda) hesaplaması için
* **TEMPSENSOR**: İç sıcaklık sensörü (Vsense)

Okunan değerler ADC kesmesi ile alınır ve şu hesaplamalar yapılır:

* `Vdda`: Referans voltajına göre gerçek besleme voltajı
* `Vadc1`: Harici analog pinin gerçek voltajı
* `temp`: Dahili sıcaklık sensörüne göre sıcaklık değeri

Sıcaklık hesabı şu formülle yapılır:
`temp = ((Vsense - 0.76) / 0.0025) + 25`

Tüm işlemler kesme fonksiyonu içinde yapılır. `main()` döngüsü boş bırakılmıştır. ADC sürekli modda ve kesme ile çalışır.

Kod STM32CubeIDE ile yazıldı ve HAL kütüphanesi kullanıldı.


## CUBE MONİTORDE GÖSTERİM

Bu kısımda ise cube monitor uygulaması üzerinden grafiksel ve gauge ile gösterim gerçekleştirildi.
