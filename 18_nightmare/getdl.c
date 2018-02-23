#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

#define LIBC "/lib/libc.so.6"

int main()
{
    void *handle;
    long strcpyAddr;

    handle = dlopen(LIBC, RTLD_LAZY);
    strcpyAddr = (long)dlsym(handle, "strcpy");
    dlclose(handle);

    printf("%x\n", strcpyAddr - 0x4000);
    return 0;
}
