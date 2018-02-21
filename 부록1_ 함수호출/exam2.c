#include <stdio.h>
#include <string.h>

void A(int a)
{
        printf("A function is called\n");
}

void B(int a, int b)
{
        printf("B function is called\n");
        printf("%d %d\n",a,b);
}

void C(int a, int b, int c)
{
    printf("C function is called\n"); 
    printf("%d %d %d\n",a,b,c);
}

void D(int a, int b, int c, int d)
{
    printf("D function is called\n");
        printf("%d %d %d %d\n",a,b,c,d);
}

int main(int argc, char** argv)
{
        char buffer[128];
        strcpy(buffer, argv[1]);
        return 0;
}