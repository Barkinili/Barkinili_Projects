# ASIS PROJELER

Bu `main` dosyasında isterler sonucunda elde edilen araştırma sonuçları ve kodlar yer almaktadır.

---

## 6. GÜN – CRC NEDİR ve C DİLİNDE UYGULAMASI

Cyclic Redundancy Check (CRC), veri iletiminde hataların tespit edilmesi için yaygın olarak kullanılan bir hata kontrol algoritmasıdır. Bu algoritma, gönderilen veriyi bir polinomla böler ve kalan değeri kontrol etmek için kullanır. CRC-8, CRC algoritmasının 8 bitlik bir versiyonudur ve genellikle düşük seviyeli veri iletim protokollerinde tercih edilir.

### CRC-8 Polinomu ve Hesaplama

CRC-8, genellikle 8 bit uzunluğunda bir kontrol değeri hesaplamak için kullanılır. Bu işlem, verinin her bir baytını bir polinomla böler ve kalan değeri elde eder. CRC-8 hesaplamasında kullanılan en yaygın polinom şu şekilde ifade edilir:

```
x^8 + x^2 + x + 1
```

Bu polinom, genellikle 0x07 (7) olarak gösterilir. Bu polinomun her bir biti, CRC algoritmasının her aşamasında nasıl kullanılacağını belirler. Verinin her bir bitinin işlenmesi sırasında, bu polinom ile yapılan bölme işlemiyle elde edilen kalan değer, veri iletimi sırasında hata kontrolü için kullanılır.

### CRC-8 Hesaplamada Lookup Table (Arama Tablosu) Yöntemi

CRC-8 hesaplamalarını hızlandırmak için "lookup table" (arama tablosu) yöntemi kullanılabilir. Arama tablosu, önceden hesaplanmış CRC-8 değerlerini saklar ve her bir byte için bu tablodan hızlıca değer almayı sağlar. Bu yöntem, özellikle yüksek hızda veri iletimi gerektiğinde işlem süresini önemli ölçüde azaltır.

Bir lookup table, 256 farklı byte değeri için CRC-8 değerlerini önceden hesaplar. Veriyi işlerken her byte için bu tablodan karşılık gelen CRC-8 değeri alınır ve hızla hesaplama yapılır. Bu sayede, her bir bitin işlenmesi yerine doğrudan tabloyu kullanarak daha hızlı bir işlem gerçekleştirilir.






