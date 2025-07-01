# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 11. GÜN - TCP-UDP HABERLEŞMESİ ARAŞTIRMASI VE STM'de ADC İNJECTED MODDA ÇALIŞIRILMASI

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


