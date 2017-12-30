#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    /* The hh, j, z, and t length prefixes are not supported in visual studio use %Iu in this case */
    printf("Storage size for char : %zu \n", sizeof(char));
    printf("Storage size for short : %zu \n", sizeof(short));
    printf("Storage size for int : %zu \n", sizeof(int));
    printf("Storage size for long : %zu \n", sizeof(long));
    printf("Storage size for long long : %zu \n", sizeof(long long));

    printf("Storage size for unsigned char : %zu \n", sizeof(unsigned char));
    printf("Storage size for unsigned short : %zu \n", sizeof(unsigned short));
    printf("Storage size for unsigned int : %zu \n", sizeof(unsigned int));
    printf("Storage size for unsigned long : %zu \n", sizeof(unsigned long));
    printf("Storage size for unsigned long long : %zu \n", sizeof(unsigned long long));


    printf("Storage size for float : %zu \n", sizeof(float));
    printf("Storage size for double : %zu \n", sizeof(double));
    printf("Storage size for long double : %zu \n", sizeof(long double));

    printf("Minimum float positive value : %f \n", FLT_MIN);
    printf("Maximum float positive value : %f \n", FLT_MAX);
    printf("Precision value : %d \n", FLT_DIG);

    printf("Storage size for void : %zu \n", sizeof(void));

    return 0;
}
