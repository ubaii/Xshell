#!/usr/bin/env python
from urllib import urlopen, urlencode
from re import search
import sys,os
def omega():
    data = urlencode({"hash":hashvalue, "decrypt":"Decrypt"})
    html = urlopen("http://md5decrypt.net/en/Sha256/", data)
    find = html.read()
    match = search (r'<b>[^<]*</b><br/><br/>', find)
    if match:
        print "\n\033[1;32m[+] Sukses hash:\033[1;m", match.group().split('<b>')[1][:-14]
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Kode hash tidak di temukan di database."
        sys.exit()

def Lambda():
    html = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashvalue+"&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728")
    find = html.read()
    if len(find) > 0:
        print "\n\033[1;32m[+] sukses:\033[1;m", find
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Kode hash tidak di temukan di database."
        sys.exit()
def beta():
    data = urlencode({"auth":"8272hgt", "hash":hashvalue, "string":"","Submit":"Submit"})
    html = urlopen("http://hashcrack.com/index.php" , data)
    find = html.read()
    match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', find)
    if match:
        print "\n\033[1;32m[+] Sukses hash:\033[1;m", match.group().split('hervorheb2>')[1][:-18]
        sys.exit()
    else:
        omega()
print((56 * '\033[31m-\033[1;m'))
print "\t\033[97m     Dibuat oleh: \033[1;m\033[1;31m<3\033[1;31m\033[97m INDONESIAN CODER\033[1;m"
print """\033[1;97mThanks: Mas yugeng,om Yudi, all member INDONESIA CODER \033[1;m"""
print "\033[1;32mServers database: Alpha, Beta, Gamma, Delta, Omega, Lambda, hashKiller\033[1;m"
print((56 * '\033[31m-\033[1;m'))
hashvalue = raw_input('\033[97mKode hash: \033[1;m').lower()
if len(hashvalue) == 32:
    print "\033[1;33m[!]\033[1;m Kode Hash : MD5"
    data = urlencode({"hash":hashvalue,"submit":"Decrypt It!"})
    html = urlopen("http://md5decryption.com", data)
    find = html.read()
    match = search(r"Decrypted : </b>[^<]*</font>", find)
    if match:
        print "\n\033[1;32m[+] Hash sukses :\033[1;m", match.group().split('b>')[1][:-7]
        sys.exit()
    else:
        data = urlencode({"md5":hashvalue,"x":"21","y":"8"})
        html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data)
        find = html.read()
        match = search (r"<span class='middle_title'>Sedang mencari hash yg cocok.</span>: [^<]*</div>", find)    
        if match:
            print "\n\033[1;32m[+] sukses di hash:\033[1;m", match.group().split('span')[2][3:-6]
            sys.exit()
        else:
            url = "http://www.nitrxgen.net/md5db/" + hashvalue
            purl = urlopen(url).read()
            if len(purl) > 0:
                print "\n\033[1;32m[+] Hash sukses :\033[1;m", purl
                sys.exit()
            else:
                print "\033[1;31m[-]\033[1;m kode hash tidak ada di database!"
                sys.exit()
if len(hashvalue) == 40:
    print "\033[1;33m[!]\033[1;m Hash : SHA1"
    beta()
if len(hashvalue) == 64:
    print "\033[1;33m[!]\033[1;m Hash : SHA-256"
    Lambda()
else:
    print "\033[1;31m[-]\033[1;m Hash tidak cocok."
