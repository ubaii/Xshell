# Create python3 
# Author Ubaii ID

import urllib.request  as urllib2 
import re
import sys,os,time
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
 
def info():
  os.system('clear')
  print("\n[ OS: ]")
  os.system("uname -o")
  print(G+"""
   XSHELL FRAMEWORK - CREATED BY UBAII ID
  (bantuan)Jika program ini bermasalah,harap 
beri tau saya.
kontak : fb.com/ubaii.id.9
Script ini boleh di edit/Recoded. asal intro jangan
di ganti!! 
Thanks : ALLAH SWT. Ubaii ID(author) Mas Mukti(mastah Termux) mas yugeng(Script editing) hery(Design Creator) Mas Yusril(Mastah Termux).""")

def heads():
	global head
	head = E+H+"""
   XXXXXXXXX      XXXXXXXXX
    XXXXXXXXX    XXXXXXXXX
     XXXXXXXXX  XXXXXXXXX
      """+F+"""XXXXXXXXXXXXXXXXXX
      """+F+"""XXXXXXXXXXXXXXXXXX
     """+H+"""XXXXXXXXX  XXXXXXXXX
    XXXXXXXXX    XXXXXXXXX
   XXXXXXXXX      XXXXXXXXX     """+G+"""v2
"""+E

def tol():
	print(G+'''
	Browser tool by Ubaii ID
  	'''+F+'''
  	Browser tool by INDONESIA CODER - Ubaii ID
  	'''+W+'''(---------+---------)
'''+E)

	print(G+'''
	BROWSER TOOL BY UBAII ID
  	'''+F+'''
  	1) Browser dengan lynx
  	2) Browser dengan w3m
      3) KELUAR
  	'''+W+'''(---------+---------)
'''+E)
	try:
		v = input(G+'Xshell/browser-»')
		b = input('link yg pengen di tuju->')
	except:
		print(' Wakwau,:v ')
		exit()
	
	if v == 'bantuan':
		info()
	elif int(v) == 1:
		os.system('lynx '+b)
	elif int(v) == 2:
		os.system('w3m '+b)
	elif int(v) == 3:
		Index()

def satu():
	os.system('php def.php')

def dua():
	print(head)
	print(G+'''
	Menu Bruteforce
  	'''+G+'''
  	1) Bruteforce Facebook
  	2) Bruteforce Instagram
  	3) Bruteforce FTP
  	4) Bruteforce Cpanel
  	5) Bruteforce mail
        6) Bruteforce Revenue
        7) KELUAR
  	'''+H+'''(---------+---------)
     Ketik 'bantu' untuk panduan cara penggunaan.
'''+E)
	try:
		g = input(G+'Xshell/brute-»')
	except:
		print(' Wakwau,:v ')
		exit()
	
	if g == 'bantu':
		info()
	elif int(g) == 1:
		br = input('Target ID_>')
		os.system('''python2 modules/fb.py '''+br+''' pas.txt''')
	elif int(g) == 2:
		lr = input('username korban: ')
		os.system('''python2 modules/ig.py '''+lr+''' pas.txt''')
	elif int(g) == 3:
		brut_ftp()
	elif int(g) == 4:
		df = input('link cpanel : ')
		os.system('''python2 modules/cp.py '''+df+''' pas.txt''')
	elif int(g) == 5:
		brut_mail()
	elif int(g) == 6:
		to = input('Username revenue: ')
		os.system('''python2 modules/rf.py '''+to+''' pas.txt''')
	elif int(g) == 7:
		print('''    Selamat TENGGAL   ''')
		exit()

def tiga():
	print(F+'Membuka Lazymux.')
	time.sleep(3)
	os.system('python2 lazymux.py')

def empat():
	print(G+'Membuka Hash Tool...')
	time.sleep(4)
	os.system('python2 rwds.py')

def lima():
	os.system('clear')
	print(head)
	print('Website target:')
	site = input(B+'Xshell»Dos»'+E)
	print('''Tipe dos:
		1) hard dos
 		2) Low dos''')
	level = int(input(B+'Xshell»Dos»Level»'+E))
	if level == 1:
		os.system('python3 modules/dos2.py '+site)
	if level == 2:
		os.system('python3 modules/dos.py '+site)

def enam():
  os.system('clear')
  print('INFORMASI PERANGKAT')
  print('By Ubaii ID:\n')
  print('[ Sttatus: ]')
  os.system('uname -n\n')
  print('\n[ Kernel: ]')
  os.system("uname -s")
  print("\n[ Versi Kernel: ]")
  os.system("uname -v")
  os.system("uname -r")
  print("\n[ OS: ]")
  os.system("uname -o")
  print("\n[ Hardware: ]")
  os.system("uname -m")
  print("\n[ Processor: ]")
  os.system("uname -p")
  print("\n[ Status hardware: ]")
  os.system("uname -i")
  time.sleep(4)
  Index()

def brut_ftp():
	os.system('clear')
	print(head)
	print(F+'SSH Bruteforce,'+E)
	print(B+'Enter host:'+E)
	host = input(W+'Xshell»Ftp»Host»'+E)
	print(B+'User:'+E)
	print(F+'Default: admin')
	user = input(W+'Xshell»Ftp»User»'+E)
	print(B+'Ketik (pas.txt) untuk start bruteforce'+E)
	password_list = input(W+'Xshell»Ftp»Password»'+E)
	if user == '':
		user = 'admin'
	if password_list == '':
		print('Ketik : "pas.txt"')
		sys.exit(1)
	os.system('python3 modules/ftp.py '+host+' '+user+' '+password_list)


def brut_mail():
	os.system('clear')
	print(head)
	print(H+'Brut mail account'+E)
	print(B+'Email :'+E)
	mail = input(W+'Xshell»Mail»Login»'+E)
	print(B+'Ketik (pas.txt):'+E)
	password = input(W+'Xshell»Mail»Password»'+E)
	if password == '':
		print(F+'Password list: password/password_list.txt'+E)
		password = 'password/password_list.txt'
	os.system('python3 modules/mail.py '+mail+' '+password)

def Index():
	print(head)
	print(G+'''
	Menu Xshell v2
  	'''+F+'''
  	1) Deface
  	2) Bruteforce
  	3) Install tools
  	'''+H+'''
  	4) Hash Tool
  	5) Dos tool
  	6) My device
        7) Browser tool
        8) KELUAR
  	'''+W+'''(---------+---------)
     Ketik 'bantu' untuk panduan cara penggunaan.
'''+E)
	try:
		v = input(G+'Xshell-»')
	except:
		print(' Wakwau,:v ')
		exit()
	
	if v == 'bantu':
		info()
	elif int(v) == 1:
		satu()
	elif int(v) == 2:
		dua()
	elif int(v) == 3:
		tiga()
	elif int(v) == 4:
		empat()
	elif int(v) == 5:
		lima()
	elif int(v) == 6:
		enam()
	elif int(v) == 7:
		tol()
	elif int(v) == 8:
		exit()
heads()
Index()

