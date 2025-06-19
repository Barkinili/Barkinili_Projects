/**
 * @file buffer.c
 * @brief Dairesel (circular) karakter tamponu (FIFO) uygulamasi
 *
 * Bu program, sabit boyutlu bir tampon (buffer) kullanarak karakter ekleme ve cikarma islemleri yapar.
 * Tampon bir kuyruk (queue) mantigi ile calisir: Ilk giren karakter ilk cikar (FIFO).
 *
 * Kullaniciya bir menu sunulur. Bu menu araciligiyla kullanici:
 * - Coklu karakter girisi yaparak buffer'a veri ekleyebilir,
 * - Mevcut buffer'dan bir karakter okuyabilir (cikarabilir),
 * - Tamponun mevcut durumunu gorebilir,
 * - Veya cikis yapabilir.
 */

#include <stdio.h>     /**< Giris/Cikis islemleri icin gerekli kutuphane */
#include <string.h>    /**< Karakter dizisi islemleri icin kutuphane */

/**
 * @def BUYUKLUK
 * @brief Tamponun (buffer) maksimum kapasitesi
 */
#define BUYUKLUK 10

/**
 * @brief Dairesel tamponu temsil eden global degiskenler
 */
char buffer[BUYUKLUK];  /**< Karakterleri tutacak olan buffer */
int head = 0;           /**< Yeni karakterin eklenecegi konum */
int tail = 0;           /**< Okunacak karakterin konumu */
int count = 0;          /**< Tampondaki mevcut karakter sayisi */

/**
 * @brief Buffer'a karakter ekler (push islemi)
 * 
 * Eger buffer doluysa karakter eklenemez.
 * 
 * @param value Eklenecek karakter
 * @return int 1 basari, 0 basarisiz (buffer dolu)
 */
int push(char value) {
    if (count == BUYUKLUK) {
        return 0; // Dolu
    }
    buffer[head] = value;
    head = (head + 1) % BUYUKLUK;
    count++;
    return 1;
}

/**
 * @brief Buffer'dan karakter okur (pop islemi)
 * 
 * Eger buffer bossa karakter okunamaz.
 * 
 * @param value Okunan karakterin yazilacagi adres
 * @return int 1 basari, 0 basarisiz (buffer bos)
 */
int pop(char *value) {
    if (count == 0) {
        return 0; // Bos
    }
    *value = buffer[tail];
    tail = (tail + 1) % BUYUKLUK;
    count--;
    return 1;
}

/**
 * @brief Buffer'in mevcut durumunu grafiksel olarak ekrana yazdirir
 *
 * Dolular karakterlerle, bos alanlar '-' ile gosterilir.
 */
void buffer_goster() {
    printf("Buffer durumu: [");
    for (int i = 0; i < BUYUKLUK; i++) {
        if (count == 0) {
            printf(" -");
        } else {
            int aktif = 0;
            if (tail < head) {
                if (i >= tail && i < head) aktif = 1;
            } else if (tail > head) {
                if (i >= tail || i < head) aktif = 1;
            } else if (count == BUYUKLUK) {
                aktif = 1;
            }

            if (aktif) {
                printf(" %c", buffer[i]);
            } else {
                printf(" -");
            }
        }
    }
    printf(" ]\n");
}

/**
 * @brief Programin giris noktasi (main fonksiyonu)
 *
 * Kullaniciya etkilesimli bir menu sunar.
 * 1. Coklu karakter ekleme
 * 2. FIFO'dan karakter okuma
 * 0. Programdan cikis
 * 
 * @return int Programdan cikis kodu
 */
int main() {
    int secim;
    char giris[100];
    char alinan;

    while (1) {
        printf("\n1 - Ekle (coklu harf veya rakam)\n2 - Oku (cikart)\n0 - Cikis\nSecim: ");
        scanf("%d", &secim);
        while ((getchar()) != '\n'); // Enter karakterini temizle

        switch (secim) {
            case 1:
                printf("Giris (birden fazla harf/rakam yaz): ");
                fgets(giris, sizeof(giris), stdin);
                giris[strcspn(giris, "\n")] = '\0'; // Satir sonunu kaldir

                for (int i = 0; i < strlen(giris); i++) {
                    if (push(giris[i])) {
                        printf("Eklendi: %c\n", giris[i]);
                    } else {
                        printf("Buffer dolu, eklenemedi: %c\n", giris[i]);
                        break;
                    }
                }
                buffer_goster();
                break;

            case 2:
                if (pop(&alinan)) {
                    printf("Okunan karakter: %c\n", alinan);
                } else {
                    printf("Buffer bos!\n");
                }
                buffer_goster();
                break;

            case 0:
                printf("Programdan cikiliyor...\n");
                return 0;

            default:
                printf("Gecersiz secim!\n");
        }
    }

    return 0;
}

