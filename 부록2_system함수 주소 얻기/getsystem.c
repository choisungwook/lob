/*
컴파일러 옵션 -ldl 필요
*/

#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#define LIBC "/lib/libc.so.6"

int main()
{
        void* handle;
        long systemAddr;

        handle = dlopen(LIBC, RTLD_LAZY);
        systemAddr = (long)dlsym(handle, "system") -0x4000;
        dlclose(handle);

        printf("system addr : %x\n", systemAddr);

        //baseaddress : systemAddr
        //offset : "/bin/sh"
        while(memcmp((void*)systemAddr, "/bin/sh", 8)){
            systemAddr++;
        }

        printf("system addr : %x\n", systemAddr-0x4000);
        return 0;
}