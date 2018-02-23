#include <dlfcn.h>
#include <stdlib.h>
#include <stdio.h>

#define LIBC "/lib/libc.so.6"

int main()
{
    void* handle;
    long systemAddr, binshAddr;

    handle = dlopen(LIBC, RTLD_LAZY);
    systemAddr = (long)dlsym(handle, "system");
    dlclose(handle);

    while(memcmp((void*)systemAddr, "/bin/sh" ,8))
        systemAddr++;

    printf("%x\n", systemAddr-0x4000);

    return 0;
}