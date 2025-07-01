# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 11. GÜN - TCP-UDP HABERLEŞMESİ ARAŞTIRMASI VE ADC'nin İNJECTED MODDA ÇALIŞIRILMASI

# Ağ Protokolleri ve Temel Ağ Kavramları

## TCP (Transmission Control Protocol)

* Veri iletimi öncesi bir bağlantı kurar ve bu bağlantı noktası üzerinden iletişim kurar.
* Doğru ve güvenli veri iletimi sağlar.

## UDP (User Datagram Protocol)

* Bağlantı kurmadan veri paketi gönderir.
* Hızlıdır ancak güvenli değildir.
* Küçük veri paketleri için uygundur.

## Bant Genişliği (Bandwidth)

* Bant genişliği, veri transferi veya akış yoğunluğunu belirler.
* Trafik sorunu yaşanıyorsa bandwidth artırılır.
* Bandwidth, site trafiğine limit koyar.

## İletim Türleri

* **Unicast**: Noktadan noktaya özel iletişim için idealdir.
* **Multicast**: Bir kaynaktan birkaç hedefe veri göndermeyi amaçlar.
* **Broadcast**: Ağdaki tüm cihazlara veri gönderir.

## Multicast IP Aralıkları

* IPv4 multicast adres aralığı: `224.0.0.0` - `239.255.255.255`
* `224.0.0.0`: Yerel ağda kullanılan multicast
* `224.0.1.0`: İnternette yönlendirilebilir multicast
* `239.0.0.0`: Özel multicast aralığı
* `224.0.0.1`: Tüm cihazlara multicast göndermek için kullanılır

## Adres Çözümleme (ARP - Address Resolution Protocol)

* IP adresine karşılık gelen MAC adresini bulmak için kullanılır.
* ARP isteği ve yanıtı ile çalışır.

## OSI Modeli Katmanları

* Ağ (Network) katmanındaki IP adresi ile Veri Bağlantı (Data Link) katmanındaki MAC adresi eşleştirilir.

## Gateway

* Farklı ağlar veya iletişim protokolleri arasında çevirmen/araç görevi yapar.

## Subnet Mask

* IP adresinin hangi kısmının ağ adresi ve hangi kısmının cihaz adresi olduğunu belirler.
 
Tabii, işte daha sade ve doğal bir dille yazılmış, README dosyasına uygun hali:

---

## Injected Modda ADC Kullanımı

Bu bölümde ADC, injected modda çalışacak şekilde ayarlandı. Önceki örneklerden farklı olarak bu modda ADC, yazılım tarafından değil, Timer 1 tarafından tetikleniyor.

### Yapılanlar

* `ioc` dosyası üzerinden injected mod aktif edildi.
* Injected modda iki kanal kullanıldı: `VREFINT` ve `TEMPSENSOR`.
* Tetikleme kaynağı olarak Timer 1'in TRGO sinyali seçildi.
* Timer 1, her 1 saniyede bir ADC'yi tetikleyecek şekilde ayarlandı.

### Callback Fonksiyonu

ADC dönüşü tamamlandığında aşağıdaki callback fonksiyonu çalışıyor. Burada önce VREF ve sıcaklık sensöründen okunan ADC değerleri alınıyor, ardından sıcaklık değeri hesaplanıyor:

```c
void HAL_ADCEx_InjectedConvCpltCallback(ADC_HandleTypeDef *hadc)
{
    if (hadc->Instance == ADC1)
    {
        adc1_value[0] = HAL_ADCEx_InjectedGetValue(hadc, ADC_INJECTED_RANK_1);
        adc1_value[1] = HAL_ADCEx_InjectedGetValue(hadc, ADC_INJECTED_RANK_2);

        Vdda   = 3.3f * (*VREFIN_CAL) / adc1_value[0];
        Vsense = Vdda * adc1_value[1] / 4095.0f;
        temp   = ((Vsense - V25) / Avg_slope) + 25.0f;
    }
}
```

Bu yapı sayesinde, sıcaklık değeri her saniye otomatik olarak ölçülüyor. Timer kesmesi kullanmak da mümkün, ancak TRGO tetiklemesi doğrudan ADC'yi çalıştırdığı için buna gerek kalmadan sistem düzgün çalışıyor.

---


