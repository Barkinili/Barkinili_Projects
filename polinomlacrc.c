#include <stdio.h>

unsigned char calculate_crc(unsigned char *data, int len, unsigned char poly, unsigned char init, unsigned char xor_out) {
    unsigned char crc = init;

    for (int j = 0; j < len; j++) {
        crc ^= data[j];
        for (int i = 0; i < 8; i++) {
            if (crc & 0x80)
                crc = (crc << 1) ^ poly;
            else
                crc <<= 1;
        }
    }

    crc ^= xor_out;
    return crc;
}

int main() {
    unsigned char mesaj[256];
    int adet;
    unsigned char poly = 0x07;
    unsigned char init = 0x00;
    unsigned char xor_out = 0x55;

    printf("Kac adet hex deger gireceksiniz? ");
    scanf("%d", &adet);

    if (adet <= 0 || adet > 256) {
        printf("Gecersiz adet.\n");
        return 1;
    }

    for (int i = 0; i < adet; i++) {
        printf("%d. hex degeri girin (0x ile veya onsuz): ", i + 1);
        unsigned int temp;
        scanf("%x", &temp);
        mesaj[i] = (unsigned char)temp;
    }

    printf("\nGirdi (Hex): ");
    for (int i = 0; i < adet; i++) {
        printf("0x%02X ", mesaj[i]);
    }
    printf("\n");

    unsigned char crc_sender = calculate_crc(mesaj, adet, poly, init, xor_out);
    unsigned char crc_receiver = calculate_crc(mesaj, adet, poly, init, xor_out);

    printf("\nSonuclar:\n");
    printf("Result\tCheck\tPoly\tInit\tXorOut\n");
    printf("0x%02X\t0xA1\t0x%02X\t0x%02X\t0x%02X\n", crc_sender, poly, init, xor_out);

    if (crc_sender == crc_receiver) {
        printf("\nVeri dogru iletildi.\n");
    } else {
        printf("\nVeri yanlis iletildi.\n");
    }

    return 0;
}
