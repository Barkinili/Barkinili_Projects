# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 5. GÜN – STM32 GELİŞTİRME KARTINDA DMA UART İLE TRANSMİT VE RECEİVE DATA İŞLEMİ GERÇEKLEŞTİRİLMESİ 

---

## 📡 UART Nedir?

**UART (Universal Asynchronous Receiver Transmitter)**, seri haberleşme protokolüdür. İki cihaz arasında **asenkron** şekilde (yani saat sinyali olmadan) veri gönderimi sağlar.

- RX: Veri alma (Receive)
- TX: Veri gönderme (Transmit)
- Tipik olarak 8-bit veri, 1 start ve 1 stop biti ile iletilir.
- Hız (baud rate): 9600, 115200 vb.

STM32'de `HAL_UART_Transmit()` veya `HAL_UART_Transmit_DMA()` fonksiyonları ile kullanılır.

---

## 🚀 DMA Nedir?

**DMA (Direct Memory Access)**, işlemcinin (CPU) müdahalesi olmadan verinin **bellek (RAM) ile çevresel birim (UART, ADC, SPI)** arasında doğrudan taşınmasını sağlar.

Avantajları:
- CPU meşgul edilmez.
- Daha hızlı ve verimli veri transferi yapılır.
- Arka planda transfer çalışır, işlemci başka işler yapabilir.

DMA ile UART birleştiğinde, veri gönderimi `HAL_UART_Transmit_DMA()` fonksiyonu ile başlatılır, transfer tamamlandığında `HAL_UART_TxCpltCallback()` otomatik çağrılır.


---

## 🛠 Fonksiyonlar

- `HAL_UART_Transmit_DMA(...)`: DMA ile UART gönderimini başlatır.
- `HAL_UART_TxCpltCallback(...)`: Gönderim tamamlandığında çağrılır.
- `HAL_GPIO_ReadPin(...)`: Butonun basılıp basılmadığını kontrol eder.

---

## 🧠 Notlar

- DMA transferi sırasında başka işlem yapılabilir.
- Buton sürekli basılı tutulsa bile `"merhaba"` sadece bir defa gönderilir.
- DMA ile yapılan haberleşme, kesme (interrupt) temelli olduğu için verimli ve hızlıdır.

---


