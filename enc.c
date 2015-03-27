#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

void uint32_t_dump(uint32_t val)
{
    uint8_t *buf = (uint8_t *) &val;

    for (int i = 0; i < sizeof(uint32_t); ++i) {
        printf("0x%02X", (uint8_t)*(buf+i));
        if (i < sizeof(uint32_t) - 1) {
            printf(" ");
        }
    }
    printf("\n");
    
}

int main (int argc, char *argv[])
{
    for (int i = 1; i < argc; i+=2) {
        char *val = argv[i];
        char *type = argv[i+1];
        
        if (!strcmp(type, "uint32_t")) {
            uint32_t_dump((uint32_t) atoi(val));
        }
    }
}