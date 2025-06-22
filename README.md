# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 4. GÜN – DOXYGEN İLE HTML DOKÜMANTASYON OLUŞTURMA

### Doxygen Nedir?

Doxygen, C/C++ gibi programlama dillerinde yazılmış projelerde kaynak kod içerisindeki açıklamaları (yorumları) toplayarak otomatik şekilde dokümantasyon (belgelendirme) üretmeye yarayan bir araçtır. HTML, PDF, LaTeX gibi farklı çıktılar verebilir.

---

### Aşamalar

#### 1. Doxygen Kurulumu

* Linux:

  ```bash
  sudo apt install doxygen
  ```

* Windows:

  * [https://www.doxygen.nl/download.html](https://www.doxygen.nl/download.html) adresinden indirip kurulum yapılır.

---

#### 2. Doxyfile Dosyasının Oluşturulması

Terminal veya komut istemcisinde proje dizininde aşağıdaki komut girilir:

```bash
doxygen -g
```

Bu komut bulunduğun dizine varsayılan ayarlarla bir `Doxyfile` oluşturur.

---

#### 3. Doxyfile Ayarlarının Düzenlenmesi

`Doxyfile` dosyasını bir metin düzenleyici ile açıp aşağıdaki ayarları güncelle:

```ini
PROJECT_NAME           = "Circular Buffer"
INPUT                  = main.c
OUTPUT_DIRECTORY       = docs
RECURSIVE              = NO
EXTRACT_ALL            = YES
SOURCE_BROWSER         = NO
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = YES
GENERATE_HTML          = YES
GENERATE_LATEX         = NO
```

> Not: `INPUT` alanına `.c` veya `.h` dosyalarının ismini yazabilirsin.

---

#### 4. Kodun Belgelendirilmesi

Kod içerisine Doxygen yorumları eklendi. Örnek:

```c
/**
 * @brief Buffer'a karakter ekler (push islemi)
 * @param value Eklenecek karakter
 * @return 1 basari, 0 basarisiz
 */
int push(char value);
```

Bu format sayesinde Doxygen, fonksiyonlar ve açıklamalarını otomatik olarak ayıklar.

---

#### 5. HTML Dokümantasyonunun Oluşturulması

Dökümantasyonu oluşturmak için terminalden:

```bash
doxygen Doxyfile
```

komutu çalıştırılır. İşlem sonunda `docs/html/` klasörü altında `index.html` dosyası oluşur.

---

#### 6. Dokümantasyonun Görüntülenmesi

Oluşan HTML dosyalarını bir web tarayıcısı ile açabilirsin:

```bash
xdg-open docs/html/index.html
```

veya Windows'ta doğrudan `docs/html/index.html` dosyasına çift tıklanarak açılabilir.

---

### Sonuç

Doxygen kullanılarak `main.c` dosyası içerisindeki açıklamalardan okunabilir, şık bir HTML belgeleri seti oluşturulmuştur. Böylece proje belgelenmesi standartlara uygun hale getirilmiştir.

