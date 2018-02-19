`python -c 'print "A"*48 + " " + "B"*512 '`



(gdb) disassemble main
Dump of assembler code for function main:
0x8048500 <main>:	push   %ebp
0x8048501 <main+1>:	mov    %ebp,%esp
0x8048503 <main+3>:	sub    %esp,44
0x8048506 <main+6>:	cmp    DWORD PTR [%ebp+8],1
0x804850a <main+10>:	jg     0x8048523 <main+35>
0x804850c <main+12>:	push   0x8048630
0x8048511 <main+17>:	call   0x8048410 <printf>
0x8048516 <main+22>:	add    %esp,4
0x8048519 <main+25>:	push   0
0x804851b <main+27>:	call   0x8048420 <exit>
0x8048520 <main+32>:	add    %esp,4
0x8048523 <main+35>:	nop    
0x8048524 <main+36>:	mov    DWORD PTR [%ebp-44],0x0
0x804852b <main+43>:	nop    
0x804852c <main+44>:	lea    %esi,[%esi*1]
0x8048530 <main+48>:	mov    %eax,DWORD PTR [%ebp-44]
0x8048533 <main+51>:	lea    %edx,[%eax*4]
0x804853a <main+58>:	mov    %eax,%ds:0x8049750
0x804853f <main+63>:	cmp    DWORD PTR [%eax+%edx],0
0x8048543 <main+67>:	jne    0x8048547 <main+71>
0x8048545 <main+69>:	jmp    0x8048587 <main+135>
0x8048547 <main+71>:	mov    %eax,DWORD PTR [%ebp-44]
0x804854a <main+74>:	lea    %edx,[%eax*4]
0x8048551 <main+81>:	mov    %eax,%ds:0x8049750
0x8048556 <main+86>:	mov    %edx,DWORD PTR [%eax+%edx]
0x8048559 <main+89>:	push   %edx
0x804855a <main+90>:	call   0x80483f0 <strlen>
0x804855f <main+95>:	add    %esp,4
0x8048562 <main+98>:	mov    %eax,%eax
0x8048564 <main+100>:	push   %eax
---Type <return> to continue, or q <return> to quit---  
0x8048565 <main+101>:	push   0
0x8048567 <main+103>:	mov    %eax,DWORD PTR [%ebp-44]
0x804856a <main+106>:	lea    %edx,[%eax*4]
0x8048571 <main+113>:	mov    %eax,%ds:0x8049750
0x8048576 <main+118>:	mov    %edx,DWORD PTR [%eax+%edx]
0x8048579 <main+121>:	push   %edx
0x804857a <main+122>:	call   0x8048430 <memset>
0x804857f <main+127>:	add    %esp,12
0x8048582 <main+130>:	inc    DWORD PTR [%ebp-44]
0x8048585 <main+133>:	jmp    0x8048530 <main+48>
0x8048587 <main+135>:	mov    %eax,DWORD PTR [%ebp+12]
0x804858a <main+138>:	add    %eax,4
0x804858d <main+141>:	mov    %edx,DWORD PTR [%eax]
0x804858f <main+143>:	add    %edx,47
0x8048592 <main+146>:	cmp    BYTE PTR [%edx],0xbf
0x8048595 <main+149>:	je     0x80485b0 <main+176>
0x8048597 <main+151>:	push   0x804863c
0x804859c <main+156>:	call   0x8048410 <printf>
0x80485a1 <main+161>:	add    %esp,4
0x80485a4 <main+164>:	push   0
0x80485a6 <main+166>:	call   0x8048420 <exit>
0x80485ab <main+171>:	add    %esp,4
0x80485ae <main+174>:	mov    %esi,%esi
0x80485b0 <main+176>:	mov    %eax,DWORD PTR [%ebp+12]
0x80485b3 <main+179>:	add    %eax,4
0x80485b6 <main+182>:	mov    %edx,DWORD PTR [%eax]
0x80485b8 <main+184>:	push   %edx
0x80485b9 <main+185>:	lea    %eax,[%ebp-40]
0x80485bc <main+188>:	push   %eax
0x80485bd <main+189>:	call   0x8048440 <strcpy>
0x80485c2 <main+194>:	add    %esp,8
---Type <return> to continue, or q <return> to quit---
0x80485c5 <main+197>:	lea    %eax,[%ebp-40]
0x80485c8 <main+200>:	push   %eax
0x80485c9 <main+201>:	push   0x8048659
0x80485ce <main+206>:	call   0x8048410 <printf>
0x80485d3 <main+211>:	add    %esp,8
0x80485d6 <main+214>:	leave  
0x80485d7 <main+215>:	ret    
0x80485d8 <main+216>:	nop    
0x80485d9 <main+217>:	nop    
0x80485da <main+218>:	nop    
0x80485db <main+219>:	nop    
0x80485dc <main+220>:	nop    
0x80485dd <main+221>:	nop    
0x80485de <main+222>:	nop    
0x80485df <main+223>:	nop    
End of assembler dump.
