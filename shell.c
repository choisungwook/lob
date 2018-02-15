#include <stdio.h>

int main()
{
    char *buf[] = {"/bin/sh", 0};
    execve(buf[0], buf, 0);
    return 0;
}

