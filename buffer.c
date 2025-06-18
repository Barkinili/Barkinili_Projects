#include <stdio.h>
#include <string.h>

#define BUYUKLUK 10

char buffer[BUYUKLUK];
int head = 0;
int tail = 0;
int count = 0;

int push(char value) {
    if (count == BUYUKLUK) {
        return 0; // Dolu
    }
    buffer[head] = value;
    head = (head + 1) % BUYUKLUK;
    count++;
    return 1;
}

int pop(char *value) {
    if (count == 0) {
        return 0; // Boþ
    }
    *value = buffer[tail];
    tail = (tail + 1) % BUYUKLUK;
    count--;
    return 1;
}

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

int main() {
    int secim;
    char giris[100];
    char alinan;

    while (1) {
        printf("\n1 - Ekle (coklu harf veya rakam)\n2 - Oku (cikart)\n0 - Cikis\nSecim: ");
        scanf("%d", &secim);
        while ((getchar()) != '\n');

        switch (secim) {
            case 1:
                printf("Giris (birden fazla harf/rakam yaz): ");
                fgets(giris, sizeof(giris), stdin);
                giris[strcspn(giris, "\n")] = '\0';

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
